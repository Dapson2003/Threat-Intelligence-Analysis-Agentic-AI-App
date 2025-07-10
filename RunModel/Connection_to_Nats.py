from NatsFunction.Nats_JS_Create import create_js_stream as create_stream
from NatsFunction.Nats_Sub import start_nats_subscriber_with_js
from config.Config import cfg


async def OpenModelServer() :
    """
    This function is used to open the model server.
    It creates a JetStream stream and starts a subscriber for the model server.
    """
    # Create a JetStream stream
    await create_stream("model_server", "agent-type")

    # Start a subscriber for the model server
    await start_nats_subscriber_with_js("agent-type.Input", durable_name="model_server_durable")
    
    print("Model server is running and ready to receive messages.")

