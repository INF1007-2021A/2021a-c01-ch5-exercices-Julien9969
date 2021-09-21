#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
        #fonction abs()

    if number<0:
       absolute_number=(number**2)**(0.5)
    else:
        absolute_number=number
    return absolute_number



def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'
    list=[]
    for char in prefixes:
        nom=char+suffixe
        list.append(nom)

    return list

def prime_integer_summation() -> int:
    compteur=2
    nombre = 5
    somme=5
   #correction prof dans le fichier exo version prof
    while compteur<100:
        B=True
        j= nombre // 2
        for i in range(2, j):
           if nombre%i ==0:
               B=False
               break

        if B==True:
            somme+=nombre
            compteur+=1
        nombre+=1
           
       

    return somme


def factorial(number: int) -> int:
    facto=1 # 0!=1
    for i in range(1, number):
        facto+=facto*i
    return facto


def use_continue() -> None:
    for i in range(1, 11):
        if i == 5:
            continue
        else:
            print(i)

# correction fichier prof
def verify_ages(groups: List[List[int]]) -> List[bool]:
    list_accept=[]
    for group in groups:
        resultat = True
        if len(group)>10 or len(group)<4:
            list_accept.append(False)
            continue
        
        for individual in group:

            if individual<18:
                resultat=False

            if individual>70:
                for individual in group:
                    if individual==50:
                        resultat=False
        
        for individual in group:
            if individual==25:
                resultat=True

        list_accept.append(resultat) 

    return list_accept


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 0
    print(f"La factiorelle du nombre {number} est: {factorial(number)}")
    
    print(f"L'affichage de la boucle est:")
    use_continue()

    groups = [
        [15, 28, 65, 70, 72], [18, 24, 22, 50, 70], [25, 2],
              [20, 22, 23, 24, 18, 75, 51, 49, 100, 18, 20, 20], [70, 50, 26, 28], [75, 50, 18, 25],
              [13, 25, 80, 15], [20, 30, 40, 50, 60], [75, 50, 100, 28]
    ]
    print(f"Les différents groupes sont: {groups}")
    print(f"L'acceptance des groupes est: {verify_ages(groups)}")


if __name__ == '__main__':
    main()
