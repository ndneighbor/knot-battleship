import socket
import sys
import logging

# Logger Block

logger = logging.getLogger('myapp')
hdlr = logging.FileHandler('/var/tmp/myapp.log')
formatter = logging.Formatter('%(asctime)s %(levelname)s %(message)s')
hdlr.setFormatter(formatter)
logger.addHandler(hdlr) 
logger.setLevel(logging.WARNING)

class Client:
    def __init__(self):
        self.isClientConnected = False

    def connect(self, host='', port=50000):
        try:
            self.clientSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            self.clientSocket.connect((host, port))
            self.isClientConnected = True
        except socket.error as errorMessage:
            if errorMessage.errno == socket.error.errno:
                sys.stderr.write('Connection refused to ' + str(host) + ' on port ' + str(port))
            else:
                sys.stderr.write('Failed to create a client socket: Error - %s\n', errorMessage)

    def disconnect(self):
        if self.isClientConnected:
            self.clientSocket.close()
            self.isClientConnected = False

    def send(self, data):
        if not self.isClientConnected:
            return

        self.clientSocket.send(data.encode('utf8'))

    def send_all(self, data):
        if not self.isClientConnected:
            return

        self.clientSocket.send(data.encode('utf8'))

    def receive(self, size=4096):
        if not self.isClientConnected:
            return ""

        return self.clientSocket.recv(size).decode('utf8')

    def setup_logs(self, filename):
        try:
            x = open(filename, "r")
            pass
        except FileNotFoundError:
            print("No log file found, making one")
            pass

    def log(self, data, log):
        try:
            x = open(log, "r")
            pass
        except FileNotFoundError:
            print("Logs should have been setup")
            pass
        if (log == log):
            open(log, "w")

    def save_to_quick(self):
        print("Save the connect to a txt")

    def make_team(self):
        print("Fires off message to make a chat room")