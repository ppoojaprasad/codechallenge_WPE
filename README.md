# codechallenge_WPE
Web Performance Engineering Code Challenge

The goal of this challenge is to measure your ability to perform different programming tasks. Please feel free to use any resources at your disposal to answer the questions. However, we do not permit any of the following:
●	Assistance from another person
●	Copying code or responses

Please create a public repository in Github to submit this code challenge. (OPTIONAL) Use virtualenv for development. If so, please include the requirements.txt file associated to your scripts

1.	Use Python to obtain and analyze data from the https://www.wunderground.com/weather/api API. Note that you would need to create a free account to obtain a key to call the API. 
a.	Get the tidal data available for the city of Santa Monica, CA
b.	Report the following information:
■	Name of the geographic site that the data is associated with
■	For each type of tide, show the maximum, minimum, average and median of the tide height, and the times at which they occurred (excluding the aggregates, of course)
■	The median of the time at which sunrise, sunset, moonrise and moonset occurred.
c.	Make necessary changes to your code to allow the type of “features” as a generic input parameter to your script (e.g. alerts, astronomy, hourly, hourly10day, tide, yesterday). For more info on the allowed features by the API, refer to: https://www.wunderground.com/weather/api/d/docs?d=data/index
■	Print an appropriate error messages if the input is invalid
■	Handle errors accordingly if the API is not available or not working
■	Note that the output of the API is different for each input parameter. 
1.	If hourly is passed as a parameter, report the average temperature
2.	If tide is passed as a parameter, report the tide statistics as calculated in part (b) above
3.	If any other valid parameter is passed, after successfully fetching the corresponding data from the API, print the message:
	“Data for <parameter> was successfully obtained”
(OPTIONAL): If you have experience with the unittest module, write unit tests for your code.  Please document your unit tests to make it clear what you are testing and why.


2.	You are given a range of IP addresses (e.g., 192.168.1.0/24). Assume you are going to use such range for a simple network scanning tool. In addition, you are given a set of IP address from that range that should not be scanned. 
a.	Use Python to write a script that takes a list of IPs to be used in the scanning tool.
■	Inputs: IP address range and the set of addresses to be excluded
■	Output: List of IP addresses to be scanned (range - excluded ip list)
■	Use netaddr module
■	Print appropriate error messages to handle invalid inputs
■	Print an error message if the list of excluded IPs is equal to the IP range

(OPTIONAL): If you have experience with the unittest module, write unit tests for your code.  Please document your unit tests to make it clear what you are testing and why.


Suggested Reference Material:

●	https://git-scm.com/ -- a cohesive public reference for Git
●	https://pypi.python.org/pypi -- The Python Packaging Index for obtaining modules that do not ship with Python
