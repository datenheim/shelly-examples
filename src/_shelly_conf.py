class shelly_host:
    server_url = 'paste_your_cloud_servers_URL_here'     # for instance 'https://shelly-44-eu.shelly.cloud'
    auth_key = 'paste_your_auth_key_here'                # the very long key you copied from the cloud


class shelly_devices:
    # use the real hex device ids of your devices, and a nice name for the device
    idn = [
        ('000001', 'Workbench'),
        ('f2d000', 'Network'),
        ]


class shelly_rqurl:
    device_status = shelly_host.server_url + '/device/status/'
    device_info = shelly_host.server_url + '/device/all_status?show_info=true'
