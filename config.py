"""Configuration for the book generation system"""
from typing import Dict

def get_config() -> Dict:
    """Get the configuration for the agents using GPT-4"""

    # Directly specify the OpenAI API key here
    openai_api_key = "sk-None-Your-OpenAI-API-Key-Here"

    # Config for GPT-4 via OpenAI API
    config_list = [{
        'model': 'gpt-4-turbo',
        'base_url': "https://api.openai.com/v1",
        'api_key': openai_api_key
    }]

    # Common configuration for all agents
    agent_config = {
        "seed": 42,
        "temperature": 0.7,
        "config_list": config_list,
        "timeout": 600,
        "cache_seed": None
    }
    
    return agent_config
