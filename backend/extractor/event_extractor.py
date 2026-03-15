import ollama
import json
import re
import dateparser


"""def normalize_date(date_string):

    parsed = dateparser.parse(date_string)

    if parsed:
        return parsed.strftime("%Y-%m-%d")

    return date_string"""

def normalize_date(date_string):

    import dateparser

    parsed = dateparser.parse(
        date_string,
        languages=["de", "en"]
    )

    if parsed:
        return parsed.strftime("%Y-%m-%d")

    return date_string


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

If description is missing return:
"No description"

Text:
{raw_text}
"""

    response = ollama.chat(
        model="llama3",
        messages=[{"role": "user", "content": prompt}]
    )

    content = response["message"]["content"]

    match = re.search(r'\{[\s\S]*?\}', content)

    if match:

        json_text = match.group()

        try:

            data = json.loads(json_text)

            # normalize date
            if "date" in data:
                data["date"] = normalize_date(data["date"])

            return data

        except Exception:

            return {
                "error": "JSON parsing failed",
                "raw": json_text
            }

    return {
        "error": "No JSON found",
        "raw": content
    }