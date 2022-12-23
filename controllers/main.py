from views.display import Display
from models.all import Player, PLAYER_SUBSCRIBED, TOURNOIS_LIST, LIST_OF_DUEL, LIST_ROUNDS



class MainController:


    def __init__(self):
        self.display = Display()

    def main(self):
        self.display.affiche("                                       ")
        self.display.affiche("-------------------------------------------------- ")
        self.display.affiche("BIENVENUE : Faites votre choix ")
        self.display.affiche("-------------------------------------------------- ")
        self.display.affiche("                                       ")

        menu = ["Gestion des Joueurs", "Gestion des Tournois", "Visualiser les Rapports", "Sauvegarder / Charger les données", "Quitter"]
        self.display.affiche_menu(menu)
        self.display.affiche("                                       ")
        response = self.display.get_input('Choisissez parmis les propositions (de 1 à 5) : ', "number")



        while response != len(menu):
            #print(response, len(menu), response != len(menu))

            if (response == 1):
                PlayerController().menu_players()

            elif (response == 2):
                TournoisController().menu_tournois()

            elif (response == 3):
                RapportController().menu_rapports()

            elif (response == 4):
                SaveController().menu_save()

            elif (response == 5):
                exit()

            else:
                self.display.affiche("-------------------------------------------------- ")
                response = self.display.get_input('Votre choix est incorrect, réessayez : ', "number")


# Gestion des joueurs
class PlayerController:

    def __init__(self):
        self.display = Display()


    def menu_players(self):
        
        self.display.affiche("                                       ")
        self.display.affiche("-------------------------------------------------- ")
        self.display.affiche("Voici le menu des joueurs")
        self.display.affiche("-------------------------------------------------- ")
        self.display.affiche("                                       ")

        menu = ["Créer un Joueur", "Supprimer un Joueur", "Voir la Liste des Joueurs", "Mettre à jour le classement d'un Joueur","Retour"]
        self.display.affiche_menu(menu)
        self.display.affiche("                                       ")
        response = self.display.get_input('Choisissez un chiffre pour aller sur le menu de votre choix :  ', 'number')


        while response != len(menu):


            if (response == 1):
                PlayerController().create_player()

            elif (response == 2):
                PlayerController().delete_player()

            elif (response == 3):
                TournoisController().menu_tournois()

            elif (response == 4):
                RapportController().menu_rapports()

            elif (response == 5):
                SaveController().menu_save()

            elif (response == 6):
                exit()

            else:
                self.display.affiche("-------------------------------------------------- ")
                response = self.display.get_input('Votre choix est incorrect, réessayez : ', "number")


    def create_player(self):

        self.display.affiche("                                       ")
        self.display.affiche("-------------------------------------------------- ")
        self.display.affiche("Ajout d'un nouveau joueur")
        self.display.affiche("-------------------------------------------------- ")
        self.display.affiche("                                       ")
        self.display.affiche("                                       ")


        prenom = input(f'Ajoutez le prénom du joueur : ')
        nom = input('Ajoutez le nom joueur n°1 : ')
        date_naissance = input('Ajoutez la date de naissance du joueur jj/mm/aaaa : ')
        genre = input('Ajoutez le genre du joueur ("m"/"f") : ')
        classement = input('Ajoutez le classement du joueur : ')

        player = Player(prenom, nom, date_naissance, genre, classement)
        self.display.affiche("                                       ")
        print(player.save())

        self.display.affiche("                                       ")
        self.display.affiche("                                       ")
        self.display.affiche("*********************************************************")
        self.display.affiche(f'Le nouveau joueur {player.prenom} {player.nom} est ajouté avec succès ! ')
        self.display.affiche("*********************************************************")
        self.menu_players()

    def delete_player(self):

        if len(PLAYER_SUBSCRIBED) == 0:
            print("")
            print("Il n'y a pas de joueurs à supprimer")
            print("")

        else:
            self.display.affiche("                                       ")
            quantite = 0

            for item in PLAYER_SUBSCRIBED:
                quantite += 1
                print(quantite, ".", item[0], item[1], f' | classement : {item[-1]}')
            self.display.affiche("                                       ")
            self.display.affiche("                                       ")

            response = self.display.get_input('Choisissez le bon numéro pour supprimer le joueur de votre choix :  ',
                                              'number')

            if response > quantite:
                print("")
                print("Ce numéro de joueurs n'existe pas !  Retour au menu.")
                print("")

            else:
                deleting = PLAYER_SUBSCRIBED.pop(response - 1)
                print("")
                print("Le joueur a été supprimé ! ")
                print("")

            PlayerController().menu_players()
