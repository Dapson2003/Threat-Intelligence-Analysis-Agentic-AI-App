import json
from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.callbacks import StdOutCallbackHandler

from config.Config import cfg
from tools.escape_prompt_braces import load_escaped_prompt_template
from tools.Example_Log_Keeper import example_log_body2 as example_log
from tools.Example_Log_Keeper import example_type_body2 as example_type
from contexts.compose_tools_data import compose_full_tools_data_from_log
from typing import Dict, Any


# ✅ Step 1: Load prompt template
prompt_template_str = load_escaped_prompt_template("tools/Recommendation_formated.txt")

prompt = PromptTemplate(
    input_variables=["log", "mitre_attack_type", "client_tools_json"],
    template=prompt_template_str
)

# ✅ Step 2: Initialize LLM and chain only ONCE
handler = StdOutCallbackHandler()
llm = OllamaLLM(
    model=cfg.LLM_MODEL,
    temperature=cfg.LLM_TEMPERATURE,
    callbacks=[handler],
    base_url=cfg.LOCAL_LLM_URL
)

chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

# ✅ Step 3: Call function (to be used in FastAPI or async NATS flow)
async def call_single_recommendation_agent(input_data: Dict[str, Any]) -> Dict[str, Any]:
    try:
        log_data = input_data.get("log", {}).get("node", example_log["node"])
        type_data = input_data.get("type", example_type)
        tools_data = await compose_full_tools_data_from_log({"node": log_data})

        result = chain.run({
            "log": json.dumps(log_data, indent=2),
            "mitre_attack_type": json.dumps(type_data, indent=2),
            "client_tools_json": json.dumps(tools_data, indent=2),
        })

        return {"status": "success", "result": result}
    
    except Exception as e:
        return {"status": "error", "detail": str(e)}
