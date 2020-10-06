from SimpleWebSocketServer import SimpleWebSocketServer, WebSocket

import sys

port = 3001
# port = int(sys.argv[1])

class SocketServer(WebSocket):

    def handleMessage(self):
        # echo message back to client
        print(self.data)
        self.sendMessage(self.data)

    def handleConnected(self):
        print(self.address, 'connected')

    def handleClose(self):
        print(self.address, 'closed')

server = SimpleWebSocketServer('', port, SocketServer)
server.serveforever()