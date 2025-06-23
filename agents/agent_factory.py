from langchain import hub
#from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import Tool, AgentExecutor, create_react_agent
from langchain_experimental.plan_and_execute import (
    PlanAndExecute,
    load_agent_executor,
    load_chat_planner
)
from langchain_ollama import OllamaLLM

from config import Config
from tools.threat_intelligence_tools import IPIntelligenceTool
from tools.threat_intelligence_tools import GeolocationTool
from tools.threat_intelligence_tools import MalwareAnalysisTool
from tools.threat_intelligence_tools import ThreatScoreAssessmentTool
from tools.threat_intelligence_tools import Retrieve_IP_Info
from tools.threat_intelligence_tools import DomainToIPTool
from langchain_core.callbacks import StdOutCallbackHandler

class ThreatIntelAgentFactory:
    def __init__(self, config: Config):
        self.config = config
        handler = StdOutCallbackHandler()
        self.llm = OllamaLLM(
            model=config.LLM_MODEL,
            #model = 'qwen3:32b',
            temperature=config.LLM_TEMPERATURE,
            callbacks=[handler],
            base_url="http://192.168.123.110:11434"
            )
        print("⚙️ Using LLM_MODEL:", config.LLM_MODEL)

        # Initialize tools
        self.ip_intel_tool = IPIntelligenceTool(config)
        self.geolocation_tool = GeolocationTool(config)
        self.malware_tool = MalwareAnalysisTool(config)
        self.threat_Score_Assessment_tool = ThreatScoreAssessmentTool(config)
        self.retrieve_IP_Info_tool = Retrieve_IP_Info(config)
        self.domain_To_IP_Tool = DomainToIPTool(config)

    def _create_tools(self):
        """Create LangChain tools"""
        return [
            Tool(
                name="IP_Intelligence",
                func=self.ip_intel_tool.process,
                description="Retrieve threat intelligence for an IP address"
            ),
            Tool(
                name="Geolocation",
                func=self.geolocation_tool.process,
                description="Perform geolocation lookup for an IP address, providing city, region, country, and organization details"
            ),
            Tool(
                name="Malware_Analysis",
                func=self.malware_tool.process,
                description="Analyze file hash for malware characteristics"
            ),
            Tool(
                name="Threat_Score_Assessment",
                func=self.threat_Score_Assessment_tool.process,
                description="Calculate a comprehensive threat score for an IP address based on multiple intelligence sources"
            ),
            # Tool(
            #     name="Retrieve_IP_Info",
            #     func=self.retrieve_IP_Info_tool.process,
            #     description="Retrieve threat intelligence information for an IP address from VirusTotal"
            # ),
            Tool(
                name="DomainToIPTool",
                func=self.domain_To_IP_Tool.process,
                description="Retrieve IP addresses Using Domain Name"
            ),
        ]

    def create_react_agent(self):
        """Create a React-style agent"""
        tools = self._create_tools()
        base_prompt = hub.pull("langchain-ai/react-agent-template")

        prompt = base_prompt.partial(
            instructions=(
                "You are a threat intelligence assistant. Your job is to select and use the available tools to answer security-related queries as efficiently as possible.\n\n"
                "IMPORTANT:\n"
                "- Do NOT return JSON, Markdown, or code blocks — respond only in plain text.\n"
                "- Do NOT explain your reasoning outside the required format.\n"
                "- Do NOT add extra commentary.\n"
                "- Avoid parentheses and decorative formatting.\n\n"
                "You must complete **all necessary steps** before providing the final answer.\n"
                "- If the input is a domain, resolve it to an IP address first.\n"
                "- Then perform a threat intelligence scan on that IP.\n"
                #"- If there are samples or indicators, summarize them before finishing.\n"
                "- Don't Summarize the 'Final Answer'\n"
                "- Only write 'Final Answer:' when the full analysis is complete.\n"
                "If you write 'Final Answer:', do not continue with any more Thought, Action, or Observations.\n"
            )
        )
        react_agent = create_react_agent(self.llm, tools, prompt)
        return AgentExecutor(agent=react_agent, tools=tools,max_iterations=15, early_stopping_method="force", verbose=True,handle_parsing_errors=True)

    def create_plan_execute_agent(self):
        """Create a Plan-and-Execute agent"""
        tools = self._create_tools()
        planner = load_chat_planner(self.llm)
        executor = load_agent_executor(self.llm, tools , verbose=True)

        return PlanAndExecute(planner=planner, executor=executor)