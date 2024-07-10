from pathlib import Path

chemin = Path.cwd()

dir = {
    "Films_c": ["Le seigneur des anneaux",
                "Harry Potter",
                "Moon",
                "Forrest Gump"],
    "Employes_c": ["Paul",
                   "Pierre",
                   "Marie"],
    "Exercices_c": ["les_variables",
                    "les_fichiers",
                    "les_boucles"]
}

for dossier_principal, sous_dossiers in dir.items():
    for dossier in sous_dossiers:
        chemin_dossier = chemin / dossier_principal / dossier
        chemin_dossier.mkdir(exist_ok=True, parents=True)
