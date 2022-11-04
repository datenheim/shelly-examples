import sys
import requests

from prettytable import PrettyTable
from tqdm import trange

# create a copy from _conf.py, name it my_conf.py and fill in your data
try:
    from my_shelly_conf import shelly_host, shelly_devices
except ImportError:
    try:
        from _shelly_conf import shelly_host, shelly_devices
    except ImportError:
        print("You should copy or rename _shelly_conf.py to my_shelly_conf.py and fill it with your actual data!")
        print(sys.exc_info())
        exit()

# defining globals
table = PrettyTable()
table.field_names = ['Device Name', 'Current Watts','Counter 1','Counter 2','Counter 3']
table.align = 'r'

# main
if __name__ != '__main__':
    print("This code should not be used as package. Exiting...")
else:
    for num in trange(len(shelly_devices.id)):
        try:
            response = requests.post(
                shelly_host.url_device_status,
                data={'id': shelly_devices.id[num],'auth_key': shelly_host.auth_key}
                )
        except Exception as this_ex:
            print(" We tryied to request data for device with ID:", shelly_devices.id[num], "and name:", shelly_devices.name[num])
            print("We caught Exception: ", this_ex)
            print("Please check the IDs and the url in your my_conf.py file.")
            raise this_ex
        content = response.json()
        row = [
            shelly_devices.name[num],
            content['data']['device_status']['meters'][0]['power']] + \
            content['data']['device_status']['meters'][0]['counters']
        table.add_row(row)
    print(table)
