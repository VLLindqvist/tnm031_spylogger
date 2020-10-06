import pynput
from pynput.keyboard import Key, Listener

class SocketClient:
    def __init__():
    websocket.enableTrace(True)
    ws = websocket.WebSocketApp("ws://localhost:" + port + "/",
                            on_message = on_message,
                            on_error = on_error,
                            on_close = on_close)
    ws.on_open = on_open
    ws.run_forever()

    def on_message(ws, message):
        print(message)

    def on_error(ws, error):
        print(error)

    def on_close(ws):
        print("### Connection closed ###\n")

    def on_open(ws):
        def run(*args):
            while True:
                time.sleep(5)
                ws.send("Hello")
            time.sleep(1)
            ws.close()
        thread.start_new_thread(run, ())

def main:
    def on_press(key):
        print("{0} pressed".format(key))

    def on_release(key):
        # DEBUG (in order to end the program in development)
        if key== Key.esc:
        return False

    with Listener(on_press=on_press, on_release=on_release) as listener:
        listener.join()

main()