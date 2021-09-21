#!/usr/bin/env python
# -*- coding: utf-8 -*-


from typing import List


def convert_to_absolute(number: float) -> float:
    return 0


def use_prefixes() -> List[str]:
    prefixes, suffixe = 'JKLMNOPQ', 'ack'

    return [""]


def prime_integer_summation() -> int:
    prime = [2, 3, 5]
    number = 6
    while len(prime)<100:
        is_prime= True
        for diviseur in range(2, number // 2):
            if number % diviseur == 0:
                #pas premier
                is_prime=False
                break
        if is_prime == True:
            prime.append(number)
        number+=1


    return sum(prime)


def factorial(number: int) -> int:
    return 0


def use_continue() -> None:
    pass


def verify_ages(groups: List[List[int]]) -> List[bool]:
    accept=[]
    for group in groups:
        if len(group) > 10 or len(group)<=3:
            accept.append(False)

        if 25 in group:
            accept.append(True)
            continue

        if min(group)<18:
            accept.append(False)
            continue

        if 50 in group and max(group)>70:
            accept.append(False)
            continue

        accept.append(True)


    return accept


def main() -> None:
    number = -4.325
    print(f"La valeur absolue du nombre {number} est {convert_to_absolute(number)}")

    print(f"La liste des noms générés avec les préfixes est: {use_prefixes()}")

    print(f"La somme des 100 premiers nombre premier est : {prime_integer_summation()}")

    number = 10
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
