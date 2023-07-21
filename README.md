# Application qui permet de générer des QrCode en ligne de commande avec Python.
Description
Le Générateur de QR Code est une application Python simple qui vous permet de créer des codes QR avec des URL personnalisées et des formats de fichiers au choix. Cette application nécessite l'installation des modules qrcode et pillow à l'aide de pip. qrcode est utilisé pour générer les codes QR, tandis que pillow est utilisé pour la manipulation d'images, notamment le redimensionnement et l'insertion du logo dans le code QR.

Installation
Avant d'exécuter l'application, assurez-vous d'installer les modules requis en exécutant les commandes suivantes dans votre terminal ou invite de commande :
pip install qrcode pillow

Description
Le Générateur de QR Code est une application Python simple qui vous permet de créer des codes QR avec des URL personnalisées et des formats de fichiers au choix. Cette application nécessite l'installation des modules qrcode et pillow à l'aide de pip. qrcode est utilisé pour générer les codes QR, tandis que pillow est utilisé pour la manipulation d'images, notamment le redimensionnement et l'insertion du logo dans le code QR.

Installation
Avant d'exécuter l'application, assurez-vous d'installer les modules requis en exécutant les commandes suivantes dans votre terminal ou invite de commande :
pip install qrcode pillow

Utilisation
Pour utiliser le Générateur de QR Code, suivez ces étapes :
Lancez le script, il vous demandera d'entrer l'URL que vous souhaitez insérer dans le code QR.
Après avoir saisi l'URL, l'application générera un code QR avec l'URL spécifiée et un logo personnalisé (logo Instagram dans cet exemple) placé au centre du code QR.
Vous devrez ensuite choisir le format de l'image du code QR (PNG, JPG ou JPEG).
Ensuite, fournissez un nom pour le fichier. L'application remplacera les espaces dans le nom par des traits de soulignement pour assurer un nom de fichier valide.
Le code QR sera enregistré dans le répertoire generated_qr_codes avec le nom de fichier au format : AAAA-MM-JJ_nomdefichier.png (ou .jpg ou .jpeg, selon votre choix).
Un message de réussite sera affiché, indiquant que le code QR a été généré avec succès.

Prérequis
    Python 3.x
    Modules : qrcode, pillow
    
import qrcode
import datetime
from PIL import Image
# Votre code ici (incluez le code fourni dans votre script)

Veuillez noter que vous devez remplacer ./source_images/logo_instagram.png par le chemin d'accès de l'image de logo souhaitée. Assurez-vous également d'avoir les autorisations nécessaires pour créer des répertoires et des fichiers dans le répertoire de travail.

Bonne génération de codes QR !
