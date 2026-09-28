
def format_text(text: str) -> str:
    """
    Format the given text by removing extra spaces and converting to lowercase,
    except for text inside single quotes.

    Args:
        text (str): The text to format.

    Returns:
        str: The formatted text.
    """
    # remove multiple spaces, new lines and tabs
    text = remove_extra_spaces(text)
    # lower case without damaging business rules
    text = lower_case(text)
    return text

def lower_case(text: str) -> str:
    """
    Convert the given text to lowercase, except for text inside single quotes.

    Args:
        text (str): The text to convert.

    Returns:
        str: The text converted to lowercase, except for text inside single quotes.
    """
    parts = text.split("'")
    
    # Process each part, skipping the parts inside simple quotes because range(..,..,2)
    for i in range(0, len(parts), 2):
        parts[i] = parts[i].lower()
    
    # Join the parts back together with single quotes
    return "'".join(parts)

def remove_extra_spaces(text: str) -> str:
    """
    Remove extra spaces from the given text.

    Args:
        text (str): The text to process.

    Returns:
        str: The text with extra spaces removed.
    """
    import re as regex

    #text = text.replace("\n", " ")
    #return regex.sub(r' {2,}', ' ', text).strip()
    return " ".join(text.split())