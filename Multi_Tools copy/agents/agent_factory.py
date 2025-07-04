from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.callbacks import StdOutCallbackHandler
from config import Config

class AgentFactory:
    def __init__(self, config: Config):
        self.config = config
        handler = StdOutCallbackHandler()
        self.llm = OllamaLLM(
            model=config.LLM_MODEL,
            temperature=config.LLM_TEMPERATURE,
            callbacks=[handler],
            base_url=config.LOCAL_LLM_URL
        )
        print("⚙️ Using LLM_MODEL:", config.LLM_MODEL)

    def create_ftool_selector_agent(self):
        """
        Create a simple agent that uses a prompt template to recommend forensic tools
        based on user input. This does not use ReAct or tool calling.
        """

        with open("./agents/ftool_prompt_template.txt", "r", encoding="utf-8") as f:
            template_str = f.read()

        prompt = PromptTemplate(
            input_variables=["Detection_Types", "Detection_Methods", "Raw_Logs"],
            template=template_str
        )

        chain = LLMChain(
            llm=self.llm,
            prompt=prompt,
            verbose=True
        )

        return chain