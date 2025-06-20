from langchain import hub
from langchain_google_genai import ChatGoogleGenerativeAI
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
from langchain.callbacks.streaming_stdout import StreamingStdOutCallbackHandler
from langchain_core.callbacks import StdOutCallbackHandler

class ThreatIntelAgentFactory:
    def __init__(self, config: Config):
        self.config = config
        handler = StdOutCallbackHandler()
        self.llm = OllamaLLM(
            model=config.LLM_MODEL,
            #model = 'qwen3:32b',
            temperature=config.LLM_TEMPERATURE,
            #callbacks=[handler],
            base_url="http://192.168.123.110:11434"
            )
        print("⚙️ Using LLM_MODEL:", config.LLM_MODEL)

        # Initialize tools
        self.ip_intel_tool = IPIntelligenceTool(config)
        self.geolocation_tool = GeolocationTool(config)
        self.malware_tool = MalwareAnalysisTool(config)
        self.threat_Score_Assessment_tool = ThreatScoreAssessmentTool(config)
        self.retrieve_IP_Info_tool = Retrieve_IP_Info(config)

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
            Tool(
                name="Retrieve_IP_Info",
                func=self.retrieve_IP_Info_tool.process,
                description="Retrieve threat intelligence information for an IP address from VirusTotal"
            ),
        ]

    def create_react_agent(self):
        """Create a React-style agent"""
        tools = self._create_tools()
        base_prompt = hub.pull("langchain-ai/react-agent-template")
        #prompt = base_prompt.partial(instructions="Utilize tools to answer threat intelligence queries")
        prompt = base_prompt.partial(
            instructions=(
                "You are a threat intelligence assistant. Use ONLY the following format to respond:\n\n"
                "Thought: <your reasoning>\n"
                "Action: <the name of the tool to use>\n"
                "Action Input: <the input to that tool>\n\n"
                "You must always return valid plain text — NOT JSON, NOT Python, NOT code blocks.\n"
                "Do NOT use parentheses. Do NOT explain your answer. End with 'Final Answer: <your summary>' when no tool is needed.\n"
                "Do NOT format responses as JSON or Markdown. This is NOT a chat; this is an API agent interface.\n\n"
                "Valid Example:\n"
                "Thought: I need to check the reputation of the IP.\n"
                "Action: IP_Intelligence\n"
                "Action Input: \"8.8.8.8\"\n\n"
                "This is the ONLY correct response format. Any deviation will fail."
            )
        )
        react_agent = create_react_agent(self.llm, tools, prompt)
        return AgentExecutor(agent=react_agent, tools=tools,max_iterations=15, early_stopping_method="force", verbose=True,handle_parsing_errors=True)

    def create_plan_execute_agent(self):
        """Create a Plan-and-Execute agent"""
        tools = self._create_tools()
        planner = load_chat_planner(self.llm)
        executor = load_agent_executor(self.llm, tools ,max_iterations=15, early_stopping_method="force", verbose=True)

        return PlanAndExecute(planner=planner, executor=executor)