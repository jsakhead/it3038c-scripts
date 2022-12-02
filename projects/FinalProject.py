from datetime import *
import pytz

us_central = datetime.now(pytz.timezone('US/Central')).strftime("%m/%d/%Y, %I:%M %p")
us_eastern = datetime.now(pytz.timezone('US/Eastern')).strftime("%m/%d/%Y, %I:%M %p")
us_mountain = datetime.now(pytz.timezone('US/Mountain')).strftime("%m/%d/%Y, %I:%M %p")
us_pacific = datetime.now(pytz.timezone('US/Pacific')).strftime("%m/%d/%Y, %I:%M %p")
us_alaska = datetime.now(pytz.timezone('US/Alaska')).strftime("%m/%d/%Y, %I:%M %p")
us_hawaii = datetime.now(pytz.timezone('US/Hawaii')).strftime("%m/%d/%Y, %I:%M %p")
timezonelisting = ("Alaska, Central, Eastern, Hawaii, Mountain, or Pacific")

def getuserstimezone():
    timezone = input("Enter USA Timezone or enter 'view' to list available timezones:")
    if timezone == 'Central' or timezone == 'central':
        print('US Central Date/Time', us_central)
    elif timezone == 'view' or timezone == 'View':
        print(timezonelisting)
        getuserstimezone()
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
        getuserstimezone()
        
getuserstimezone()

while True:
    restart =input("Would you like to continue? Please type y for yes or n for no")
    if restart =='y':
        getuserstimezone()
    elif restart =='n':
       print('Goodbye :)')
       break
    elif restart !='y' or 'n':
       print('Incorrect value entered. Please restart program')
       break
