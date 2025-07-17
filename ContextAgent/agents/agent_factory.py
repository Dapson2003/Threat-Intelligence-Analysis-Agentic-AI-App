from langchain.chains import LLMChain
from langchain_core.prompts import PromptTemplate
from langchain_ollama import OllamaLLM
from langchain_core.callbacks import StdOutCallbackHandler
from langchain.agents import initialize_agent, AgentType
from langchain.tools import Tool
from config.Config import cfg
from DataBaseFolder.getFromDB import query_onboarding_database
from apis.Example_Log_Keeper import example_log_body as example_log
from apis.Example_Log_Keeper import example_type_body as example_type


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
        
    def create_ask_tools_agent(self):
        """
        Creates an agent that reads a security log and a MITRE ATT&CK type,
        then reasons over it to decide which onboarding data to query using available tools.
        """
        with open("agents/Ask_Tools_Template.txt", "r") as f:
            prompt_template = f.read()

        query_tool = Tool(
            name="query_onboarding_database",
            func=query_onboarding_database,
            description=(
                "Use this tool to construct a SQL query for onboarding asset information such as devices, technologies, or systems. "
                "It takes optional filters such as asset location, technology type, or hostname."
            )
        )

        agent = initialize_agent(
            tools=[query_tool],
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            llm=self.llm,
            verbose=True
        )

        def run(log: str, mitre_attack_type: str) -> str:
            prompt = prompt_template.format(log=example_log, mitre_attack_type=example_type)
            return agent.run(prompt)

        return run

    def create_recommending_agent(self):
        """
        Creates an agent that reads a security log and a MITRE ATT&CK type,
        then reasons over it to decide which onboarding data to query using available tools.
        """
        with open("agents/Ask_Tools_Template.txt", "r") as f:
            prompt_template = f.read()

        agent = initialize_agent(
            tools=[],
            agent=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
            llm=self.llm,
            verbose=True
        )

        def run(log: str, mitre_attack_type: str) -> str:
            prompt = prompt_template.format(log=example_log, mitre_attack_type=example_type)
            return agent.run(prompt)

        return run