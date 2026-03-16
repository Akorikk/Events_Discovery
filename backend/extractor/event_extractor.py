import ollama
import json
import dateparser


def normalize_date(date_string):
    """
    Convert different date formats (German/English) into YYYY-MM-DD.
    """

    parsed = dateparser.parse(
        date_string,
        languages=["de", "en"]
    )

    if parsed:
        return parsed.strftime("%Y-%m-%d")

    return date_string


def extract_event(raw_text):
    """
    Use LLM to extract structured event information from raw text.
    """

    prompt = f"""
Extract event information from the text below.

Return ONLY a valid JSON object.
Do NOT include explanations, comments, markdown, or extra text.

Fields:
title
date
location
description

Rules:
- title: name of the event
- date: event date
- location: venue or city name
- description: event category or type

Additional rules:
- description must NOT contain the location
- location must NOT contain time information
- if description is missing return "No description"
- if location is missing return "Unknown"
- if date cannot be determined return "Unknown"

The output MUST follow this exact JSON structure:

{{
  "title": "...",
  "date": "...",
  "location": "...",
  "description": "..."
}}

Return ONLY the JSON object.

Text:
{raw_text}
"""

    try:
        response = ollama.chat(
            model="llama3",
            messages=[{"role": "user", "content": prompt}]
        )

        content = response["message"]["content"]

    except Exception as e:
        return {
            "error": "LLM request failed",
            "raw": str(e)
        }

    # Try to safely extract JSON from model output
    try:

        start = content.find("{")
        end = content.rfind("}") + 1

        if start != -1:

            json_text = content[start:end] if end > start else content[start:]

            json_text = json_text.strip()

            # Fix truncated JSON from LLM
            if not json_text.endswith("}"):
                json_text = json_text + "}"

            data = json.loads(json_text)

            # Normalize date
            if "date" in data:
                data["date"] = normalize_date(data["date"])

            return data

    except Exception:
        return {
            "error": "JSON parsing failed",
            "raw": content
        }

    return {
        "error": "No JSON found",
        "raw": content
    }