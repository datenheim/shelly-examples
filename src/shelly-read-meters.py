import sys
import requests

from prettytable import PrettyTable
from tqdm import trange

# create a copy from _conf.py, name it my_conf.py and fill in your data
try:
    from my_conf import shelly_host as my_host
except ImportError:
    try:
        from _conf import shelly_host as my_host
    except ImportError:
        print("You should copy _conf.py to my_conf.py and fill it with your data!")
        print(sys.exc_info())
        exit()
try:
    from my_conf import shelly_devices as my_devices
except ImportError:
    try:
        from _conf import shelly_devices as my_devices
    except ImportError:
        print("You should copy _conf.py to my_conf.py and fill it with your data!")
        print(sys.exc_info())
        exit()


# defining globals
table = PrettyTable()
table.field_names = ['Device Name', 'Current Watts','Counter 1','Counter 2','Counter 3']
table.align = 'r'

# main
if __name__ == '__main__':
    for num in trange(len(my_devices.id)):
        try:
            response = requests.post(
                my_host.url_device_status,
                data={'id': my_devices.id[num],'auth_key': my_host.auth_key}
                )
        except:
            print(" We tryied to request data for device with ID:", my_devices.id[num], "and name:", my_devices.name[num])
            print("Please check the IDs and the url in your my_conf.py file.")
            exit()
        content = response.json()
        row = [
            my_devices.name[num],
            content['data']['device_status']['meters'][0]['power']] + \
            content['data']['device_status']['meters'][0]['counters'
            ]
        table.add_row(row)
    print(table)
