import asyncio
from nats.aio.client import Client as NATS
from nats.js.api import StreamConfig
from nats.js.errors import NotFoundError

async def close_jetstream_stream(nats_server_url: str, stream_name: str):
    """
    Connects to a NATS server and deletes the given JetStream stream.

    Args:
        nats_server_url (str): The NATS server URL (e.g., "nats://localhost:4222")
        stream_name (str): The name of the JetStream stream to delete

    Example:
        asyncio.run(close_jetstream_stream("nats://localhost:4222", "mystream"))
    """
    nc = NATS()
    try:
        await nc.connect(servers=[nats_server_url])
        js = nc.jetstream()

        # Try to delete the stream
        try:
            await js.delete_stream(stream_name)
            print(f"Stream '{stream_name}' deleted successfully.")
        except NotFoundError:
            print(f"Stream '{stream_name}' does not exist.")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        await nc.drain()

# For manual testing:
if __name__ == "__main__":
    asyncio.run(close_jetstream_stream("nats://localhost:4222", "mystream"))