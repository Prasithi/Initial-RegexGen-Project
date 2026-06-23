def generate_regex(analysis):

    if analysis.get("type") == "digits":
        return "[0-9]+"

    if analysis.get("type") == "alphabets":
        return "[a-zA-Z]+"

    if analysis.get("type") == "binary":
        return "[01]+"

    if analysis.get("type") == "email":
        return r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    if analysis.get("type") == "phone":
        return r"^[0-9]{10}$"

    if analysis.get("type") == "url":
        return r"^(https?|ftp)://[^\s]+$"

    if "substring" in analysis:

        sub = analysis["substring"]

        return f".*{sub}.*"

    if "start" in analysis:

        start = analysis["start"]

        return f"^{start}.*"

    if "end" in analysis:

        end = analysis["end"]

        return f".*{end}$"

    return "Pattern not supported"