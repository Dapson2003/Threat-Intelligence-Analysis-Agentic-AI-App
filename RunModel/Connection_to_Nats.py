from NatsFunction.Nats_JS_Create import create_js_stream as create_stream
from NatsFunction.Nats_Sub import start_nats_subscriber_with_js
from config.Config import cfg


async def OpenModelServer():
    """
    Open the model server:
    - Create a JetStream stream (if it doesn't already exist)
    - Start a subscriber (if not already running)
    """

    # Step 1: Create Stream
    try:
        await create_stream(cfg.STREAM_NAME, cfg.STREAM_PREFIX)
    except Exception as e:
        if "already exists" in str(e).lower() or "stream name already in use" in str(e).lower():
            print(f"ℹ️ Stream '{cfg.STREAM_NAME}' already exists — continuing.")
        else:
            print(f"❌ Unexpected error creating stream: {e}")
            raise

    # Step 2: Start Subscriber
    try:
        await start_nats_subscriber_with_js(
            subject=cfg.INPUT_SUBJECT,
            durable_name=cfg.DURABLE_NAME
        )
    except Exception as e:
        if "consumer name already in use" in str(e).lower() or "already bound" in str(e).lower():
            print(f"ℹ️ Subscriber already exists on subject '{cfg.INPUT_SUBJECT}' with durable '{cfg.DURABLE_NAME}' — continuing.")
        else:
            print(f"❌ Error starting NATS subscriber: {e}")
            raise

    print("✅ Model server is running and ready to receive messages.")
