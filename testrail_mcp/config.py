"""Configuration module for TestRail MCP server."""
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# TestRail configuration
TESTRAIL_URL = os.getenv('TESTRAIL_URL')
TESTRAIL_USERNAME = os.getenv('TESTRAIL_USERNAME')
TESTRAIL_API_KEY = os.getenv('TESTRAIL_API_KEY')
TESTRAIL_MCP_ALLOW_DELETES = os.getenv(
    'TESTRAIL_MCP_ALLOW_DELETES',
    'false'
).strip().lower() in {'1', 'true', 'yes', 'on'}

# Validate configuration
if not all([TESTRAIL_URL, TESTRAIL_USERNAME, TESTRAIL_API_KEY]):
    raise ValueError(
        "Missing TestRail configuration. Please set TESTRAIL_URL, "
        "TESTRAIL_USERNAME, and TESTRAIL_API_KEY environment variables."
    )
