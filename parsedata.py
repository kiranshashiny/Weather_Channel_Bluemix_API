import json
import itertools
from pprint import pprint
from itertools import izip


#!/bin/bash
#

#curl -o data.json somefile -k https://ef5128a4-86b4-47b8-b14f-a0cd74abf0ef:MwN42ReQZ9@twcservice.mybluemix.net:443/api/weather/v1/geocode/45.42/75.69/forecast/daily/3day.json

#Returns a JSON blob containing "metadata" - which is a dictionary and a "forecast" - which is a list

# The list in the JSON could have multiple dictionaries.


with open('data.json') as data_file:    
    data = json.load(data_file)

#pprint(data)
#print data["metadata"]["language"]
#print data["metadata"][0].encode("utf-8")
#print type(data)

for key, value in data.iteritems():
    print "Key = [" + key + "]"
    print type(value)
    #mystring = str (value)
    #print  "value = ["+ mystring.encode("utf-8") + "shashi]"

    # The value can  be either a dictionary or a list
    # I have to check what is it and then do appropriate.

    # process the "metadata" which is in dictionary format.

    if  type(value) == type(dict()):
        print "key = [" + key + "] this is a dict"
        for k, v in value.iteritems():
            print k, v

    # process the forecast, which is a list but inside it has multiple dicionaries.

    if type(value ) == type(list()):
        print " Key = [" + key + "]" + "******  Value is a list"
        
        #print value[4]
        print len(value)
        for p in value:
            #print p  # careful - this prints a blob - so commented it.
            print "****************"
           
            for k, v in p.iteritems():
                if ( k == "max_temp" or  k == "min_temp" or k == "narrative"\
                 or k == "dow" or k == "lunar_phase" or k == "fcst_valid"):
                    map2 = str(v)
                    print " key = [" + k + "]" + "  value = ["+ map2 + "]" 
