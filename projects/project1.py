from datetime import datetime
import pytz

timezone = input("Enter USA Timezone:")

us_central = datetime.now(pytz.timezone('US/Central'))
us_eastern = datetime.now(pytz.timezone('US/Eastern'))
us_mountain = datetime.now(pytz.timezone('US/Mountain'))
us_pacific = datetime.now(pytz.timezone('US/Pacific'))
us_alaska = datetime.now(pytz.timezone('US/Alaska'))
us_hawaii = datetime.now(pytz.timezone('US/Hawaii'))

if timezone == 'Central' or timezone == 'central':
    print('US Central Date/Time', us_central)
elif timezone == 'Eastern' or timezone == 'eastern':
    print('US Eastern Date/Time', us_eastern)
elif timezone == 'Mountain' or timezone == 'mountain':
    print('US Mountain Date/Time', us_mountain)
elif timezone == 'Pacific' or timezone == 'pacific':
    print('US Pacific Date/Time', us_pacific)
elif timezone == 'Alaska' or timezone == 'alaska':
    print('US Alaska Date/Time', us_alaska)
elif timezone == 'Hawaii' or timezone == 'hawaii':
    print('US Hawaii Date/Time', us_hawaii)
else:
    print('Please enter valid USA time zone')