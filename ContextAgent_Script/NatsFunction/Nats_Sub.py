from nats.aio.client import Client as NATS
from NatsFunction.Nats_Send_New import send_to_next_agent
from config.Config import cfg

nc = NATS()


async def message_handler(msg):
    
    data_str = msg.data.decode("utf-8", errors="replace")
    # Optional logging
    log_message = f"Received from '{str(msg.subject)}': {data_str}\n"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_message)
    await send_to_next_agent(data_str)
        
async def start_nats_subscriber(subject: str):
    global subscribed_subject
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    await nc.subscribe(subject, cb=message_handler)
    subscribed_subject = subject
    print(f"Subscribed to '{subject}'")
    
async def start_nats_subscriber_with_js(subject: str,durable_name: str = "default_durable"):
    global subscribed_subject
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    
    js = nc.jetstream()
    await js.subscribe(subject, cb=message_handler,durable=durable_name)
    subscribed_subject = subject
    print(f"Subscribed to JetStream subject: '{subject}', durable: '{durable_name}'")

async def stop_nats_subscriber():
    if nc.is_connected:
        await nc.drain()
        await nc.close()
        print(f"Unsubscribed from '{subscribed_subject}'")
