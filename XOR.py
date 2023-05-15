import sys

if __name__ == '__main__':
    # get message from stdin
    message = sys.stdin.buffer.read()
    # get key from reserved key file
    with open('k3y', 'rb') as k:
        key = k.read()
    # get xored message
    xored = bytearray()
    for i in range(len(message)):
        xored.append(message[i] ^ key[i])
    # print xored message
    sys.stdout.buffer.write(xored)