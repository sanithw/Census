#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 19:57:57 2026

@author: sanith
"""

import asyncio
import os

from dotenv import load_dotenv

from agents import Agent, Runner
from agents.mcp import MCPServerStdio
from agents.model_settings import ModelSettings

# Load environment variables from .env file
load_dotenv()

CENSUS_MCP_COMMAND = os.environ.get("CENSUS_MCP_COMMAND", "/Users/sanith/Documents/Projects/Census/us-census-bureau-data-api-mcp/scripts/mcp-connect.sh")
CENSUS_API_KEY = os.environ["CENSUS_API_KEY"]  # must be set

async def main():
    async with MCPServerStdio(
        name="Census MCP",
        params={
            "command": CENSUS_MCP_COMMAND,
            "args": [],
            "env": {**os.environ, "CENSUS_API_KEY": CENSUS_API_KEY},
        },
        cache_tools_list=True,
    ) as census_server:
        agent = Agent(
            name="Census Assistant",
            instructions="Use the Census MCP tools to answer questions about U.S. population and demographics.",
            mcp_servers=[census_server],
            model_settings=ModelSettings(
                model="gpt-4.1-mini",  # any tool-using model
                tool_choice="auto",
            ),
        )

        result = await Runner.run(
            agent,
            "What is the income distribution for FIPS code 24031?",
        )

        print(result.final_output)

if __name__ == "__main__":
    asyncio.run(main())
