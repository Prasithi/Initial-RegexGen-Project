import re

def analyze_language(language):

    language = language.lower()

    analysis = {}

    if "digits" in language:
        analysis["type"] = "digits"

    elif "alphabets" in language:
        analysis["type"] = "alphabets"

    elif "binary" in language:
        analysis["type"] = "binary"

    elif "email" in language:
        analysis["type"] = "email"

    elif "phone" in language:
        analysis["type"] = "phone"

    elif "url" in language:
        analysis["type"] = "url"

    elif "substring" in language:

        match = re.search(r"substring\s+(\w+)", language)

        if match:
            analysis["substring"] = match.group(1)

    elif "starts with" in language:

        match = re.search(r"starts with\s+(\w+)", language)

        if match:
            analysis["start"] = match.group(1)

    elif "ends with" in language:

        match = re.search(r"ends with\s+(\w+)", language)

        if match:
            analysis["end"] = match.group(1)

    return analysis