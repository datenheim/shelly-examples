class shelly_host:
    server_url = 'paste_your_cloud_servers_URL_here'     # for instance 'https://shelly-44-eu.shelly.cloud'
    auth_key = 'paste_your_auth_key_here'                # the very long key from the cloud
    url_device_status = server_url + "/device/status"      # must not be changed normally


class shelly_devices:
    id = ['id1', 'id2', 'id3']                    # paste the hexadecimal ids as found in the device info
    name = ['name1', 'name2', 'name3']            # give a readable name for the devices
