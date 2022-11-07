import sys
import json
import requests

from prettytable import PrettyTable
from tqdm import trange

# create a copy from _conf.py, name it my_conf.py and fill in your data
try:
    from my_shelly_conf import shelly_host, shelly_rqurl
except ImportError:
    try:
        from _shelly_conf import shelly_host, shelly_rqurl
    except ImportError:
        print("You should copy or rename _shelly_conf.py to my_shelly_conf.py and fill it with your actual data!")
        print(sys.exc_info())
        exit()


def ff2d(inp):
    fl = float(inp)
    return f'{fl:.2f}'


# create a table
table = PrettyTable()
# add a header to the table
table.field_names = ['Device ID', 'Code', 'Online', 'Wifi', 'Meters?', 'Power [W]']
# define right alignment for all columns
table.align = 'c'

# main program
if __name__ != '__main__':
    print("This code should not be used as package. Exiting...")
else:
    # try to request the data for each device in the list
    # for num in trange(len(shelly_devices.idn)):
    url  = shelly_rqurl.device_info
    data = {'auth_key': shelly_host.auth_key}
    try:
        response = requests.post(url, data)
    except Exception as this_ex:
        print(" We tryied to request data from", url)
        print("We caught Exception: ", this_ex)
        print("Please check server_url and auth_key in your my_conf.py file.")
        raise this_ex

    # decide the response to a json dictionary
    content = response.json()

    # extract the devices_status array
    try:
        statuses = content['data']['devices_status']
    except Exception as this_ex:
        print(" Extracting device statuses has failed.")
        print("We caught Exception: ", this_ex)
        print("Please check server_url and auth_key in your my_conf.py file.")
        raise this_ex

    # this basically puts all hex device ids in a list
    keys = statuses.keys()
    if len(keys) == 0:
        print("We obtained zero device statuses. Is there anything connected to this cloude account?")
    else:
        for key in keys:
            # grab name, watthours and counters from the response
            id = statuses[key]['_dev_info']['id']
            gen = statuses[key]['_dev_info']['gen']
            cod = statuses[key]['_dev_info']['code']
            onl = str(statuses[key]['_dev_info']['online'])
            ssi = statuses[key]['wifi_sta']['ssid']
            if 'meters' in statuses[key]:
                mtr = str(len(statuses[key]['meters']))
                mtr_cp = ff2d(statuses[key]['meters'][0]['power'])
            else:
                mtr = 'None'
                mtr_sp = 'n.a.'
            # add all that to the table as a new row
            table.add_row([id, cod, onl, ssi, mtr, mtr_cp])

        # finally print the table
        print(table)
