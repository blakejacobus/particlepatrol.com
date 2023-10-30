_Credit should first be given to the appropriate source - federal, state, local, and tribal air quality agencies and the EPA AirNow program - in products, publications, presentations, or any other related distribution. These federal, state, local, and tribal air quality agencies are the owners of the data and the authorities for the data. A list of state/local/tribal agencies can be found at http://www.airnow.gov/index.cfm?action=airnow.partnerslist._

# airizona
Air quality index (AQI) aggregation for specific Arizona areas of interest. Source: https://docs.airnowapi.org/

## Objectives
- [X] Use Python to issue API call that collects current data at specific location
- [ ] Use `boto3` to pull API key from AWS Secrets Manager
- [ ] Review and parse response to collect required information [https://docs.airnowapi.org/forecastsbyzip/docs]
- [ ] Expand API call to multiple locations
- [ ] Collect, parse, and store historical data (database may be needed)
- [ ] Create [database](https://docs.airnowapi.org/faq#:~:text=How%20can%20I%20maintain%20my%20own%20database%20of%20air%20quality%20data%3F) to cache records and limit API calls
- [ ] Develop front end presentation of database information

## Reference
- [Historical Observations](https://docs.airnowapi.org/HistoricalObservationsByZip/docs)
- [File Products](files.airnowtech.org)
  - [Hourly Data Fact Sheet](https://docs.airnowapi.org/docs/HourlyDataFactSheet.pdf)
  - [Daily Data Fact Sheet](https://docs.airnowapi.org/docs/DailyDataFactSheet.pdf)
- [Current Observations](https://docs.airnowapi.org/CurrentObservationsByZip/docs)

### Sample API Call
| method | endpoint | headers | auth |
| ------ | -------- | ------- | ---- |
| GET | historical: https://www.airnowapi.org/aq/observation/zipCode/historical/ <br> current: https://www.airnowapi.org/aq/observation/zipCode/current/ | ?format=application/json&zipCode=12345&date=YYYY-MM-DDT00-0000&distance=25 | &API_KEY={REDACTED} |