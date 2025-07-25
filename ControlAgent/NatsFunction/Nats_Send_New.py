from contexts.Recommendation_From_Log import call_recommendation_agent_from_script
from NatsFunction.Nats_Pub import publish_Js_message as publish_js_message
import json
from config.Config import cfg
subscribed_subject = None

async def send_to_next_agent(data_str):
    #Log the received message
    
    data_dict = json.loads(data_str)
    print(f"log received data: {data_dict}")
    try:    
        #Run The Model and Publish the result
        result = await call_recommendation_agent_from_script(data_dict)
        Pub_Out = await publish_js_message(cfg.OUTPUT_SUBJECT, result)
        print(f"Data Sucessfully Pub : {Pub_Out}")
        
    except Exception as e:
        data_str = f"<decode-error: {e}>"
        with open("log.txt", "a", encoding="utf-8") as f:
            f.write(data_str)