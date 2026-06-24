def generate_test_cases(pattern_type):

    valid = []
    invalid = []

    if pattern_type == "digits":
        valid = ["123", "4567", "99999"]
        invalid = ["abc", "12ab", "@123"]

    elif pattern_type == "alphabets":
        valid = ["hello", "Regex", "Python"]
        invalid = ["123", "abc123", "@test"]

    elif pattern_type == "uppercase":
        valid = ["HELLO", "WORLD"]
        invalid = ["Hello", "hello", "123"]

    elif pattern_type == "lowercase":
        valid = ["hello", "regex"]
        invalid = ["HELLO", "Hello", "123"]

    elif pattern_type == "binary":
        valid = ["0", "1", "10101"]
        invalid = ["2", "102", "abc"]

    elif pattern_type == "phone":
        valid = ["9876543210"]
        invalid = ["98765", "abc123", "12345678901"]

    elif pattern_type == "email":
        valid = ["test@gmail.com"]
        invalid = ["test@", "@gmail.com", "abc"]

    return valid, invalid