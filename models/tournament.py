from tinydb import TinyDB, Query, where
from views.display import Display
from models.players import PLAYER_SUBSCRIBED
import datetime
import ast

# Base de données
db = TinyDB('db.json')
chess = db.table('chess')

LIST_ROUNDS = []
TOURNOIS_LIST = []

class Rounds:
    def __init__(self,
                 start = datetime.datetime.now(),
                 end = str(),
                 matches = []):

        self.start = str(datetime.datetime.now())
        self.end = str(datetime.datetime.now())
        self.matches = matches

    # initialiser le 1er round quand le tournoi est créé
    def initialize_round(self):


        #######    Ajout d'informations sur le round


        launch_round = []
        launch_round.append("Round n°" + str(len(LIST_ROUNDS) + 1))
        launch_round.append(str(self.start))
        launch_round.append(None)
        launch_round.append(self.matches)
        LIST_ROUNDS.append(launch_round)




        #######   add player subscribed in list


        list_player = []
        for item in TOURNOIS_LIST[-1][2]:
            list_player.append(item)


        #######   function to divide list of players subscribed in 2 lists


        def split_list(list_player):
            half = len(list_player) // 2

            first_list = list_player[:half]
            second_list = list_player[half:]

            zip(first_list, second_list)
            print(zip(first_list, second_list))

            # créer des paires de match avec la fonction zip
            return list(zip(first_list, second_list))

        list_of_match = split_list(list_player)



        #######  définir les matchs pour le round à partir de la liste


        def match_for_round():

            numero_paire = 0

            for match in list_of_match:
                numero_paire += 1
                duel = []
                joueur_1 = []
                joueur_2 = []

                joueur_1.append(match[0][0])
                joueur_1.append(0)

                joueur_2.append(match[1][0])
                joueur_2.append(0)

                duel.append(joueur_1)
                duel.append(joueur_2)

                self.matches.append(duel)

                print(f'Paire n°: {numero_paire}', ".", match[0][0], " VS ", match[1][0])

        match_for_round()


        ######    Display information about round

        print("")
        print("")
        #print(LIST_ROUNDS[-1][3])
        print("")


    ######  Créer un nouveau round

    def new_round(self):
        if len(LIST_ROUNDS) < 4 :

            if LIST_ROUNDS[-1][2] == None:
                print("")
                print("")
                print("Vous n'avez pas mis à jour les résultats du précédent round")
                print("Veuillez mettre à jour les scores en tapant sur la touche n°3")
                print("")
                print("")

            else:

                TOURNOIS_LIST[-1][-2] += 1

                if len(LIST_ROUNDS) < 2:

                    print("OPTION 1")
                    ranking_round = []

                    for item in LIST_ROUNDS[-1][3]:

                        for player in item:
                            ranking_round.append(player)

                    ranking_round = sorted(ranking_round, key=lambda ranking: ranking[-1], reverse=True)


                    def split_list(list_player):
                        half = len(list_player) // 2

                        first_list = list_player[:half]

                        second_list = list_player[half:]

                        zip(first_list, second_list)

                        print(zip(first_list, second_list))

                        # créer des paires de match avec la fonction zip
                        return list(zip(first_list, second_list))



                    second_round = split_list(ranking_round)

                    print(second_round)

                    # Enregistrer le round dans la liste


                    launch_round = []
                    launch_round.append("Round numero " + str(len(LIST_ROUNDS) + 1))
                    launch_round.append(str(self.start))
                    launch_round.append(None)
                    launch_round.append(second_round)
                    LIST_ROUNDS.append(launch_round)

                    print("")
                    print("Le round numero ",len(LIST_ROUNDS), " est prêt")
                    print("Vous pouvez entrer les résultats des nouveaux matchs en sélectionnant la touche 3' ")
                    print("")

                    print(LIST_ROUNDS)

                else :
                    print("OPTION 2")
                    ranking_round = []

                    for item in LIST_ROUNDS[1][3]:

                        for player in item:
                            ranking_round.append(player)

                        ranking_round = sorted(ranking_round, key=lambda ranking: ranking[-1], reverse=True)


                    duel_ready_to_control = []
                    duel_ready_to_control.append([ranking_round[0], ranking_round[1]])
                    duel_ready_to_control.append([ranking_round[2], ranking_round[3]])
                    duel_ready_to_control.append([ranking_round[4], ranking_round[5]])
                    duel_ready_to_control.append([ranking_round[6], ranking_round[7]])

                    launch_round = []
                    launch_round.append("Round numero " + str(len(LIST_ROUNDS) + 1))
                    launch_round.append(None)
                    launch_round.append(None)
                    launch_round.append(duel_ready_to_control)
                    LIST_ROUNDS.append(launch_round)

                    print("")
                    print("Le round n°",len(LIST_ROUNDS), " est prêt")
                    print("Vous pouvez entrer les résultats des nouveaux matchs en sélectionnant la touche 3' ")
                    print("")

                    #return print(LIST_ROUNDS)
        else:
            print("")
            print("Vous avez déjà atteint les 4 rounds et entré les résultats.")
            print("Tapez sur la touche 6 pour clôturer le tournoi ou si c'est déjà fait, vous pouvez créer un nouveau tournoi ! ")
            print("")



    def end_round(self):
        LIST_ROUNDS[-1][2] = datetime.datetime.now()
 
class Tournois():

    def __init__(self, nom=None,
                 lieu=None,
                 joueurs=[],
                 temps=None,
                 description=None,
                 date=str(datetime.datetime.now()),
                 nombre_tours=1, tournees=[]):

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
                player_subscribe = None
                player_subscribe = Display().get_input('Inscrivez un joueur en renseignant son numéro parmi la liste : ', 'number')
                player_subscribe = int(player_subscribe)
                print(type(player_subscribe))

                if player_subscribe < len(PLAYER_SUBSCRIBED):
                    self.joueurs.append(PLAYER_SUBSCRIBED[int(player_subscribe) - 1])
                    nb_players -= 1
                    print("-------------------------------------------------- ")
                    print(PLAYER_SUBSCRIBED[int(player_subscribe) - 1][0], "est inscrit !")
                    print("Il vous reste **",nb_players,"joueurs ** à inscrire")
                    print("")

                else:
                    print("-------------------------------------------------- ")
                    print("Votre choix est incorrect")
                    print("")
            else:
                print("Tous les joueurs sont inscrits pour ce tournoi")
                print('')
                self.save()
            print('Le Tournoi **',TOURNOIS_LIST[-1][0], '** a bien a bien été créé')
            print('')
            print('Voici la liste des matchs du Round n°1')
            print('')



        print("ÉTAPE 1/5 - NOM DU TOURNOI")
        self.nom = input('Renseignez le Nom du Tournoi : ')
        print("ÉTAPE 2/5 - LIEU")
        self.lieu = input('Renseignez le Lieu du Tournoi : ')
        print("ÉTAPE 3/5 - TYPE DE COUP")
        self.temps = input('Chosissez votre coup | "un bullet", "un blitz" ou un "coup rapide" : ')
        print("ÉTAPE 4/5 - DESCRIPTION")
        self.description = input('Renseignez les Remarques sur le Tournoi : ')
        print("ÉTAPE 5/5 - AJOUT DE JOUEURS")
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


    def update_nombre_tours(self):
        self.nombre_tours += 1

    def close_tournament(self):

        print(TOURNOIS_LIST[-1][-2])

        if TOURNOIS_LIST[-1][-2] < 4:
            print("")
            print("Le Tournoi n'est pas encore terminé")
            print("Veuillez compléter tous les rounds afin de clôturer le Tournoi")
            print("")

        else:
            print("")
            print("Le Tournoi est maintenant clôturé !")
            print("Cela signifie que : ")
            print("- Vous ne pourrez plus modifier les résultats du tournoi clôturé")
            print("- Vous ne pourrez plus créer de nouveau round sur le tournoi clôturé")
            print("")

            # Element ci-dessous à effacer après avoir vérifié tournois_list
            print("RECAPITULATIF DE LA TABLE TOURNOIS_LIST")
            print(TOURNOIS_LIST)
            LIST_ROUNDS = []


    def export_data(self):


        # Convert tournois de Liste vers Dictionnaire

        tournois_dict_list = []
        for tournament in TOURNOIS_LIST:
            tournoi = {
                "nom_competition": tournament[0],
                "ville": tournament[1],
                "liste_joueurs": tournament[2],
                "coup": tournament[3],
                "description": tournament[4],
                "date_debut": tournament[5],
                "nb_tour": tournament[6],
                "liste_rounds": tournament[7]
            }
            tournois_dict_list.append(tournoi)

        ##############################################################
        # Convert Rounds  Liste vers Dictionnaire
        def list_to_dict(lst):
            my_dict = {}
            for i, item in enumerate(lst):
                my_dict[i] = item
            return my_dict

        list_to_dict(LIST_ROUNDS)

        ##############################################################
        # Convert Player  Liste vers Dictionnaire
        player_subscribed_dict = {i: player for i, player in enumerate(PLAYER_SUBSCRIBED)}

        tournament_converted = tournois_dict_list[0]
        rounds_converted = list_to_dict(LIST_ROUNDS)
        players_converted = player_subscribed_dict = {i: player for i, player in enumerate(PLAYER_SUBSCRIBED)}

        chess.insert(tournament_converted)
        chess.insert(rounds_converted)
        chess.insert(players_converted)

        ################################################


        print("")
        print("=================================================================")
        print("Votre configuration a bien été sauvegardée en base de données !")
        print("Vous pouvez à tout moment recharger votre dernière sauvegarde")
        print("=================================================================")
        print("")

    def import_data(self):



        # Importation des listes

        tournament_imported = chess.get(doc_id=1)
        rounds_imported = chess.get(doc_id=2)
        players_imported = chess.get(doc_id=3)

        # Test importation

        print(tournament_imported)

        print(type(tournament_imported))

        print("")

        # Test importation
        print(rounds_imported)
        print("")

        # Test importation

        print(players_imported)
        print("")

        ########################################################
        #
        # Convert Round  Dictionnaire vers Liste
        def dict_to_list(d):
            return list(d.values())

        # Convert Player  Dictionnaire  vers Liste
        player_dict_to_list = list(players_imported.values())

        # Convert Tournois de Dictionnaire JSON vers Liste
        tournois_dict_to_list = list(tournament_imported.values())

        print(tournois_dict_to_list)

        #######################################################

        for item in player_dict_to_list:
            PLAYER_SUBSCRIBED.append(item)

        tournois_cache = []
        for item in tournois_dict_to_list:
            tournois_cache.append(item)
        TOURNOIS_LIST.append(tournois_cache)

        for item in dict_to_list(rounds_imported):
            LIST_ROUNDS.append(item)



        ####################

        print("")
        print(PLAYER_SUBSCRIBED)
        print("")
        print(TOURNOIS_LIST)
        print("")
        print(LIST_ROUNDS)

        print("")
        print("=================================================================")
        print("Votre Sauvegarde a bien été Chargé sur ce jeu !")
        print("Vous pouvez retrouver tous les éléments sauvegardés de votre ancienne partie")
        print("=================================================================")
        print("")

        print(type(players_imported))
        print("")

