#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jan  4 13:38:23 2026

@author: sanith
"""

import asyncio
import json
import os
from typing import Any

from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

CENSUS_MCP_COMMAND = os.environ.get("CENSUS_MCP_COMMAND", "/Users/sanith/Documents/Projects/Census/us-census-bureau-data-api-mcp/scripts/mcp-connect.sh")
CENSUS_API_KEY = os.environ.get("CENSUS_API_KEY")

async def main() -> None:
    if not CENSUS_API_KEY:
        raise RuntimeError("CENSUS_API_KEY environment variable is required")

    server_params = StdioServerParameters(
        command=CENSUS_MCP_COMMAND,
        args=[],
        env={**os.environ, "CENSUS_API_KEY": CENSUS_API_KEY},
    )

    # stdio_client gives you (read, write) streams.[web:10][web:58]
    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:
            init_result = await session.initialize()
            print("Initialized MCP session, capabilities:", init_result.capabilities)

            tools_result = await session.list_tools()
            print("Available tools from Census MCP:")
            for t in tools_result.tools:
                print(f"- {t.name}: {t.description}")

            tool_name = "fetch-aggregate-data"  # adjust to actual tool name exposed by server[web:21]

            arguments: dict[str, Any] = {
                "year": 2023,
                "dataset": "acs/acs5",
                "geography": {"type": "state", "fips": "24"},
                "variables": ["B01003_001E"],
            }

            print(f"\nCalling tool {tool_name} with:\n{json.dumps(arguments, indent=2)}")

            call_result = await session.call_tool(
                name=tool_name,
                arguments=arguments,
            )

            print("\nTool result content:")
            for item in call_result.content:
                if getattr(item, "type", None) == "text":
                    print(item.text)


if __name__ == "__main__":
    asyncio.run(main())
