import asyncio
import json
from nats.aio.client import Client as NATS
from config.Config import Config

cfg = Config()

async def publish_message(subject: str, message: dict):
    nc = NATS()
    await nc.connect(cfg.NAT_SERVER_URL)
    
    #JetStream support
    #js = nc.jetstream()
    # await js.publish(subject, json.dumps(message).encode())
    
    #Non-JetStream support
    await nc.publish(subject, json.dumps(message).encode())
    
    print(f"Published message to subject '{subject}'")
    await nc.drain()

# Standalone for CLI testing
if __name__ == "__main__":
    import sys
    subject = sys.argv[1] if len(sys.argv) > 1 else "alert.default"
    message = {
        "alert": {"id": "cli-call"},
        "triage": {
            "triage_level": "Low",
            "score": 1,
            "mitre_ids": [],
            "src_ip": [],
            "severity": "info"
        }
    }
    asyncio.run(publish_message(subject, message))
