# Creating the server to have LAN connection between 2 computers

import socket
from threading import Thread

message = []

def ultMsgCompare(msgs: list[str]):
    ultMSG = ""
    for msg in msgs:
        if msg not in ultMSG:
            return False
    return True


class Server:
    Clients = []  ##static, this has the 3 people connected to "192.168.56.1"

    def __init__(self, HOST, PORT):
        self.socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)  ## create the socket
        self.socket.bind((HOST, PORT))
        self.socket.listen(5)    ## 5 connections
        print("Server waiting for connection...")


    def listen(self):
        while True:
            client_socket, address = self.socket.accept() 
            print("Connection from: " + str(address))

            #the first message will be the username
            client_name = client_socket.recv(1024).decode()
            client = {'client_name': client_name, 'client_socket': client_socket}

            ## broadcast that the new client has connected
            self.broadcast_message(client_name, client_name + " has successfully entered Virtual HQ ")

            Server.Clients.append(client) ## appends to the list
            Thread(target = self.handle_new_client, args = (client,)).start()  ## a different thread for each client

    def handle_new_client(self, client):
        client_name = client['client_name']
        client_socket  = client['client_socket']
        count = 0
        msgs = []
        while True:
            ##listen for message and broadcast message to all clients
            client_message = client_socket.recv(1024).decode()
            msgs.append(client_message)
            count +=1
            with open("msg.txt", "a") as msgFile:
                        msgFile.write(client_message)
            if(count == 3):
                if(ultMsgCompare(msgs)):
                    #broadcast successful launch
                    self.broadcast_message("NUKE LAUNCHED! LEGS GO NUCLEAR!")
                else:
                    msgs = []
                

            ## take the three hashcode messages and print Acces Granted

            if client_message.strip() == client_name + ": bye" or not client_message.strip():
                self.broadcast_message(client_name, client_name + "has left the interface!")
                Server.Clients.remove(client)
                client_socket.close()
                break


            else:
                
                self.broadcast_message(client_name, client_message)

                ## loop through the list of clients and check that each person has entered a hashcode
                for client in self.Clients:
                    client_socket = client['client_socket']
                    client_name = client['client_name']
                    message.append(client_message)
                    
                    print("Message Stored (server output)") 

                    if len(message) ==3:
                        "TODO"
                    ##self.broadcast("Message Stored (client output)")
                    
                



    def broadcast_message(self, sender_name, message):
        for client in self.Clients:
            client_socket = client['client_socket']
            client_name = client['client_name']
            if client_name != sender_name:
                client_socket.send(message.encode()) ##encoding in bytes before sending
        


if __name__ == '__main__':
    server = Server('127.0.0.1', 7632)  ## 127.0.0.1 is loopback and the same for everyone
    server.listen()

print("file running")
