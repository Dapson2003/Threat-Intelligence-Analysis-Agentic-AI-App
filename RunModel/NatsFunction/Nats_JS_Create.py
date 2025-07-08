import asyncio
from nats.aio.client import Client as NATS
from config.Config import Config
from nats.js.api import StreamConfig

cfg = Config()
async def create_js_stream(input_stream: str, input_filter: dict):

    nc = NATS()
    await nc.connect(cfg.NAT_SERVER_URL)
    
    js = nc.jetstream()

    stream_name = input_stream
    subject_filter = [f"{input_filter}.>"]  # Covers all subjects starting with 'alert.'

    try:
        await js.add_stream(
            config=StreamConfig(
                name=stream_name,
                subjects=subject_filter,
                storage="memory"  # Or use "file" for disk-backed persistence
            )
        )
        print(f"✅ Stream '{stream_name}' created with subject(s): {subject_filter}")
    except Exception as e:
        if "stream name already in use" in str(e).lower():
            print(f"ℹ️ Stream '{stream_name}' already exists.")
        else:
            print(f"❌ Error creating stream: {e}")

    await nc.drain()

# Run the function
if __name__ == "__main__":
    asyncio.run(create_js_stream())