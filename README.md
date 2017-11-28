# ATLAS-Sem1-Project
CO2 data driven servo motor

-------------------------------------------------------------------------------------------------------------------------
Requirements
Hardware required:
1. Netatmo weather station ( or any compatible weather sensor modules)
2. Arduino ( Genuino Uno used)
3. Servo Motor ( SM-S2309S used)
4. LED ( Red 5V used)
5. MOSFET ( IRF520 used)
6. Two new 9V batteries or a DC Power Supply ( Power Supply E015 used)

Software required:
1. Arduino IDE
2. Python 2.x / 3.x (3.5 used)
3. Modules to be installed for python
    3.1 pyserial
    3.2 lnetatmo
4. Netatmo Web interface( Just to register and request Authentication)
--------------------------------------------------------------------------------------------------------------------------

Procedure:
I.Get data from Netatmo weather station with python API and library lnetatmo -https://github.com/philippelt/netatmo-api-python
  1.Set up Netatmo weather station device and account, register app and get authentication keys as such:
    a.Client ID
    b.Client Secret
  2.Download above lnetatmo github repo and follow the readme.
    2.1 Edit lnetatmo file as given in above readme
    2.2 Add auth credentials in the actual python file - refer serduino.py
    2.3 Request relevant data from netatmo - refer serduino.py or https://dev.netatmo.com/resources/technical/samplessdks/sdks
  3.Communicate with ( remember data is sent in bytes- refer serduino.py to get the idea)
    3.1 Send acquired data to arduino using pyserial
    3.2 Use logic and control the servo and/or fan motor as needed.
    3.3 return ack to pyserial from arduino
  4.Done?
