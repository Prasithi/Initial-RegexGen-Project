import re

def analyze_language(language):

    language = language.lower().strip()

    analysis = {}

    if any(word in language for word in [
        "digits",
        "numbers",
        "numeric",
        "integer",
        "only numbers",
        "only digits",
        "number strings",
        "numeric strings",
        "integer value"
    ]):
        analysis["type"] = "digits"

    elif any(word in language for word in [
        "alphabets",
        "letters",
        "alphabetic",
        "characters only",
        "letters only",
        "alphabetic strings",
        "alphabetic strings"
    ]):
        analysis["type"] = "alphabets"

    elif any(word in language for word in [
    "uppercase",
    "capital letters",
    "upper case letters"
]):
        analysis["type"] = "uppercase"
    elif any(word in language for word in [
    "lowercase",
    "small letters",
    "lower case letters"
]):
        analysis["type"] = "lowercase"

    elif any(word in language for word in [
    "binary",
    "binary strings",
    "binary numbers",
    "0 and 1 only"
]):
        analysis["type"] = "binary"

    elif any(word in language for word in [
    "email",
    "email address",
    "mail id",
    "gmail format"
]):
        analysis["type"] = "email"
        
    elif any(word in language for word in [
    "phone",
    "mobile",
    "phone number",
    "mobile number",
    "contact number"
]):
        analysis["type"] = "phone"
    

    elif any(word in language for word in [
    "url",
    "website",
    "web address",
    "website url",
    "link format"
]):
        analysis["type"] = "url"

    elif "hexadecimal" in language:
        analysis["type"] = "hexadecimal"

    elif "floating point" in language or "float" in language:
        analysis["type"] = "float"

    elif "alphanumeric" in language:
        analysis["type"] = "alphanumeric"

    elif "special characters" in language:
        analysis["type"] = "special"

    start_match = re.search(r"starts with\s+(\w+)", language)
    end_match = re.search(r"ends with\s+(\w+)", language)

    if start_match:
        analysis["start"] = start_match.group(1)

    if end_match:
        analysis["end"] = end_match.group(1)

    if "contains substring" in language:
        match = re.search(r"contains substring\s+(\w+)", language)

        if match:
            analysis["substring"] = match.group(1)

    return analysis