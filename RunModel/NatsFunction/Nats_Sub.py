from config.Config import cfg
from NatsFunction.Nats_Send_New import send_to_next_agent
from NatsFunction.Connection_to_Nats import nc  

subscriptions = {}  # Track subscriptions by subject


async def message_handler(msg):
    data_str = msg.data.decode("utf-8", errors="replace")
    await send_to_next_agent(data_str)


async def start_nats_subscriber(subject: str):
    global subscriptions
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    sub = await nc.subscribe(subject, cb=message_handler)
    subscriptions[subject] = sub
    print(f"Subscribed to '{subject}'")


async def start_nats_subscriber_with_js(subject: str, durable_name: str = "default_durable"):
    global subscriptions
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    js = nc.jetstream()
    sub = await js.subscribe(subject, cb=message_handler, durable=durable_name)
    subscriptions[subject] = sub
    print(f"Subscribed to JetStream subject: '{subject}', durable: '{durable_name}'")


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