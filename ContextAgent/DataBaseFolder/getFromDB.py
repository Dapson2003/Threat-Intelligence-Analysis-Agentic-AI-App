# tools/onboarding_tool.py
from typing import List, Optional
from pydantic import BaseModel, Field
from langchain.tools import tool
from enum import Enum

"""
Tool Context:

This module defines LangChain-compatible tools for agent use:

1. `query_onboarding_database`
   - Purpose: Construct SQL queries to retrieve stored onboarding records.
   - Use when: The agent needs historical or structured data already persisted in the system.
   - Data Source: `onboarding_records` table in the database.

Important Notes for Agent:
- This tool does not connect to JetStream or any live messaging system.
- It generates SQL queries only and does not run them.
- Use it when working with onboarding-related records (technologies, assets, devices, network data).
"""

# ---------- ENUMS ----------

class OnLocation(str, Enum):
    ON_PREMISES = "ON_PREMISES"
    ON_CLOUD = "ON_CLOUD"

class Technology(str, Enum):
    ANTIVIRUS = "ANTIVIRUS"
    EDR = "EDR"
    NDR = "NDR"
    NEXTGENERATIONFIREWALL = "NEXTGENERATIONFIREWALL"
    NIDS_NIPS = "NIDS_NIPS"
    HOSTBASEDDLP = "HOSTBASEDDLP"
    SIEM_ELK = "SIEM_ELK"
    NETWORKBASEDDLP = "NETWORKBASEDDLP"
    NAC = "NAC"
    IAM = "IAM"
    TWOFACTORAUTHENTICATION = "TWOFACTORAUTHENTICATION"
    EMAILGATEWAY = "EMAILGATEWAY"
    WEBGATEWAY = "WEBGATEWAY"
    SOAR = "SOAR"
    USBCONTROL = "USBCONTROL"
    WAF = "WAF"
    FULLDISKENCRYPTION = "FULLDISKENCRYPTION"
    THREATINTELLIGENCEPLATFORM = "THREATINTELLIGENCEPLATFORM"
    APPLICATIONWHITELISTING = "APPLICATIONWHITELISTING"
    SANDBOX = "SANDBOX"
    DAM = "DAM"
    FIM = "FIM"
    OSPATCHING = "OSPATCHING"
    THIRDPARTYAPPPATCHING = "THIRDPARTYAPPPATCHING"
    VULNERABILITYASSESSMENT = "VULNERABILITYASSESSMENT"
    ANTIDDOS = "ANTIDDOS"
    ASSETMANAGEMENT = "ASSETMANAGEMENT"
    GRC = "GRC"
    ICS_SCADA_NIDS = "ICS_SCADA_NIDS"
    PAM = "PAM"
    OTHERS = "OTHERS"

# ---------- MODELS ----------

class TechnologicalInput(BaseModel):
    technology: Technology
    product: Optional[str] = None

class CustomerNetworkInfoInput(BaseModel):
    ip: str
    description: str

class CustomerDeviceInput(BaseModel):
    deviceType: Optional[str] = None
    vendor: Optional[str] = None
    os: Optional[str] = None
    amount: Optional[int] = None

class MonitorAssetInfoInput(BaseModel):
    purpose: str
    productName: str
    os: Optional[str] = None
    version: Optional[str] = None
    ipAddress: Optional[str] = None
    hostname: Optional[str] = None
    assetLocation: OnLocation
    isVm: bool
    inProduction: bool
    hasApi: bool

class OnBoardingInput(BaseModel):
    currentTechnologies: Optional[List[TechnologicalInput]] = []
    monitorAssets: Optional[List[MonitorAssetInfoInput]] = []
    devices: Optional[List[CustomerDeviceInput]] = []
    networkInfos: Optional[List[CustomerNetworkInfoInput]] = []

# ---------- TOOLS ----------

class QueryOnboardingDBInput(BaseModel):
    asset_location: Optional[OnLocation] = Field(None, description="Filter by asset location (ON_PREMISES or ON_CLOUD)")
    technology: Optional[Technology] = Field(None, description="Filter by technology type")
    hostname: Optional[str] = Field(None, description="Filter by hostname")

@tool("query_onboarding_database", args_schema=QueryOnboardingDBInput)
def query_onboarding_database(input_data: QueryOnboardingDBInput) -> str:
    """
    Construct a simulated query string to retrieve specific onboarding technologies, tools, or assets
    that could assist in investigating a security log event mapped to a MITRE ATT&CK technique.

    You must only query the fields relevant to the technique in question.

    Choose from:
    - currentTechnologies (technology: enum Technology, product: string)
    - monitorAssets (hostname, os, productName, purpose, hasApi, assetLocation)
    - devices (deviceType, os, vendor)
    - networkInfos (ip, description)

    Your output must:
    - Identify tools or assets relevant to the technique (e.g., EDR for process abuse, NDR for lateral movement)
    - Justify **why** the selected fields are useful
    - Return a SQL-like query or structured explanation
    """

    where_clauses = []
    if input_data.asset_location:
        where_clauses.append(f"asset_location = '{input_data.asset_location}'")
    if input_data.technology:
        where_clauses.append(f"technology = '{input_data.technology}'")
    if input_data.hostname:
        where_clauses.append(f"hostname ILIKE '%{input_data.hostname}%'")

    where_sql = " AND ".join(where_clauses)
    base_query = "SELECT * FROM onboarding_records"
    query = f"{base_query} WHERE {where_sql}" if where_clauses else base_query

    print("[Prototype] Simulated DB Query:", query)
    return query
