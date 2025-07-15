from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.callbacks import StdOutCallbackHandler
from config.Config import cfg


class AgentFactory:
    def __init__(self):
        self.config = cfg
        handler = StdOutCallbackHandler()
        self.llm = OllamaLLM(
            model=self.config.LLM_MODEL,
            temperature=self.config.LLM_TEMPERATURE,
            callbacks=[handler],
            base_url=self.config.LOCAL_LLM_URL
        )
        print("⚙️ Using LLM_MODEL:", self.config.LLM_MODEL)

    def create_cybersecurity_answer_agent(self):
            """
            Returns a chain that answers cybersecurity questions intelligently.
            The LLM is instructed to only respond if it is confident.
            """

            prompt_template = PromptTemplate(
                input_variables=["question"],
                template=(
                    "You are a cybersecurity expert AI.\n"
                    "Your task is to answer the following question as accurately as possible.\n"
                    "Only answer if you are confident. If you do not know the answer, say 'I'm not sure about that.'\n\n"
                    "Question: {question}\n\n"
                    "Answer:"
                )
            )

            chain = LLMChain(
                llm=self.llm,
                prompt=prompt_template,
                verbose=True
            )

            return chain