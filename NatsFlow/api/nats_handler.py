# api/nats_handler.py
from fastapi import Body
from pydantic import BaseModel
import asyncio
from NatsFunction.Nats_Sub import start_nats_subscriber, stop_nats_subscriber
from NatsFunction.Nats_Pub import publish_message as pub_msg

subscriber_task = None

class PublishRequest(BaseModel):
    subject: str
    message: dict

class SubscribeRequest(BaseModel):
    subject: str

async def start_subscriber(req: SubscribeRequest):
    global subscriber_task
    if subscriber_task is None or subscriber_task.done():
        loop = asyncio.get_running_loop()
        subscriber_task = loop.create_task(start_nats_subscriber(req.subject))
        return {"status": f"Subscribed to '{req.subject}'"}
    return {"status": "Subscriber already running"}

async def stop_subscriber():
    global subscriber_task
    await stop_nats_subscriber()
    if subscriber_task:
        subscriber_task.cancel()
        subscriber_task = None
    return {"status": "Subscriber stopped"}

async def publish_message(req: PublishRequest):
    await pub_msg(req.subject, req.message)
    return {"status": f"Message published to '{req.subject}'"}
