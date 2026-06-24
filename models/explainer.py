def explain_regex(regex):

    explanations = []

    if "^" in regex:
        explanations.append("^ : Start of string")

    if "[0-9]" in regex:
        explanations.append("[0-9] : Digits from 0 to 9")

    if "[a-zA-Z]" in regex:
        explanations.append("[a-zA-Z] : Uppercase and lowercase letters")

    if "[A-Z]" in regex:
        explanations.append("[A-Z] : Uppercase letters only")

    if "[a-z]" in regex:
        explanations.append("[a-z] : Lowercase letters only")

    if "+" in regex:
        explanations.append("+ : One or more occurrences")

    if "*" in regex:
        explanations.append("* : Zero or more occurrences")

    if "@" in regex:
        explanations.append("@ : Email separator")

    if "$" in regex:
        explanations.append("$ : End of string")

    return explanations