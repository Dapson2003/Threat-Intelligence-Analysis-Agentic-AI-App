import os
from nats.aio.client import Client as NATS
from config.Config import Config

cfg = Config()
nc = NATS()
subscribed_subject = None

async def message_handler(msg):
    try:
        # Ensure decoding doesn't fail silently
        data_str = msg.data.decode("utf-8", errors="replace")
    except Exception as e:
        data_str = f"<decode-error: {e}>"

    log_message = f"Received from '{str(msg.subject)}': {str(data_str)}\n"

    # Write to log.txt in main directory
    log_path = os.path.join(os.path.dirname(__file__), "..", "log.txt")
    with open(log_path, "a", encoding="utf-8") as f:
        f.write(log_message)
        
        
async def start_nats_subscriber(subject: str):
    global subscribed_subject
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    await nc.subscribe(subject, cb=message_handler)
    subscribed_subject = subject
    print(f"Subscribed to '{subject}'")

async def stop_nats_subscriber():
    if nc.is_connected:
        await nc.drain()
        await nc.close()
        print(f"Unsubscribed from '{subscribed_subject}'")
