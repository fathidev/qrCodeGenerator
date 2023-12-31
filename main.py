import qrcode
import datetime
from PIL import Image

# functions to get the date, the extension and the full name of the file
def getDate ():
    dateToday = datetime.date.today()
    return dateToday

def getExtension(choice):
    if choice == 1:
        return ".png"
    elif choice == 2:
        return ".jpg"
    else :
        return ".webp"

    
def makeFullName (name, extension, dateToday):
    return f'{dateToday}_{name}{extension}'
# end of functions

# open the logo and resize it
logo = Image.open('./sources_images/logo_instagram.png').resize((60, 60))
print(logo.size)

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
# remove the spaces
data = data.replace(" ", "")
qr_big.add_data(data)
qr_big.make()

# create the QR Code image
img_qr_big = qr_big.make_image(
    fill_color = "black", 
    back_color = "white"
).convert('RGB')

# paste the logo in the middle of the QR Code
pos = ((img_qr_big.size[0] - logo.size[0]) // 2, (img_qr_big.size[1] - logo.size[1]) // 2)
img_qr_big.paste(logo, pos)

# ask the user for the extension of the file
while True:
    try:
        choice = int(input("Etape 2 : Quel format souhaitez-vous pour le QR Code ?\n1. PNG\n2. JPG\n3. WEBP\nVotre choix : "))
        if choice < 1 or choice > 3:
            raise ValueError
        break
    except ValueError:
        print("Veuillez choisir un chiffre entre 1 et 3")

# get the extension
extension = getExtension(choice)

# ask the user for the name of the file
name = input("Etape 3 : Quel nom souhaitez-vous donner au fichier ? : ")
# replace the spaces by underscores
name = name.replace(" ", "_")

# create the full name of the file
full_name = makeFullName(name, extension, getDate())

# save the QR Code
img_qr_big.save(f'./generated_qr_codes/{full_name}')

# print the success message
print("*" * 50)
print(f"Félicitations! Le QR Code nommé {full_name} a bien été généré")
print("*" * 50)




