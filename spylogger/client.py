import websocket
# import thread
import time
import sys


port = "3000"
# port = int(sys.argv[1])


def on_message(ws, message):
    pass

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### Connection closed ###\n")

def on_open(ws):
    while True:
        time.sleep(5)
        ws.send("Hello")
    time.sleep(1)
    ws.close()

if __name__ == "__main__":
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:" + port + "/",
                              on_message = on_message,
                              on_error = on_error,
                              on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()