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


For Question #2 thier is only one node 
Usig the GUI you can control the movments of x and y also its 
angular movments.
Also can change the background of the turtlesim_node.

N.B - sorry i didn't prepate launch file, so start turtlesim_node
      separetly.

```
  - ./scripts/turtlesim_controller.py
```

For Question #5 thier is client node and server node. 
Start the Server node first , then start the client node and
give arguments of integers separeted by space.
```
    rosrun check_prime_client.py 4 5 6
```

```
    - ./scripts/check_prime_client.py
    - ./scripts/check_prime_server.py
```

N.B -   I didn't finish the other 2 questions. I will submit it ASA possible.   