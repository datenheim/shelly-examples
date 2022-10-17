## How to play with cloud connected shelly devices
In this repository I'll document some experiments with shelly devices that are connected to the shelly cloud.
The experiments aim to make use of the devices data while keeping them connected to the shelly cloud and thus being able to use the shelly smartphone App.

While shelly devices can natively connect to an MQTT broker afaik it implies that you loose the connection to the shelly cloud and thus the App is useless.

All examples here try to overcome this limitation by getting the data via the shelly cloud API.

## Example 1: `shelly-read-meters.py`
This example collects the current power and counter values from one or many shelly Plug S devices which are connected to the shelly cloud.