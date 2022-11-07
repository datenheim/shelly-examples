# How to play with cloud connected shelly devices
In this repository I'll document some experiments with shelly devices that are connected to the shelly cloud.
The experiments aim to make use of the devices data while keeping them connected to the shelly cloud and thus being able to use the shelly smartphone App.

While shelly devices can natively connect to an MQTT broker afaik it implies that you loose the connection to the shelly cloud and thus the App is useless.

All examples here try to overcome this limitation by getting the data via the shelly cloud API.

**Please read ech examples individual readme for further details. The mentioned preparations must only be done once - they cover all examples.**

# Examples

## Shelly Cloud Example 1: [`shelly-list-devices.py`](src/shelly-list-devices.md)

This example produces a list of all devices connected to your cloud shelly.cloud account.

It also checks if they have the feature of power metering, and if so, displays their latest power measurement.

### Output
```
+-----------+---------+--------+------------+---------+-----------+
| Device ID |   Code  | Online |    Wifi    | Meters? | Power [W] |
+-----------+---------+--------+------------+---------+-----------+
|   bc3721  | SHPLG-S |  True  |  Mondtau   |    1    |    0.00   |
|   22183e  | SHPLG-S |  True  |  Mondtau   |    1    |   96.68   |
|   22962d  | SHPLG-S |  True  |  Mondtau   |    1    |   119.86  |
|   2296f0  | SHPLG-S |  True  |  Mondtau   |    1    |   70.57   |
|   ecb83f  | SHPLG-S |  True  | MONDSCHEIN |    1    |   31.90   |
+-----------+---------+--------+------------+---------+-----------+
```
### Purpose
Basically to get a list of all the devices that are of a specific type.
You can use the `code` key to distinguish them (here `SHPLG-S` means `Shelly Plug-S`).
For instance a list of all Shelly PlugS devices could also be used in example 2.

## Shelly Cloud Example 2: [`shelly-read-meters.py`](src/shelly-read-meters.md)

This example collects the current power and counter values from one or many shelly Plug S devices which are connected to the shelly cloud.

### Output
```
100%|█████████████████████████████████| 5/5 [00:01<00:00,  4.83it/s]
+--------------+---------------+-----------+-----------+-----------+--------+--------+
|  Device Name | Current Watts | Counter 1 | Counter 2 | Counter 3 | Is ON? | T [°C] |
+--------------+---------------+-----------+-----------+-----------+--------+--------+
|    Workbench |        107.46 |   120.986 |   119.486 |   122.095 |   True |  23.88 |
|      Network |         70.74 |    70.701 |    72.118 |    70.424 |   True |  24.03 |
|     Steambox |          0.00 |         0 |         0 |         0 |  False |  22.93 |
| Coolermaster |         91.93 |     92.11 |    92.545 |    93.021 |   True |  23.43 |
|   Meter_Gdhg |         32.08 |    32.089 |    32.216 |     32.31 |   True |  24.88 |
+--------------+---------------+-----------+-----------+-----------+--------+--------+
```

# Final thoughts
With shelly devices you have the choice to __*EITHER*__ connect them to shelly cloud and make use of the shelly App __*OR*__ connect them to a MQTT broker of your choice. In the latter case you will loose the control via the Android App afaik.

This python example is just a first step to get the current readings of a number of cloud connected shelly Plug S devices for __further analysis__. I put it up in the hope it will help somebody.

By "further analysis" one could imagine a Linux service that regularly polls the current power state from shelly cloud and publishes these to an MQTT broker - and thus get's you the best of both worlds: have the shelly cloud & App and also get the data on your choice of MQTT broker. If you are interested in such an example stay tuned.