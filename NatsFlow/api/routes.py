# api/routes.py
from fastapi import APIRouter
from api import nats_handler
from api.nats_handler import PublishRequest, SubscribeRequest

router = APIRouter()

@router.post("/start-subscriber")
async def start_subscriber(req: SubscribeRequest):
    return await nats_handler.start_subscriber(req)

@router.post("/stop-subscriber")
async def stop_subscriber():
    return await nats_handler.stop_subscriber()

@router.post("/publish")
async def publish(req: PublishRequest):
    return await nats_handler.publish_message(req)
