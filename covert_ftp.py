import os
import ftplib
import sys

IP_ADDR = "138.47.99.64"
PORT = 21
DIRECTORY = ""
# 1 is 7 bit, 2 is 10 bit
METHOD = 1
PATH = "/7"

def get_permissions(server, PATH):
    # change stdout to auxiliary file
    aux_file = open("aux.txt", "w+")
    sys.stdout = aux_file
    # print directory info to stdout
    server.dir(PATH)
    # reset stdout
    sys.stdout = sys.__stdout__
    # reset file pointer for reading
    aux_file.seek(0)
    # get file permissions
    permissions = []
    lines = aux_file.readlines()
    for line in lines:
        permissions.append(line[:10])
    # close and delete file
    aux_file.close()
    os.remove("aux.txt")

    return permissions

def permissions_to_binary(permissions):
    '''
    convert permissions from linux-format to binary-format
    '''
    binary_permissions = []
    for p in permissions:
        binary = ""
        for i in range(len(p)):
            if p[i] == "-":
                binary += "0"
            else:
                binary += "1"
        binary_permissions.append(binary)

    return binary_permissions

def decode(binary_permissions, METHOD):
    '''
    decode binary to ascii
    '''
    decoded = []
    if METHOD == 1:
        for perm in binary_permissions:
            if perm[:3] == "000":
                decoded.append(chr(int(perm[3:],2)))
    else:
        concatted = ''.join(binary_permissions)
        refactored = [concatted[i:i+7] for i in range(0,len(concatted), 7)]
        for perm in refactored:
            if len(perm) == 7:
                decoded.append(chr(int(perm,2)))

    return decoded

if __name__ == '__main__':
    # Create server object
    server = ftplib.FTP()

    # Connect to server
    server.connect(IP_ADDR, PORT)

    # Login to anonymous server
    server.login("anonymous", "")
    
    # get file permissions
    permissions = get_permissions(server, PATH)

    # change file permissions to binary
    binary_permissions = permissions_to_binary(permissions)

    # decode according to METHOD
    decoded = decode(binary_permissions, METHOD)

    # display the decoded message
    print(''.join(decoded))
