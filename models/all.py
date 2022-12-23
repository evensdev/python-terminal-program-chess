from tinydb import TinyDB, Query, where
import datetime

# Base de données
db = TinyDB('db.json')


# LISTE DE JOUEURS INSCRITS
PLAYER_SUBSCRIBED = [['Evens', 'JOSEPH', '13/06/1991', 'm', '1'],
                  ['Elodie', 'JOSEPH', '28/11/1981', 'f', '2'],
                  ['Nina', 'JOSEPH', '02/03/2023', 'f', '3'],
                  ['Kylian', 'JOSEPH', '02/03/2023', 'm', '4'],
                  ['Clara', 'JOSEPH', '02/03/2023', 'f', '5'],
                  ['Chelsea', 'JOSEPH', '12/05/2025', 'f', '6'],
                  ['Seven', 'JOSEPH', '12/05/2025', 'f', '7'],
                  ['Elohim', 'JOSEPH', '04/06/2027', 'm', '8'],
                     ['Tom', 'JOSEPH', '04/06/2027', 'm', '1'],
                     ['Kerry', 'JOSEPH', '04/06/2027', 'm', '2'],
                     ['Jess', 'JOSEPH', '04/06/2027', 'm', '3'],
                     ['Linda', 'JOSEPH', '04/06/2027', 'm', '4'],
                     ['Max', 'JOSEPH', '04/06/2027', 'm', '5'],
                     ['Gerald', 'JOSEPH', '04/06/2027', 'm', '6'],
                     ['Sabine', 'JOSEPH', '04/06/2027', 'm', '7'],
                     ['Oscar', 'JOSEPH', '04/06/2027', 'm', '8']
                     ]

LIST_OF_DUEL = [[

    [['Evens', 0], ['Clara', 0]],
       [['Elodie', 0], ['Chelsea', 0]],
       [['Nina', 0], ['Kylian', 0]],
       [['Kylian', 0], ['Elohim', 0]]
    ],
               [[['Evens', 0], ['Elodie', 0]],
       [['Kylian', 0], ['Chelsea', 0]],
       [['Nina', 0], ['Clara', 0]],
       [['Clara', 0], ['Seven', 0]]
    ],
               [[['Evens', 0], ['Chelsea', 0]],
       [['Elodie', 0], ['Seven', 0]],
       [['Nina', 0], ['Seven', 0]],
       [['Kylian', 0], ['Clara', 0]]
    ],
               [[['Evens', 0], ['Seven', 0]],
       [['Elodie', 0], ['Elohim', 0]],
       [['Nina', 0], ['Elohim', 0]],
       [['Kylian', 0], ['Elohim', 0]]
    ]]



LIST_ROUNDS = [

    ["Round n°1",
    datetime.datetime(2022, 8, 10, 14, 25, 22, 195002),
     datetime.datetime(2022, 8, 10, 17, 25, 22, 195002),
     [LIST_OF_DUEL[0]]
     ],
    ["Round n°2",
    datetime.datetime(2022, 8, 10, 14, 25, 22, 195002),
     datetime.datetime(2022, 8, 10, 17, 25, 22, 195002),
     [LIST_OF_DUEL[1]]
     ],
    ["Round n°3",
    datetime.datetime(2022, 8, 10, 14, 25, 22, 195002),
     datetime.datetime(2022, 8, 10, 17, 25, 22, 195002),
     [LIST_OF_DUEL[2]]
     ],
    ["Round n°4",
    datetime.datetime(2022, 8, 10, 14, 25, 22, 195002),
     datetime.datetime(2022, 8, 10, 17, 25, 22, 195002),
     [LIST_OF_DUEL[3]]
     ],
         ]



TOURNOIS_LIST = [

    ['The Wars', 'Paris',
     ['Tom', 'JOSEPH', '04/06/2027', 'm', '1'],
     ['Kerry', 'JOSEPH', '04/06/2027', 'm', '2'],
     ['Jess', 'JOSEPH', '04/06/2027', 'm', '3'],
     ['Linda', 'JOSEPH', '04/06/2027', 'm', '4'],
     ['Max', 'JOSEPH', '04/06/2027', 'm', '5'],
     ['Gerald', 'JOSEPH', '04/06/2027', 'm', '6'],
     ['Sabine', 'JOSEPH', '04/06/2027', 'm', '7'],
     ['Oscar', 'JOSEPH', '04/06/2027', 'm', '8'],
     'un bullet', 'RAS', datetime.datetime(2022, 8, 10, 14, 25, 22, 195002), 4, [LIST_ROUNDS]],


    ['Armagedon', 'New-York',

                 [['Tom', 'JOSEPH', '04/06/2027', 'm', '1'],
    ['Kerry', 'JOSEPH', '04/06/2027', 'm', '2'],
    ['Jess', 'JOSEPH', '04/06/2027', 'm', '3'],
    ['Linda', 'JOSEPH', '04/06/2027', 'm', '4'],
    ['Max', 'JOSEPH', '04/06/2027', 'm', '5'],
    ['Gerald', 'JOSEPH', '04/06/2027', 'm', '6'],
    ['Sabine', 'JOSEPH', '04/06/2027', 'm', '7'],
    ['Oscar', 'JOSEPH', '04/06/2027', 'm', '8']],
                 'un bullet', 'RAS',
                 datetime.datetime(2022, 8, 11, 20, 25, 22, 195001), 4, [LIST_ROUNDS]]]


class Player:

    def __init__(self, prenom, nom, date_naissance, genre, classement):
        self.prenom = prenom
        self.nom = nom
        self.date_naissance = date_naissance
        self.genre  = genre
        self.classement = classement


    def save(self):
        list_player = []
        list_player.append(self.prenom)
        list_player.append(self.nom)
        list_player.append(self.date_naissance)
        list_player.append(self.genre)
        list_player.append(self.classement)
        PLAYER_SUBSCRIBED.append(list_player)

        return list_player



class Tournois():

    def __init__(self, nom=None,
                 lieu=None,
                 joueurs=[],
                 temps=None,
                 description=None,
                 date=datetime.datetime.now(),
                 nombre_tours=4, tournees=[]):

        self.nom = nom
        self.lieu = lieu
        self.joueurs = joueurs
        self.temps = temps
        self.description = description
        self.date = date
        self.nombre_tours = nombre_tours
        self.tournees = tournees

    def make_tournament(self):

        def add_player_tournament():
            print("                                       ")
            print("-------------------------------------------------- ")
            print("Ajouter des joueurs")
            print("-------------------------------------------------- ")
            print("                                       ")

            quantite = 0
            for item in PLAYER_SUBSCRIBED:
                quantite += 1
                print(quantite, ".", item[0], item[1])

            print("")

            joueurs_preselect = []
            nb_players = 8

            while nb_players > 0:
                player_subscribe = input('Inscrivez un joueur en renseignant son numéro parmi la liste : ')

                if int(player_subscribe) <= len(PLAYER_SUBSCRIBED) + 1 and int(player_subscribe) > 0:
                    self.joueurs.append(PLAYER_SUBSCRIBED[int(player_subscribe) - 1])
                    nb_players -= 1
                    print("-------------------------------------------------- ")
                    print(PLAYER_SUBSCRIBED[int(player_subscribe) - 1][0], "est inscrit !")
                    print(nb_players)

                else:
                    print("-------------------------------------------------- ")
                    response = self.display.get_input('Votre choix est incorrect, réessayez')
            else:
                print("Tous les joueurs sont inscrits pour ce tournois")
                self.save()
            print('Le Tournoi  a bien a bien été créé, retour au menu précédent')
        self.nom = input('Renseignez le Nom du Tournoi : ')
        self.lieu = input('Renseignez le Lieu du Tournoi : ')
        self.temps = input('Chosissez votre coup | "un bullet", "un blitz" ou un "coup rapide" : ')
        self.description = input('Renseignez les Remarques sur le Tournoi : ')
        self.joueurs = add_player_tournament()


    def save(self):
        item_tournois = []
        item_tournois.append(self.nom)
        item_tournois.append(self.lieu)
        item_tournois.append(self.joueurs)
        item_tournois.append(self.temps)
        item_tournois.append(self.description)
        item_tournois.append(self.date)
        item_tournois.append(self.nombre_tours)
        item_tournois.append(self.tournees)

        TOURNOIS_LIST.append(item_tournois)

        return item_tournois
        pass