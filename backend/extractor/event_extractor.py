import ollama
import json
import re


def extract_event(raw_text):

    prompt = f"""
Extract event information from the text below.

Return ONLY valid JSON.

Fields:
title
date
location
description

Rules:
- title = name of the event
- date = event date
- location = venue or city
- description = event category or type 
- description must NOT include the location

description is important If description is missing return:
"No description"

Text:
{raw_text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    # Extract JSON block using regex
    match = re.search(r'\{.*\}', content, re.DOTALL)

    if match:
        json_text = match.group()

        try:
            return json.loads(json_text)
        except:
            return {"error": "JSON parsing failed", "raw": json_text}

    return {"error": "No JSON found", "raw": content}