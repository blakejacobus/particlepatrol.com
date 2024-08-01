"""Main function to aggregate function calls

This module calls out to the source modules to collect input, submit
API request, and display the data returned.
"""

from src.request import request
from src.display import display
from src.input import input_zip


def main():
    zip = input_zip(input)  # Requests user input for zip code
    output = request(zip)  # Outputs API call response in JSON format
    display(output)  # Parses API response and returns air quality data


if __name__ == "__main__":
    main()
