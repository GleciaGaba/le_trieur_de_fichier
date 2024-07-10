"""Le but de ce projet est de créer un script qui permette de trier automatiquement des
fichiers dans des sous-dossiers en fonction de leur type (extension).

Dans les sources de ce projet, vous trouverez un dossier data qui contient des fichiers
de différents types (images, vidéos, documents...).

Vous pouvez partir de ce dossier ou utiliser n'importe quel dossier de votre disque
dur (le dossier de téléchargements est généralement un bon endroit pour faire le ménage...).

Le but de ce script est de trier les fichiers selon leur type (et donc leur extension) dans des sous-dossiers.

Par exemple, vous devez regrouper tous les fichiers avec l'extension .mp3 ou .wav dans un sous-dossier Musique.

Tous les fichiers textes quant à eux devront se retrouver dans un dossier Documents.

Voici l'association des extensions et des dossiers que vous devez utiliser :

mp3, wav, flac : Musique
avi, mp4, gif : Videos
bmp, png, jpg : Images
txt, pptx, csv, xls, odp, pages : Documents
autres : Divers
Pour ce projet je vous conseille d'utiliser la bibliothèque pathlib que l'on a vu dans la partie précédente.

Vous verrez que c'est bien plus facile de faire ce script avec pathlib qu'avec le module os ou le module glob.



Quelques éléments pour vous aider si vous êtes bloqués :

Pour associer les extensions aux dossiers, pensez à utiliser un dictionnaire.

Pensez à créer le dossier cible avant de déplacer le fichier (rappelez-vous également du paramètre
 exist_ok de la fonction mkdir).

Pour déplacer un fichier, vous pouvez utiliser sur un objet de type Path (provenant de pathlib), la méthode rename.

Questions pour cet exercice
Comment trier les fichiers selon leur type ?"""

from pathlib import Path

# Associer les extensions aux dossiers cibles

dirs = {
    ".mp3": "Musique",
    ".wav": "Musique",
    ".flac": "Musique",
    ".avi": "Videos",
    ".mp4": "Videos",
    ".gif": "Videos",
    ".bmp": "Images",
    ".png": "Images",
    ".jpg": "Images",
    ".txt": "Documents",
    ".pptx": "Documents",
    ".csv": "Documents",
    ".xls": "Documents",
    ".odp": "Documents",
    ".pages": "Documents"
}

#  Récuperer le chemin du dossier dans lequel se trouvent les fichiers
tri_dir = Path.cwd() / "data"

#  Récuperer les fichiers à l'intérieur du dossier

files = [file for file in tri_dir.iterdir() if file.is_file()]

#  Trier les fichiers selon leur extension
for f in files:
    suffix = f.suffix
    output_dir_name = dirs.get(suffix, "Autres")
    output_dir = tri_dir / output_dir_name
    print(output_dir)

    print(f"Fichier: {f.name}, Suffixe: {suffix}, Répertoire cible: {output_dir}")

    output_dir.mkdir(parents=True, exist_ok=True)
    f.rename(output_dir / f.name)
