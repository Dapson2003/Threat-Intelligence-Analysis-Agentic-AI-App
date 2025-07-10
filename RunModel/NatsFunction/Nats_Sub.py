import os
import json
from nats.aio.client import Client as NATS
from config.Config import cfg
from apis.PredictOne import predict as predict_top7_labels
from NatsFunction.Nats_Pub import publish_Js_message as publish_js_message
from model.runModel import clean_run_prediction

nc = NATS()
subscribed_subject = None

async def message_handler(msg):
    
    data_str = msg.data.decode("utf-8", errors="replace")
    
    #Log the received message
    log_message = f"Received from '{str(msg.subject)}': {data_str}\n"
    with open("log.txt", "a", encoding="utf-8") as f:
        f.write(log_message)
    data_dict = json.loads(data_str)
    print(f"log received data: {data_dict}")
    try:    
        #Run The Model and Publish the result
        result = clean_run_prediction(data_dict)
        Pub_Out = await publish_js_message(cfg.OUTPUT_SUBJECT, result)
        print(f"Data Sucessfully Pub : {Pub_Out}")
        
    except Exception as e:
        data_str = f"<decode-error: {e}>"
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(data_str)
        
async def start_nats_subscriber(subject: str):
    global subscribed_subject
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    await nc.subscribe(subject, cb=message_handler)
    subscribed_subject = subject
    print(f"Subscribed to '{subject}'")
    
async def start_nats_subscriber_with_js(subject: str,durable_name: str = "default_durable"):
    global subscribed_subject
    if not nc.is_connected:
        await nc.connect(cfg.NAT_SERVER_URL)
    
    js = nc.jetstream()
    await js.subscribe(subject, cb=message_handler,durable=durable_name)
    subscribed_subject = subject
    print(f"Subscribed to JetStream subject: '{subject}', durable: '{durable_name}'")

async def stop_nats_subscriber():
    if nc.is_connected:
        await nc.drain()
        await nc.close()
        print(f"Unsubscribed from '{subscribed_subject}'")
