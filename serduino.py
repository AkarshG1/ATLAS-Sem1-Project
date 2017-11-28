import lnetatmo        # Netatmo library
from time import sleep # Not sure why
import serial          # Arduino 

#---------------------------------------------------------------------GET NETATMO DATA----------------------------------------------------------------------------
#Authenticate netatmo
authorization = lnetatmo.ClientAuth(
									
									clientId = "5a1d4ef32d3e041e648bb176",
									clientSecret = "uKQ4uoXxAfciFEvLzpjtkI3qp3r12jfozAiSeOqA6JJxI",
									username = "a.gopal@student.utwente.nl",
									password = "Netamo@123",
									scope = "read_station"
									)

#Get devices list
weatherData = lnetatmo.WeatherStationData(authorization)

#Access most fresh data directly

#---------------------------------------------------------------------------ARDUINO CODE--------------------------------------------------------------------------	 
	 
COM = 'COM3'	 																			#Change Value depending on Arduino Port

ser = serial.Serial(COM, 9600) 																# Establish the connection on a specific port
counter = 32 																				# Below 32 everything in ASCII is gibberish
while True:
	
	co2 = (weatherData.lastData()['Netatmo02']['CO2'])								#Collect CO2 reading from Netatmo					#
	print("Current CO2 reading(T100): %s ppm\t ,sending to Arduino..." %(co2))				#Print CO2 reading on console
	#counter +=1
	co2=co2//10
	char_co2 = chr(co2)																		#Convert Integer value to char
	ser.write(char_co2.encode()) # Convert the decimal number to ASCII then send it to the Arduino
	print (ser.readline()) # Read the newest output from the Arduino
	sleep(.1) # Delay for one tenth of a second
	#if counter == 255:
		#counter = 32
