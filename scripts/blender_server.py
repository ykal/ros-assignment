import socket, pickle
import bpy

prev_data = []    

def start_server():
    host = "127.0.0.1"
    global port
    port = 5054

    server = socket.socket()
    server.bind((host, port))
    server.listen(1)

    global c
    global d
    c, add = server.accept();
    print("Client Connected")



if __name__ == "__main__":
    start_server()
    obj = bpy.context.object
    while True:
        loc = obj.location
        data = [loc[0], loc[1]]
        if prev_data != data:
            prev_data = data
            data_str = pickle.dumps(data)
            c.send(data_str)
            print(data)
            print("location has been sent")
    