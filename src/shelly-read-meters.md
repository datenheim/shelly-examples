## Shelly Cloud Example 2

This example collects the current power and counter values from one or many shelly Plug S devices which are connected to the shelly cloud.

The received values will be printed as a table.

### Preparations
Copy or rename `_shelly_conf.py` to `my_shelly_conf.py` and edit this file as follows:
- in class `shelly_host` fill in the `server_url` and `auth_key` [^1].
- in class `shelly_devices` fill the list `idn` with tuples of the ID(s)[^2]<br>and a nice name for all your helly Plug S (or similar) device(s).
```
class shelly_host:
    server_url = 'paste_your_cloud_servers_URL_here'     # for instance 'https://shelly-44-eu.shelly.cloud'
    auth_key = 'paste_your_auth_key_here'                # the very long key you copied from the cloud
    url_device_status = server_url + '/device/status'    # must not be changed normally


class shelly_devices:
    # use the hex device id, and a nice name for the device
    idn = [
        ('000001', 'Workbench'),
        ('f2d000', 'Network'),
        ]
```

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

### Final thoughts
With shelly devices you have the choice to __*EITHER*__ connect them to shelly cloud and make use of the shelly App __*OR*__ connect them to a MQTT broker of your choice. In the latter case you will loose the control via the Android App afaik.

This python example is just a first step to get the current readings of a number of cloud connected shelly Plug S devices for __further analysis__. I put it up in the hope it will help somebody.

By "further analysis" one could imagine a Linux service that regularly polls the current power state from shelly cloud and publishes these to an MQTT broker - and thus get's you the best of both worlds: have the shelly cloud & App and also get the data on your choice of MQTT broker. If you are interested in such an example stay tuned.

[^1]:You get them these parameters from either the Shelly Android App or from your login on [https://home.shelly.cloud](https://home.shelly.cloud) by opening the `Menu/User Settings/Authorization Cloud Key`.
[^2]: You have to use the hexadcimal ID given in the devices Settings/Device Info/Device ID field!
