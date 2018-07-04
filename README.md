
![f27038_b3cec7a828da47f591769e6801ab0376_mv2](https://user-images.githubusercontent.com/2521843/42291927-c51fa02c-7fc6-11e8-933e-f8bc6eb80e25.png)
![embeddedcw](https://user-images.githubusercontent.com/2521843/42292107-ff15c0b2-7fc7-11e8-9237-3b27faeb9db7.gif)

# Objective

* Invent an IoT (Internet of Things) product

* Teaches person how to play table tennis on his own with guidance

* Swing Analyzer by measuring angles of swing in 3D


## Approach

Utilising the systems of a microprocessor, magnetometer and accelerometer, the final product is able to track the angle, direction and accerelation of hand movement. The system autonomously sends the data over a wireless communication to the server, where the analysis is carried out and any successful swings and individual feedback/records are output in realtime, capable of guiding a person how to play table tennis on his own.


### Sending of data to MQTT broker
* Mosquito broker setup on a laptop

* Device sends to laptop via MQTT (JSON format) through EEERover network

* Server(cloud) receives JSON packets and processes data and outputs statistics of counts and guidance to improve swings



### On device processing/formatting
* Triggered by push button to switch between swing detection and compass

* Utilize accelerometer to set a threshold of detecting swing

* Differentiating different types of swing by determining the angle difference using data from magnetometer



### Addition sensors, other I/O, cloud functionality
* Adapted accelerometer onto board for measurement triggering

* Only send data when accelerometer above certain magnitude(swing detected), minimising data sent

* Server acts like a cloud, processing and output can be sent to app/website/other device, etc
