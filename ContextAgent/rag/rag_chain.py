import json
import os
from langchain.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain.chains import LLMChain
from rag.rag_vector_db import load_vectorstore
from config.Config import cfg

def build_rag_chain():
    retriever = load_vectorstore().as_retriever(search_type="similarity", search_kwargs={"k": 4})

    template_path = os.path.join("tools", "RAG_Template.txt")
    with open(template_path, "r", encoding="utf-8") as f:
        prompt_template = f.read()

    prompt = PromptTemplate(
        input_variables=["log", "mitre_attack_type", "client_tools_json", "question", "context"],
        template=prompt_template
    )

    llm = OllamaLLM(
        base_url=cfg.LOCAL_LLM_URL,
        model=cfg.LLM_MODEL,
        temperature=cfg.LLM_TEMPERATURE,
    )

    chain = LLMChain(llm=llm, prompt=prompt, verbose=True)

    def run_chain(
        log: dict,
        mitre_attack_type: dict,
        client_tools_json: dict,
        question: str = "What action should be taken?"
    ) -> str:
        docs = retriever.get_relevant_documents(question)
        context = "\n\n".join([doc.page_content for doc in docs])

        return chain.run({
            "log": json.dumps(log, indent=2),
            "mitre_attack_type": json.dumps(mitre_attack_type, indent=2),
            "client_tools_json": json.dumps(client_tools_json, indent=2),
            "question": question,
            "context": context,
        })

    return run_chain
