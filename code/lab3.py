import socket
import thingspeak

# The HC-06 Address
bluetooth_addr = "Our Address"
bluetooth_port = 1 #RFCOMM channel 1

#Thingspeak Information
channel_ID = 2913073 #channel ID from thingspeak
key = "S0RJOAXCWG559TA9" #thingspeak API Key
url = 'https://api.thingspeak.com/update'  #default url to update the thingspeak server

#Init. thingspeak channel
ts = thingspeak.Channel(channel_ID, key, url)

#Create a bluetooth socket
bluetooth_socket = socket.socket(socket.AF_BLUETOOTH, socket.SOCK_STREAM, socket.BTPROTO_RFCOMM)
bluetooth_socket.connect((bluetooth_addr,bluetooth_port))


try:
  while True:
    recieved_data = bluetooth_socket.recv(1)
    temperature = int.from_bytes(recieved_data, byteorder='big')
    print("Current Temperature: %d" % temperaure)


    thingspeak_field1 = {"field1": temperature}
    ts.update(thingspeak_field1) #update Thingspeak

except KeyboardInterrupt:
    print ("ERRROR; Keyboard interrupt detected: Shutting down")

except Exception as e:
    print (f"ERROR: {e}" )
    
    
finally:
  bluetooth_socket.close()


