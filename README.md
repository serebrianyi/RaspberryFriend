# About
RaspberryFriend started purely as a home security system but after a while it became my main interface of communication with raspberry pi completely removing any need to log in into the system. Right now it supports multiple commands that I use on a daily basis. 

# Features
* Mobile integration over any xmpp communicator
* Security system based on motion detection, activated only in case no mobile is in wifi
* Photo + video capibility using e-mail
* Get the list of prefered stock quotes
* Easily extendable with custom commands 

# How it works
1. Install RaspberryFried (check the installation section)
2. Install any xmpp client on your mobile (I'm using yaxim, works very nicely)
3. Tell your raspberry pi what to do!

# List of supported commands
* Status - just a smoke test to see if the connection is fine
* Dlna - restarts the dlna media server
* Photo - makes a photo and sends it to the mail specified in the config file
* Video - makes a video and sends it to the mail specified in the config file. Optional this command supports an integer parameter to define length of the video in seconds
* Temp - returns current temperature and humidity
* Quotes - gets the list of quotes for stocks specified in config file (uses yahoo finance)
* Tram - tells you when to leave your home to catch the bus to work using google maps (if you don't want to waste your time on the bus stop and don't remember the bus schedule by heart)

# Security as main functionality
Motion detection will be turned on automatically when your mobile (or mobiles, you can specify as many ip addresses as you want) leaves wifi. In that case every movement registered by motion detector will cause raspberry pi to make a photo and send it to you per e-mail. The motion detection will be automatically turned off when any of the ip addresses will become reachable again (i.e. you are at home).

# Features not implemented (yet)
* Voice recording for the video
* Support for speakers as a really noisy alarm sound
* Option to force the alarm to go on/off via command
* Master/Slave support for multiple raspberry pi's
* Option tos witch static ip addresses to mac addresses in case you don't want to define static ip's for your mobiles

# Installation
* Clone the repository to your raspberry pi
* Install all the dependencies: nose (unit testing framework), mock (python mocking library), requests (http library) and sleekxmpp (xmpp library)                                
--* ```pip install nose mock requests sleekxmpp```
* Follow the instructions from https://github.com/adafruit/Adafruit_Python_DHT to install the python library to read the DHT series of humidity and temperature sensors
* Set the correct path for your log file in domain_services/logging_service/logging.conf
* Set the values in the config files in configuration/files:
	* pir - config for motion detector (like this [one](http://www.adafruit.com/products/189))
	* mail - config for e-mail account from where raspberry pi will send the mails and setup of the recipient list
	* quote - list of the stock symbols used by http://finance.yahoo.com/
	* temp - config for DHT sensor (like this [one](http://www.adafruit.com/products/393))
	* tram - specifies your home address and working address (supports multiple working address that will be distinguished by the sender id)
	* ip - list of ip addresses to check 
	* xmpp - config for the xmpp communication
* Run the tests:
	* For unit tests go to tests folder and run nosetests-2.7 --exe
	* For integration tests go to tests_integration folder and run nosetests-2.7 --exe
