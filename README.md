# Ros Assignment Done By
    Kaleab Yitbarek  


#Instructions
---------------
For Questioin #1 thier are two nodes,
The publisher capture image and publishe it , and will show
the image in the mean time the subscriber gets the image and
converts it to grey scale and show the converted image.

N.B - for starting 10 secs it doesn't publish, but after that it 
        will publish and reapeat it after 10 secs.

```
    - ./scripts/image_publisher.py
    - ./scripts/image_subscriber.py
```


#For Question #2 
Thier is only one node 
Usig the GUI you can control the movments of x and y also its 
angular movments.
Also can change the background of the turtlesim_node.

N.B - sorry i didn't prepate launch file, so start turtlesim_node
      separetly.

```
  - ./scripts/turtlesim_controller.py
```

#For Question #3 
Thier is only one node found in

```
  - ./scripts/fractal.py
```
N.B - sorry i didn't prepate launch file, so start turtlesim_node
      separetly.

#For Question #4

#Q - 4.1
    The blender file and the client code are found at 
    ```
        ./blender files/server_blender.blend
        ./scripts/turtle_client.py
    ```
#Q - 4.2
    The blender file and the server node are found at
    ```
        ./blender files/blender_client.blend
        ./scripts/turtle_server.py
    ```

#For Question #5 
Thier is client node and server node. 
Start the Server node first , then start the client node and
give arguments of integers separeted by space.

Example
```
    rosrun check_prime_client.py 4 5 6
```

Nodes are found in
```
    - ./scripts/check_prime_client.py
    - ./scripts/check_prime_server.py
```

 