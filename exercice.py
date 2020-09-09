#!/usr/bin/env python
# -*- coding: utf-8 -*-
def capitaliser_pays(nom):
    nom = nom.split(' ')
    nom = [nom[i].lower() for i in range(len(nom))]
    for i in range(len(nom)):
        if nom[i] != "and":
            nom[i] = nom[i].capitalize()
    
    nom = ' '.join(nom)
    place = nom.find('-')

    if place != -1:
        print(place)
        nom = list(nom)
        nom[place + 1] = nom[place + 1].upper()
        nom = ''.join(nom)
        place = -1
    return nom


if __name__ == '__main__':
    pays = [
        'Guinea-bisAu'
        'AfghanIstan',
        'albania',
        'algeria',
        'AndorRa',
        'angolA',
        'antigua ANd barbuda',
        'argEntina',
        'Armenia',
        'austrAlia',
        'ausTria',
        'azerBaijaN'
    ]
    for i in range(len(pays)):
        pays[i] = capitaliser_pays(pays[i])

    print(pays)
