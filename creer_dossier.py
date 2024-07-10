from pathlib import Path

chemin = Path.cwd()

dir = {
    "Films": ["Le seigneur des anneaux",
              "Harry Potter",
              "Moon",
              "Forrest Gump"],
    "Employes": ["Paul",
                 "Pierre",
                 "Marie"],
    "Exercices": ["les_variables",
                  "les_fichiers",
                  "les_boucles"]
}

for cle, value in dir.items():

    if cle == "Films":
        chemin_dossier = chemin / "Films"
        chemin_dossier.mkdir(exist_ok=True)
        files = dir.get("Films")
        for f in files:
            file = chemin_dossier / f
            file.touch()
            print(file)

    elif cle == "Employes":
        chemin_dossier = chemin / "Employes"
        chemin_dossier.mkdir(exist_ok=True)
        files = dir.get("Employes")
        for f in files:
            file = chemin_dossier / f
            file.touch()
    elif cle == "Exercices":
        chemin_dossier = chemin / "Exercices"
        chemin_dossier.mkdir(exist_ok=True)
        files = dir.get("Exercices")
        for f in files:
            file = chemin_dossier / f
            file.touch()
    else:
        print("Cette clé n'existe pas")
