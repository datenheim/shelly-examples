## Shelly Cloud Example 1

This example lists all the devices which are connected to the specified shelly cloud account.
It also checks, if these devices are power meters, and if so, prints the current power of the (first) power meter.

### Preparations
Copy or rename `_shelly_conf.py` to `my_shelly_conf.py` and edit this file as follows:
- in class `shelly_host` fill in the `server_url` and `auth_key` [^1].
```
class shelly_host:
    server_url = 'paste_your_cloud_servers_URL_here'     # for instance 'https://shelly-44-eu.shelly.cloud'
    auth_key = 'paste_your_auth_key_here'                # the very long key you copied from the cloud
    url_device_status = server_url + '/device/status'    # must not be changed normally
```
The other class in that file can be ignored for this example.

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

[^1]:You get them these parameters from either the Shelly Android App or from your login on [https://home.shelly.cloud](https://home.shelly.cloud) by opening the `Menu/User Settings/Authorization Cloud Key`.
