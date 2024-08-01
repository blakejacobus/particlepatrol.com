""" Parse and display API responses based on input

Take the output of API request and parse it, returning basic air quality
and pollution risk metrics from https://www.airnow.gov/aqi/aqi-basics/
"""

# TODO - raise exception if value is less than 0


def display(output):  # Output is returned as list
    # Data parsing/indexing
    entry = output[0]  # Index of list is dictionary; 0 is latest entry
    aqi = entry["AQI"]
    date = entry["DateIssue"]
    area = entry["ReportingArea"]
    print(f"AQI in {area} on {date} is: {aqi}")
    # Output variables
    aq = "Air quality: "  # Air quality
    pr = "Pollution risk: "  # Pollution risk
    green = (
        f"{aq}GOOD\n" 
        f"{pr}LITTLE/NONE"
    )
    yellow = (
        f"{aq}MODERATE\n" 
        f"{pr}LOW (for those sensitive to pollutants)"
    )
    orange = (
        f"{aq}UNHEALTHY FOR SOME\n" 
        f"{pr}MODERATE (for those sensitive to pollutants)"
    )
    red = (
        f"{aq}UNHEALTHY FOR ALL\n" 
        f"{pr}MODERATE/SEVERE"
    )
    purple = (
        f"{aq}VERY UNHEALTHY\n" 
        f"{pr}HEALTH ALERT - INCREASED RISK FOR ALL"
    )
    maroon = (
        f"{aq}HAZARDOUS\n" 
        f"{pr}HEALTH WARNING - EMERGENCY CONDITIONS"
    )
    negative = (
        f"AQI is reportedly less than 0\n"
        f"Consider validating: https://www.airnow.gov/"
    )
    status = None
    if 0 < aqi <= 50:
        status = green
        print(status)
    elif 50 < aqi <= 100:
        status = yellow
        print(status)
    elif 100 < aqi <= 150:
        print(orange)
    elif 151 < aqi <= 200:
        print(red)
    elif 200 < aqi <= 300:
        print(purple)
    elif aqi > 300:
        print(maroon)
    else:
        print(negative)
    return status
