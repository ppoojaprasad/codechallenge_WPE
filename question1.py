from urllib.request import urlopen
from urllib.error import URLError,HTTPError
import json
import statistics
import numpy
import sys

# Function to call when hourly feature is requested
def hourly():
    json_string = f.read().decode('utf8')
    parsed_json = json.loads(json_string)
    temp= parsed_json['hourly_forecast']
    num1=0
    fah=[]
    cel=[]
    for each in temp:
        num1=num1+1
    print(num1)
    for i in range(num1):
        fah.append(int(temp[i]["temp"]["english"]))
        cel.append(int(temp[i]["temp"]["metric"]))
    print("The average temp in fahrenheit",numpy.mean(fah))
    print("The average temp in celsius",numpy.mean(cel))

# Function to call when tide feature is requested    
def tide():

    print("welcome to Tide statistics")
    json_string = f.read().decode('utf8')
    parsed_json = json.loads(json_string)
    geo_site = parsed_json['tide']['tideInfo'][0]['tideSite']
    sum_list = parsed_json['tide']['tideSummary']
    num = 0
    for i in sum_list:
        num += 1
    list_of_tides=[]
    dict_of_tide_height={}
    dict_of_tide_dates={}

    # traversing through the nested dictionary response
    for each in sum_list:
        list_of_values = []
        list_of_dates=[]
        type_of_tide=each.get('data').get('type')
        if type_of_tide not in list_of_tides:
            list_of_tides.append(type_of_tide)
            if each.get('data').get('height'):
                list_of_values.append(each.get('data').get('height'))

            else:
                list_of_values.append('0 ft')
            list_of_dates.append(each.get('date').get('pretty'))
            dict_of_tide_height[type_of_tide]=list_of_values
            dict_of_tide_dates[type_of_tide]=list_of_dates
        else:

            temp_list_height=dict_of_tide_height[type_of_tide]
            temp_list_dates=dict_of_tide_dates[type_of_tide]


            if each.get('data').get('height'):
                temp_list_height.append(each.get('data').get('height'))

            else:
                temp_list_height.append('0 ft')

            temp_list_dates.append(each.get('date').get('pretty'))
            dict_of_tide_height[type_of_tide] = temp_list_height
            dict_of_tide_dates[type_of_tide] = temp_list_dates

    for key, value in dict_of_tide_height.items():
        print("\n===============================================================")

        print(" Type of tide is ",key)
        print ("max is ",max(value))
        max_index=value.index(max(value))
        print("min is ",min(value))

        min_index=value.index(min(value))
        list_val=[]
        val=[]
        for each_element in value:
            val=each_element.split()
            list_val.append(float(val[0]))

        print("avg is", numpy.mean(list_val))
        print("median is",statistics.median(list_val))
        date_list=dict_of_tide_dates[key]
        print("date at which max tide occurred is ",date_list[max_index])
        print("date at which min tide occurred is ", date_list[min_index])



# URL parameters
key = "77e3ad2ef8d36229"
query="CA/Santa_Monica"
list_of_features=['alerts','almanac','astronomy','conditions','currenthurricane','forecast','forecast10day','geolookup','history','hourly', 'hourly10day','planner','rawtide','tide','webcams','yesterday']
# Getting user input
print("Enter one of the feature in the following list:")
for i in list_of_features:
    print(i)
feature=input()
url='http://api.wunderground.com/api/%s/%s/q/%s.json'%(key,feature,query)
# Error handling for invalid API call
try:
    f = urlopen(url)
except HTTPError as e:
    print('Error code: ', e.code)
    sys.exit()
except URLError as e:
    print('Reason: ', e.reason)
    sys.exit()
else: 
    print("The input given by the user is %s"%feature)
    # Error handling for Invalid user input
    if feature.lower() not in list_of_features:
        print("Invalid Input: Feature not found for this api")
        sys.exit()
    elif feature.lower()=="tide":
        # Tide statistics
        tide()
    elif feature.lower()=="hourly":
        # Hourly statistics
        hourly()
    else:
        json_string = f.read().decode('utf8')
        parsed_json = json.loads(json_string)
    print("Data for " +feature + " was successfully obtained")
