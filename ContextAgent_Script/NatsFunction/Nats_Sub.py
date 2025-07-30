from config.Config import cfg
from NatsFunction.Nats_Send_New import send_to_next_agent,send_to_next_agent_json
from NatsFunction.Nats_Client import nc  
from nats.js.api import DeliverPolicy
from agents.create_single_agent import call_single_recommendation_agent
from nats.js.api import ConsumerConfig
subscriptions = {}  # Track subscriptions by subject

async def message_handler(msg):

    
    subject = msg.subject
    data_str = msg.data.decode("utf-8", errors="replace")

    print("📥 New NATS message received")
    print(f"📨 Subject: {subject}")
    print(f"🔁 Reply-to: {msg.reply}")
    print(f"🧾 Raw message: {repr(data_str)}")

    try:
        meta = msg.metadata  # Correct usage
        print("📦 JetStream Metadata:")
        print(f"   • Stream: {meta.stream}")
        print(f"   • Consumer: {meta.consumer}")
        print(f"   • Sequence (Stream): {meta.sequence.stream}")
        print(f"   • Sequence (Consumer): {meta.sequence.consumer}")
        print(f"   • Timestamp: {meta.timestamp}")
        print(f"   • Delivery Attempt: {meta.num_delivered}")
        print(f"   • Pending: {meta.num_pending}")
        if meta.num_delivered > 1:
            print(f"   ⚠️ Redelivered (attempt #{meta.num_delivered})")
    except Exception as e:
        print("ℹ️ JetStream metadata not available or not a JetStream message.")
        print(f"   ❌ Reason: {e}")

    # # await msg.ack()

    if not data_str.strip():
        print("⚠️ Empty message — skipping.")
        return None

    try:
        await send_to_next_agent_json(data_str)
    except Exception as e:
        print("❌ Error during agent processing:", e)
        print(f"📥 {msg.subject} - {repr(msg.data.decode())}")
    finally :
        await msg.ack()
        print("✅ ACK sent")
    




async def start_nats_subscriber(subject: str):
    global subscriptions
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    sub = await nc.subscribe(subject, cb=message_handler)
    subscriptions[subject] = sub
    print(f"Subscribed to '{subject}'")
    
    
async def start_nats_subscriber_with_js(subject: str, durable_name: str = "default_durable", queue_name: str = None):
    global subscriptions
    
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)

    js = nc.jetstream()
    
    consumer_config1 = ConsumerConfig(
        ack_wait=250
    )
    # 🧠 Add `queue=...` if queue_name is provided
    if queue_name:
        sub = await js.subscribe(
            subject,
            cb=message_handler
            ,durable=durable_name
            #,queue=queue_name
            ,deliver_policy=DeliverPolicy.NEW
            ,config = consumer_config1
        )
        #print(f"Subscribed with queue group: '{queue_name}'")
    else:
        sub = await js.subscribe(
            subject,
            cb=message_handler,
            durable=durable_name
        )
        print("Subscribed without queue group")

    subscriptions[subject] = sub
    print(f"✅ Subscribed to JetStream subject: '{subject}', durable: '{durable_name}'")

async def stop_nats_subscriber(subject: str):
    global subscriptions
    if subject in subscriptions:
        sub = subscriptions[subject]
        await sub.unsubscribe()
        del subscriptions[subject]
        print(f"Unsubscribed from subject '{subject}'")
    else:
        print(f"No active subscription found for subject '{subject}'")

def show_subscriptions() -> list[str]:
    if not subscriptions:
        return []
    return list(subscriptions.keys())

"""
#Code for without queue
async def start_nats_subscriber_with_js(subject: str, durable_name: str = "default_durable"):
    global subscriptions
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    js = nc.jetstream()
    sub = await js.subscribe(subject, cb=message_handler, durable=durable_name)
    subscriptions[subject] = sub
    print(f"Subscribed to JetStream subject: '{subject}', durable: '{durable_name}'")
"""