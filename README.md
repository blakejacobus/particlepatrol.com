_Credit should first be given to the appropriate source - federal, state, local, and tribal air quality agencies and the EPA AirNow program - in products, publications, presentations, or any other related distribution. These federal, state, local, and tribal air quality agencies are the owners of the data and the authorities for the data. A list of state/local/tribal agencies can be found at http://www.airnow.gov/index.cfm?action=airnow.partnerslist._

# Particle Patrol
Air quality index (AQI) aggregation for specific Arizona areas of interest. Source: https://docs.airnowapi.org/

The [AirNow API](https://docs.airnowapi.org/) is open to all with an account. You can reset your website password or retrieve your API key via the Log In page. Your API key is also automatically included in example URLs when using the Query Tool. The [Web Services](https://docs.airnowapi.org/webservices) endpoint is used to generate queries in the UI, which can be translated to API requests.

## Objectives

- [ ] Integrate AWS CLI solution for API key retrieval (currently in `archive/`) into `/src/request.py`
- [ ] Use Python, AWS CLI, and the AirNow API to poll and parse air quality data for specific zip codes
- [ ] Present data in a web page (`particlepatrol.com`)
- [ ] Include test cases for all functions
- [ ] Include error/exception handling for input, request, and display functionality

## Reference
- [Historical Observations](https://docs.airnowapi.org/HistoricalObservationsByZip/docs)
- [File Products](files.airnowtech.org)
  - [Hourly Data Fact Sheet](https://docs.airnowapi.org/docs/HourlyDataFactSheet.pdf)
  - [Daily Data Fact Sheet](https://docs.airnowapi.org/docs/DailyDataFactSheet.pdf)
- [Current Observations](https://docs.airnowapi.org/CurrentObservationsByZip/docs)

### Sample Request
| method | endpoint | headers | auth |
| ------ | -------- | ------- | ---- |
| GET | historical: https://www.airnowapi.org/aq/observation/zipCode/historical/ <br> current: https://www.airnowapi.org/aq/observation/zipCode/current/ | ?format=application/json&zipCode=12345&date=YYYY-MM-DDT00-0000&distance=25 | &API_KEY={REDACTED} |

### Sample Response

## Sample Output

``` bash
[
    {
        'DateIssue': '2024-07-26', 
        'DateForecast': '2024-07-26', 
        'ReportingArea': 'Decatur', 
        'StateCode': 'IL', 
        'Latitude': 39.8529, 
        'Longitude': -88.9369, 
        'ParameterName': 'O3', 
        'AQI': -1, 
        'Category': 
            {
                'Number': 1, 
                'Name': 'Good'
                }, 
        'ActionDay': False, 
        'Discussion': ''
        },
]
AQI in Decatur on 2024-07-26 is: -1
AQI is reportedly less than 0
Consider validating: https://www.airnow.gov/
```