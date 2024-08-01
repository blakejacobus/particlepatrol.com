"""Collect user input and return it as an API call header

Generate input prompt and then format response and return in format
expected by https://docs.airnowapi.org/webservices
"""

# TODO - raise exception if zip not correct value


def input_zip(input):
    """Take user input and concatenate zip code header for API call."""
    while True:
        try:
            input = int(input("Enter zip code: "))
            break
        except ValueError:
            print("A number is required. Please try again.")
    zip = f"zipCode={input}"
    return zip
