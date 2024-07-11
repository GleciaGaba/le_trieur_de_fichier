from pathlib import Path
import unicodedata

# Chemin du fichier d'entrée
chemin = Path.cwd() / "prenoms.txt"
print(chemin)

# Lire le contenu du fichier
lire = chemin.read_text(encoding='utf-8')
# Normaliser le texte
texte_normalise = unicodedata.normalize('NFD', lire)
coup = texte_normalise.split(", ")
ordre = sorted(coup)

prenoms = Path.cwd() / "prenoms_ordre.txt"
prenoms.touch()

with prenoms.open('w', encoding='utf-8') as f:
    for prenom in ordre:
        print(prenom)
        f.write(prenom + "\n")

