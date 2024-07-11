with open("/Users/Bazinga/Documents/python_2024/le_trieur_de_fichier/prenoms.txt", "r") as f:
    lines = f.read().splitlines()
    print(lines)

prenoms = []
for line in lines:
    prenoms.extend(line.split())

prenoms_final = [prenom.strip(",. ") for prenom in prenoms]
print(prenoms_final)

with open("/Users/Bazinga/Documents/python_2024/le_trieur_de_fichier/prenoms_final.txt", "w") as f:
    f.write("\n".join(sorted(prenoms_final)))
