from socket import *
from sys import stdout
from time import time

#CONSTANTS#
DEBUG = False
# we only use one for determining the 1 or 0, but both are defined for funzies.
# 0.06 seemed like the most effective midpoint to measure off of.
ONE = 0.06
ZERO = 0.025

# Variable declarations for the rest of the code.
# bitString and returnString are used for the binary and the decoded message respectively.
ip = "138.47.99.64"
#ip = "localhost"
port = 31337
bitString = ""
returnString = ""
# i is just used to track how many times the while loop at the bottom has run
i = 0

# This sets up the socket for the server and then connects to it using the ip and port provided.
# Next, it begins receiving data from the server.
s = socket(AF_INET, SOCK_STREAM)
s.connect((ip, port))
data = s.recv(4096).decode()


# precurser message to show that the server was connected to.
print("[connect to the chat server]\n")
print("...\n")

# while loop for running through the data being recieved from the chat server.
# We want to run until the message received is "EOF"
while (data.rstrip("\n") != "EOF"):

    # Write the data to stdout (less delay than print())
    stdout.write(data)
    stdout.flush()

    # measure the amount of time between the last message being written and the next message being received
    t0 = time()
    data = s.recv(4096).decode()
    t1 = time()

    # calculate the total delay (to three decimal places)
    delta = round(t1 - t0, 3)

    # Here, we check to see if the delay is greater than our midpoint
    # If it is, we add a "1" to the bit string, otherwise we add a "0"
    if(delta >= ONE):
        bitString += "1"
    else:
        bitString += "0"

    # If debug is set true, we want to print out the delays for each little bit of the message.
    if (DEBUG):
        stdout.write(f"{delta}\n")

#finally, we disconnect from the server
s.close

# message to show that the server was disconnected.
print("...\n")
print("[disconnect from the chat server]")

# looping through the built bit string 8 bits at a time in order to build a plain text message.
# I think it is important to note that we could've clipped the EOF off of the end of the covert message
# but I didn't think it was all to necessary since not all covert messages are guaranteed to end with EOF
while(i <= (len(bitString) - 8)):

    # adding a character to the return string by converting one byte of data to a char with ascii.
    returnString += chr(int(bitString[i:i+8], 2))
    i += 8

# finally, printing the return string.
stdout.write(returnString)