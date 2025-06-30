import asyncio
from fastapi import FastAPI
from NatsFunction.Nats_Sub import start_nats_subscriber, stop_nats_subscriber
from NatsFunction.Nats_Pub import publish_message

app = FastAPI()
nats_task = None

@app.on_event("startup")
async def startup_event():
    global nats_task
    loop = asyncio.get_event_loop()

    # Start subscriber
    nats_task = loop.create_task(start_nats_subscriber())

    # Wait briefly to ensure subscription happens before publishing
    await asyncio.sleep(2)

    # Publish 3 times
    for i in range(3):
        print(f"Publishing message {i+1}/3...")
        await publish_message()

@app.on_event("shutdown")
async def shutdown_event():
    await stop_nats_subscriber()
