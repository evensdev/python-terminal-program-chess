from tinydb import TinyDB, Query, where
import datetime
import ast

# Base de données
db = TinyDB('db.json')
chess = db.table('chess')

PLAYER_SUBSCRIBED = []


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
