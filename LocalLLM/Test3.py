from langchain import hub

base_prompt = hub.pull("langchain-ai/react-agent-template")
print(base_prompt)