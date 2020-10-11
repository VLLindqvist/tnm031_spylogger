import websocket
import time
import sys
import pynput
from pynput.keyboard import Key, Listener

def on_message(ws, message):
    print(message)

def on_error(ws, error):
    print(error)

def on_close(ws):
    print("### Connection closed ###\n")

def on_open(ws):
    def on_press(key):
        # print("{0} pressed".format(key))
        try:
            k = key.char  # single-char keys
        except:
            k = key.name  # other keys

        ws.send(k)

    def on_release(key):
        # DEBUG (in order to end the program in development)
        if key == Key.esc:
            ws.close()

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()


address = "localhost"
port = "3000"
websocket.enableTrace(True)
ws = websocket.WebSocketApp("ws://" + address + ":" + port + "/",
                                on_message = on_message,
                                on_error = on_error,
                                on_close = on_close)
ws.on_open = on_open
ws.run_forever()