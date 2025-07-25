from control.record_alert import append_json
from pathlib import Path
import json
from NatsFunction.Nats_Pub import publish_Js_message

async def send_status(status: int, error: str = None):
    match status:
        case 0:
            print(f"[❌] Unexpected Error: {error}")
        case 1:
            await publish_Js_message(subject="agent-test.websoc", message="status 1")
        case 2:
            await publish_Js_message(subject="agent-test.websoc", message="status 2")
        case 3:
            await publish_Js_message(subject="agent-test.websoc", message="status 3")
        case _:
            print(f"[❌] Impossible status: {status}")
    

from pathlib import Path

async def startFlow(data_str: str) -> str:
    try:
        json_data = json.loads(data_str)
        append_json(file_path=Path("database/start_log.json"), new_entry=json_data)
        await send_status(1)
        return "success"
    except json.JSONDecodeError:
        return "error: invalid JSON"
    except Exception as e:
        return f"error: {str(e)}"

async def finishedType(data_str: str) -> str:
    try:
        data = json.loads(data_str)  # Directly parse the JSON string

        append_json(file_path=Path("database/type_log.json"), new_entry=data)
        await send_status(2)
        return "success"
    except json.JSONDecodeError as e:
        return f"error: invalid JSON - {str(e)}"
    except Exception as e:
        return f"error: {str(e)}"

async def finishedFlow(data_str: str) -> str:
    try:
        data = json.loads(data_str)  # Directly parse the JSON string

        append_json(file_path=Path("database/context_log.json"), new_entry=data)
        await send_status(3)
        return "success"
    except json.JSONDecodeError as e:
        return f"error: invalid JSON - {str(e)}"
    except Exception as e:
        return f"error: {str(e)}"