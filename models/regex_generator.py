def generate_regex(analysis):

    if analysis.get("type") == "digits":
        return r"^[0-9]+$"

    elif analysis.get("type") == "alphabets":
        return r"^[a-zA-Z]+$"

    elif analysis.get("type") == "uppercase":
        return r"^[A-Z]+$"

    elif analysis.get("type") == "lowercase":
        return r"^[a-z]+$"

    elif analysis.get("type") == "binary":
        return r"^[01]+$"

    elif analysis.get("type") == "email":
        return r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    elif analysis.get("type") == "phone":
        return r"^[0-9]{10}$"

    elif analysis.get("type") == "url":
        return r"^(https?|ftp)://[^\s]+$"

    elif analysis.get("type") == "alphanumeric":
        return r"^[a-zA-Z0-9]+$"

    elif analysis.get("type") == "hexadecimal":
        return r"^[0-9A-Fa-f]+$"

    elif analysis.get("type") == "float":
        return r"^[0-9]+\.[0-9]+$"

    elif analysis.get("type") == "special":
        return r"^[^a-zA-Z0-9]+$"

    elif "start" in analysis and "end" in analysis:
        return f"^{analysis['start']}.*{analysis['end']}$"

    elif "start" in analysis:
        return f"^{analysis['start']}.*"

    elif "end" in analysis:
        return f".*{analysis['end']}$"

    elif "substring" in analysis:
        return f".*{analysis['substring']}.*"

    return "Pattern not supported"