import socket, pickle
import bpy
import mathutils
delta = (0.0, 0.0, 0.0)

bpy.context.object.location = (0, 0, 0)

obj = bpy.context.object

loc = obj.location
print(loc)

def start_client():
    host = "127.0.0.1"
    port = 5053
    client = socket.socket()
    try:
        client.connect((host, port));
    except Exception as e:
        print("Server is Down")

    while True:
        try:
            data = client.recv(4096)
            if data:
                print("recived data")
                data = pickle.loads(data);
                global delta
                delta = (data[0], data[1], 0.0)
                loc = obj.location
                obj.location = loc + mathutils.Vector(delta)
                print(obj.location)
                
            
        except Exception as e:
            pass
    
    

if __name__ == "__main__":
    start_client()