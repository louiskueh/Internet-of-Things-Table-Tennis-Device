# Files
Please find the workflow in the *Workflow-graph.pdf*
## Device files
* main.py - main file to run, measures difference between angle, poll for accelerometer reading
* acc.py - accelerometer
* mag.py - magnetometer
* functions.py - MQTT, additional functions

## Server files
* mqttServer.py - start up server, accumulate and output results (paho)
* mqttServer_publisher.py (not used) - send data from server to device
* text.py - API for printing on command line

## Correct reading of sensor data
  * Appropriate sensor settings
  * Byte data extraction
  * Two's complement conversion
  * Magnetometer
    -> Heading calculation from raw data in x, y and z directions
    -> Declination angle correction
    -> Angle conversion to degrees
    -> Relative angle difference between readings
  * Accelerometer
    -> Reading concatenation from high and low registers
    -> Acceleration magnitude calculation

## Sending of data to MQTT broker
  * Mosquito broker setup on a laptop
  * Device sends to laptop via MQTT (JSON format)through EEERover network
  * Server(cloud) receives JSON packets and processes data and outputs statistics of counts and guidance to improve swings

## On device processing/formatting
  * Converting raw data to degrees in 3D
  * Triggered by push button to switch between swing detection and compass
  * using accelerometer to set a threshold of detecting swing
  * Differentiating different types of swing by determining the angle difference using data from magnetometer

## Efficient and maintainable code
  * Files modularised (one for magnetometer, one for accelerometer...)
  * Only import what is needed from particular modules *from machine import ...*
  * Comments where needed

## Imaginative product
  * Teaches person how to play table tennis on his own
  * Done through measuring swings, with guidance if no swing is detected (E.g. *swing left to right more*)
  * Selectable compass function

## Addition sensors, other I/O, cloud functionality
  * Adapted accelerometer onto board for measurement triggering
  * Only send data when accelerometer above certain magnitude(*swing detected*), minimising data sent
  * Server acts like a cloud, processing and output can be sent to app/website/other device, etc

# Further improvement
  * Introduce more sensors for more accurate reading (e.g. gyroscope)
  * Use machine learning algorithms to analyse an individuals movement, enabling the device to get more accurate as a particular person uses it
  * Currently strapped on to a glove, perhaps adapting it to a bracelet (e.g. fitbit)/ adapting to be on the bottom of the handle
  * Utilise algorithms such as the Kalman filter to improve accuracy


# Website
[link-to-website](https://octavianhainadal.wixsite.com/pikachu)


# Contribution
  * Website - Octavian Rosu
  * Everything else - Louis Kueh, Kavin Winson, Un Kei Leong
