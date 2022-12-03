from datetime import *
import pytz

#Here I am defining the USA timezones and converting their output to show in standard 12 hour intervals instead of the default military time format it was showing before
us_central = datetime.now(pytz.timezone('US/Central')).strftime("%m/%d/%Y, %I:%M %p")
us_eastern = datetime.now(pytz.timezone('US/Eastern')).strftime("%m/%d/%Y, %I:%M %p")
us_mountain = datetime.now(pytz.timezone('US/Mountain')).strftime("%m/%d/%Y, %I:%M %p")
us_pacific = datetime.now(pytz.timezone('US/Pacific')).strftime("%m/%d/%Y, %I:%M %p")
us_alaska = datetime.now(pytz.timezone('US/Alaska')).strftime("%m/%d/%Y, %I:%M %p")
us_hawaii = datetime.now(pytz.timezone('US/Hawaii')).strftime("%m/%d/%Y, %I:%M %p")
#I created a variable that will list the available timezones the user can choose if they need to view a list while running the program
timezonelisting = ("Alaska, Central, Eastern, Hawaii, Mountain, or Pacific")

#This is the main function of the program that asks the user for a USA timezone 
def getuserstimezone():
    #If the user needs to see what timeszones are available in the program they can type "view" and the timezonelisting variable will be printed
    timezone = input("Enter USA Timezone or enter 'view' to list available timezones:")
    #Below are all the instances of when a correct timezone is entered and if it is entered correctly the corresponding variable will be printed out in standard 12 hour time format
    if timezone == 'Central' or timezone == 'central':
        print('US Central Date/Time', us_central)
    #If the user enters "view" the available timezones will be listed and the function will start over
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
    #If an incorrect value is entered then the user will be prompted to enter a valid timezone and the function will restart
    else:
        print('Please enter valid USA time zone')
        getuserstimezone()
#Here the function is run        
getuserstimezone()

while True:
    #Here we ask the user if they want to continue and try another timezone
    restart =input("Would you like to continue? Please type y for yes or n for no")
    #If the user responds with 'y' the top function starts over
    if restart =='y':
        getuserstimezone()
    #If the user enters 'n' they are given a goodbye message and the program closes
    elif restart =='n':
       print('Goodbye :)')
       break
    #If neither 'y' or 'n' are entered then they are given an error message and asked to restart the program since it will close automatically.
    elif restart !='y' or 'n':
       print('Incorrect value entered. Please restart program')
       break
