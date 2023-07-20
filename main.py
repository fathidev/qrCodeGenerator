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

# open the logo and resize it
logo = Image.open('./source_pictures/logo_instagram.png').resize((60, 60))

# create the QR Code
qr_big = qrcode.QRCode(
    version = 3,
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=9,
    border=3
)

# print the welcome message
print("*" * 50)
print("Bienvenue dans le générateur de QR Code de Fathi !")
print("*" * 50)

# ask the user for the URL to insert in the QR Code
data = input("Etape 1 : Saisissez l'URL à insérer dans le QR CODE : ")
qr_big.add_data(data)
qr_big.make()

# create the QR Code image
img_qr_big = qr_big.make_image(
    fill_color = "blue", 
    back_color = "white"
).convert('RGB')

# paste the logo in the middle of the QR Code
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)

# ask the user for the extension of the file
choice = int(input("Etape 2 : Quel format souhaitez-vous pour le QR Code ?\n1. PNG\n2. JPG\n3. JPEG\nVotre choix : "))
extension = makeExtension(choice)

# ask the user for the name of the file
name = input("Etape 3 : Quel nom souhaitez-vous donner au fichier ? : ")
name = name.replace(" ", "_")

# create the full name of the file
full_name = makeFullName(name, extension, getDate())

# save the QR Code
img_qr_big.save(f'./generated_qr_codes/{full_name}')




