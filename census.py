#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Dec 24 11:16:50 2025

@author: sanith
"""
import os
from openai import OpenAI
import openai
import subprocess
import json
import mcp


client = OpenAI()

censusmcp = [
       {
  "mcpServers": {
    "mcp-census-api": {
      "command": "bash",
      "args": [
        "/Users/sanith/Documents/Projects/Census/us-census-bureau-data-api-mcp/scripts/mcp-connect.sh"
      ],
      "env": {
        "CENSUS_API_KEY": "609b71ad5f3e8b6a09cd13dde31cd0d4105da92a"
            }
          }
        }
      }
    
]


response = client.responses.create(
    model ="gpt-5",
    instructions="You are a helpful assistant",
    input="According to Census 2020 what is the population of Maryland?"
    )

print(response.output_text)