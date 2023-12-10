import random

#variable qui contient les caractères qu'on va utiliser pour générer le mot de passe

CaractereMinuscule = "abcdefghijklmnopqrstuvwxyz"
CaractereMajuscule = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
CaractereSpeciaux = "!@#$%^&*()_+"
CaractereNombre = "0123456789"

#variable qui contient la longueur du mot de passe
longueur = 15

#Génération du mot de passe avec la fonction random.sample qui va prendre les caractères de chaque variable et les mélanger
motDePasse = "".join(random.sample(CaractereMinuscule + CaractereMajuscule + CaractereSpeciaux + CaractereNombre, longueur))

#affichage du mot de passe
print("le mot de pas généré est ", motDePasse)