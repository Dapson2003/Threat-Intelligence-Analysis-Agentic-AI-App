import streamlit as st
import json
import os
import sys

PROJECT_ROOT = os.path.abspath(os.path.join(os.path.dirname(__file__), ".."))
if PROJECT_ROOT not in sys.path:
    sys.path.insert(0, PROJECT_ROOT)

from config.Config import Config
from agents.agent_factory import ThreatIntelAgentFactory

class ThreatIntelStreamlitApp:
    def __init__(self):
        # Initialize configuration and agent factory
        self.config = Config()
        self.agent_factory = ThreatIntelAgentFactory(self.config)

    def _render_sidebar(self):
        """Render sidebar with configuration options"""
        st.sidebar.header("🔒 Threat Intelligence Configuration")

        self.agent_type = st.sidebar.radio(
            "Select Agent Type",
            ["React Agent", "Plan and Execute Agent"],
            index=0
        )

        st.sidebar.markdown("""
        ### Example Queries:
        - IP: 77.246.107.91
        - Hash: abc123
        - Analyze threat level
        """)

    def _process_query(self, query):
        """Process query using selected agent"""
        try:
            # Select agent based on user choice
            if self.agent_type == "React Agent":
                agent = self.agent_factory.create_react_agent()
                result = agent.invoke({"input": query})
            else:
                agent = self.agent_factory.create_plan_execute_agent()
                result = agent.invoke(query)

            return result
        except Exception as e:
            return {"error": str(e)}

    def run(self):
        """Main Streamlit application"""
        st.title("🔍 Threat Intelligence Analysis")

        # Render sidebar
        self._render_sidebar()

        # Query input
        query = st.text_input("Enter IP, Hash, or Threat Query:", placeholder="e.g., 77.246.107.91")

        # Process query on button click
        if st.button("Analyze Threat"):
            if not query:
                st.warning("Please enter a query")
                return

            with st.spinner("Analyzing Threat Intelligence..."):
                result = self._process_query(query)

            # Display results
            st.json(result)


def main():
    app = ThreatIntelStreamlitApp()
    app.run()


if __name__ == "__main__":
    main()