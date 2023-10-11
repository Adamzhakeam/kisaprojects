def is_reserved_character(char):
    # Check if a character is a reserved character
    reserved_characters = [":", "/", "?", "&", "=", "+", "#", " ",]
    return char in reserved_characters

def is_percent_encoded(char):
    print(char)
    reserved_characters = [":", "/", "?", "&", "=", "+", "#", " ",]
    # Check if a character is properly percent-encoded
    if char.startswith("%"):
        try:
            # Attempt to decode the percent-encoded character
            decoded_char = bytes.fromhex(char[1:]).decode("utf-8")
            return decoded_char in reserved_characters
        except ValueError:
            pass
    return False

def validate_query_parameters(query):
    # Validate query parameters
    query_params = query.split("&")
    for param in query_params:
        key_value = param.split("=")
        if len(key_value) != 2:
            return False  # Invalid parameter format

        key, value = key_value
        if not all(is_reserved_character(char) or char.isalnum() for char in key):
            return False  # Invalid parameter name
        if not all(is_reserved_character(char) or is_percent_encoded(char) for char in value):
            return False  # Invalid parameter value

    return True

def validate_fragment_identifier(fragment):
    # Validate fragment identifier
    return all(is_reserved_character(char) or char.isalnum() for char in fragment)

def validate_url(url):
    # Split the URL into components
    parts = url.split("#", 1)
    if len(parts) > 1:
        fragment = parts[1]
        if not validate_fragment_identifier(fragment):
            return False  # Invalid fragment identifier

    components = parts[0].split("?", 1)
    if len(components) > 1:
        query = components[1]
        if not validate_query_parameters(query):
            return False  # Invalid query parameters

    return True

# Test cases
url1 = "https://example.com/path/to/resource?param=value&name=John%20Doe#section3"
url2 = "https://example.com?param1=1&param2=2&param2=3"
url3 = "https://example.com/file%2Ffolder"

print(f"URL 1 Valid: {validate_url(url1)}")
print(f"URL 2 Valid: {validate_url(url2)}")
print(f"URL 3 Valid: {validate_url(url3)}")
