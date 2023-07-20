import qrcode
import datetime
from PIL import Image

# functions to get the date, the extension and the full name of the file
def getDate ():
    dateToday = datetime.date.today()
    return dateToday

def makeExtension(choice):
    if choice == 1:
        return ".png"
    elif choice == 2:
        return ".jpg"
    elif choice == 3:
        return ".jpeg"
    else:
        return ".png"
    
def makeFullName (name, extension, dateToday):
    return f'{dateToday}_{name}{extension}'
# end of functions