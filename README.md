# Weather_Channel_Bluemix_API

###  Retrieving weather data from the Weather channel using Bluemix.

<img width="989" src="https://cloud.githubusercontent.com/assets/14288989/21560000/3f7f0e5e-ce7d-11e6-99ee-dcb67d870223.png">


http://www.usatoday.com/story/tech/2015/03/31/ibm-weather-channel-cloud-collaboration/70682492/?cm_mc_uid=37247814973514823030142&cm_mc_sid_50200000=1483074785

This API lets you get current and forecast weather data from the Weather channel and use it for our business.

One would login to the Bluemix - get a set of credentials and then using some of the common API - get the data back in JSON format and use it for applications.

In this repository I have one such sample that will give you an insight on how to request for a three day data and examine the result in JSON format.

To start with:

Register or Login to console.ng.bluemix.net

click on Create Service

<img width="1249" alt="screen shot 2016-12-30 at 10 51 06 am" src="https://cloud.githubusercontent.com/assets/14288989/21560035/e3ff1a32-ce7d-11e6-8ebc-2cdb789fde0e.png">

Search for the Weather Company Data

<img width="574" alt="screen shot 2016-12-30 at 10 52 01 am" src="https://cloud.githubusercontent.com/assets/14288989/21560046/0d9e15e6-ce7e-11e6-8e26-6a4992814d47.png">

Create the service with the default credentials 
<img width="884" alt="screen shot 2016-12-30 at 10 54 04 am" src="https://cloud.githubusercontent.com/assets/14288989/21560065/64b84720-ce7e-11e6-8682-90ee28abc124.png">

Once the service is created: Click on Service Credentials and view it, keep this data aside as we would need it for querying data.

<img width="1118" alt="screen shot 2016-12-30 at 10 56 22 am" src="https://cloud.githubusercontent.com/assets/14288989/21560078/a238d7e0-ce7e-11e6-8f1f-d2f4c54bf478.png">


now, a sample of what we would like to see and how to get that data.

https://www.ng.bluemix.net/docs/services/Weather/index-gentopic1.html#weather_sample1

A Typical Rest Curl API command to get 3 day data would look like :

/v1/geocode/12.97/77.59/forecast/daily/3day.json

Where the 12.97 and 77.59 is the Latitude and Longitude of location Bangalore and today's date is 29 December
as seen in "fcst" report shown below. 

For more information or tutorials or samples on the APIs -look up this URL.

https://twcservice.mybluemix.net/rest-api/

<img width="1019" alt="screen shot 2016-12-30 at 10 58 58 am" src="https://cloud.githubusercontent.com/assets/14288989/21560099/ff730b7e-ce7e-11e6-829a-57a240381971.png">



To start with my samples : run the getthreedaydata.sh in this repository, and it returns the output in a file called data.json

This data.json results file is the JSON response in text format and contains a load of valid information for forecast for the next 3 days.

Has several key value pairs like max_temp, min_temp, Lunar(to say if it is a New Moon or not )

This file has to be parsed in Python to get the results for 3 day temperature details.

Run the script:

 $python parsedata.py

Here you will see that I have printed a small subset of data that I was able to parse from the JSON results.
You will see today was a Full Moon day, max temperature, minimum temperature, date ( in epoch -that has to converted to human readable format later ) and some narrative about the day's weather.


<img width="733" src="https://cloud.githubusercontent.com/assets/14288989/21538298/88037820-cdc1-11e6-8652-649e818e5fd7.png">

This data is just a sample of how the IBM's Weather company data relates to what is seen on the Google's Weather forecast and you will notice they are somewhat similar in terms of temperature and other data.

<img width="756" src="https://cloud.githubusercontent.com/assets/14288989/21538310/b9903a04-cdc1-11e6-968b-07a29b7c1534.png">
