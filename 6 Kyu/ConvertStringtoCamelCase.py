# Convert dash/underscore delimited word into camel case
def to_camel_case(text):
    # Edge case if text is empty
    if len(text) == 0:
        return text
    return text[0]+text.title()[1:].replace("-", "").replace("_", "")