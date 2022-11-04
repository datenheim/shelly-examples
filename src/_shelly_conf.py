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
