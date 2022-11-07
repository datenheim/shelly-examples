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

# create a table
table = PrettyTable()
# add a header to the table
table.field_names = ['Device Name', 'Current Watts','Counter 1','Counter 2','Counter 3', 'Is ON?', "T [°C]"]
# define right alignment for all columns
table.align = 'r'


def ff2d(inp):
    fl = float(inp)
    return f'{fl:.2f}'


# main program
if __name__ != '__main__':
    print("This code should not be used as package. Exiting...")
else:
    # try to request the data for each device in the list
    for num in trange(len(shelly_devices.idn)):
        try:
            response = requests.post(
                shelly_host.url_device_status,
                data={'id': shelly_devices.idn[num][0], 'auth_key': shelly_host.auth_key}
                )
        except Exception as this_ex:
            print(" We tryied to request data for device with ID:", shelly_devices.idn[num][0], "and name:", shelly_devices.idn[num][1])
            print("We caught Exception: ", this_ex)
            print("Please check the IDs and the url in your my_conf.py file.")
            raise this_ex
        
        # decide the response to a json dictionary
        content = response.json()

        # grab name, watthours and counters from the response
        dna = shelly_devices.idn[num][1]
        # format the whathours a bit nicer
        whs = ff2d(content['data']['device_status']['meters'][0]['power'])
        ctl =      content['data']['device_status']['meters'][0]['counters']
        rly =  str(content['data']['device_status']['relays'][0]['ison'])
        tmp = ff2d(content['data']['device_status']['tmp']['tC'])
        # add all that to the table as a new row
        table.add_row([dna, whs] + ctl + [rly] + [tmp])

    # finally print the table
    print(table)
