# Weather_Channel_Bluemix_API

###  Some samples of how to use the API to get the weather data.

Register at console.ng.bluemix.net

https://console.ng.bluemix.net/services/ef6374e6-aa2f-46f7-88e2-a09795e1d57d?paneId=manage


https://www.ng.bluemix.net/docs/services/Weather/index-gentopic1.html#weather_sample1

a Typical Rest Curl command would look like :

/v1/geocode/12.97/77.59/forecast/daily/3day.json

Where the 12.97 and 77.59 is the Latitude and Longitude of location Bangalore and today's date is 29 December
as seen in "fcst" report shown below. 

To start with : run the getthreedaydata.sh, and it returns the output in a file called data.json
This data.json is the JSON response and contains a load of valid information for forecast for the next 3 days.

Has several key value pairs like max_temp, min_temp, Lunar(to say if it is a New Moon or not )

This file has to be parsed in Python to get the results for 3 day temperature details.
Run as python parsedata.py


<img width="733" src="https://cloud.githubusercontent.com/assets/14288989/21538298/88037820-cdc1-11e6-8652-649e818e5fd7.png">

<img width="756" src="https://cloud.githubusercontent.com/assets/14288989/21538310/b9903a04-cdc1-11e6-968b-07a29b7c1534.png">

