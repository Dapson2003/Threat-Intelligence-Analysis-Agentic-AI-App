# NatsFunction/Nats_Pub.py
import asyncio
import json
from nats.aio.client import Client as NATS
from config.Config import Config

cfg = Config()


async def publish_message():
    nc = NATS()
    await nc.connect(cfg.NAT_SERVER_URL)
    js = nc.jetstream()

    subject = "alert.testtttt"
    message = {
        "alert": {"id": "4fb510f5-dc2d-4d09-8eb7-65656736b84a"},
        "triage": {
            "alert_id": None,
            "alert_name": None,
            "triage_level": "Low",
            "score": 0,
            "mitre_ids": [],
            "src_ip": [],
            "severity": ""
        }
    }

    await js.publish(subject, json.dumps(message).encode())
    print(f"Published message to subject '{subject}'")
    await nc.drain()

# This allows standalone use
if __name__ == "__main__":
    asyncio.run(publish_message())
