import asyncio
from nats.aio.client import Client as NATS
from config.Config import Config

cfg = Config()
nc = NATS()
js = None

# Replace this with your actual handler
async def handle_alert_message(msg, agent_executor=None):
    print(f"Handled: {msg.data.decode()}")

async def start_nats_subscriber():
    global js
    await nc.connect(cfg.NAT_SERVER_URL)
    js = nc.jetstream()

    async def callback(msg):
        await handle_alert_message(msg)
        await msg.ack()

    await js.subscribe("alert.testtttt", cb=callback, durable="only-testtttt-Ju2")
    print("Subscribed to 'alert.testtttt' topic.")

async def stop_nats_subscriber():
    if nc.is_connected:
        await nc.drain()
        await nc.close()
        print("NATS connection closed.")
