from tinydb import TinyDB, Query, where
import datetime
import ast

# Base de données
db = TinyDB('db.json')
chess = db.table('chess')


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

LIST_ROUNDS = []


# this List is full because testing, but the true version will be empty
TOURNOIS_LIST = [['Al Nasser', 'Paris',
                  [['Evens', 'JOSEPH', '13/06/1991', 'm', '1'],
                   ['Elodie', 'JOSEPH', '28/11/1981', 'f', '2'],
                   ['Nina', 'JOSEPH', '02/03/2023', 'f', '3'],
                   ['Kylian', 'JOSEPH', '02/03/2023', 'm', '4'],
                   ['Clara', 'JOSEPH', '02/03/2023', 'f', '5'],
                   ['Chelsea', 'JOSEPH', '12/05/2025', 'f', '6'],
                   ['Seven', 'JOSEPH', '12/05/2025', 'f', '7'],
                   ['Elohim', 'JOSEPH', '04/06/2027', 'm', '8']],
                  'bullet', 'RA', 'datetime.datetime(2023, 1, 21, 19, 11, 11, 627838)', 4,
                  [['Round n°1', '2023-01-21 19:11:26.350058', 'datetime.datetime(2023, 1, 21, 19, 11, 36, 147457)',
                    [[['Evens', 4], ['Clara', 1]], [['Elodie', 0], ['Chelsea', 2]],
                     [['Nina', 1], ['Seven', 2]], [['Kylian', 2], ['Elohim', 3]]]],
                   ['Round n°2', '2023-01-21 19:11:43.397692', 'datetime.datetime(2023, 1, 21, 19, 11, 47, 349600)',
                    [(['Evens', 4], ['Elodie', 0]), (['Seven', 2], ['Chelsea', 2]),
                     (['Kylian', 2], ['Nina', 1]), (['Clara', 1], ['Elohim', 3])]],
                   ['Round n°3', None, 'datetime.datetime(2023, 1, 21, 19, 11, 55, 29699)',
                    [[['Evens', 4], ['Kylian', 2]], [['Seven', 2], ['Chelsea', 2]], [['Elohim', 3], ['Elodie', 0]],
                     [['Nina', 1], ['Clara', 1]]]],
                   ['Round n°4', None, 'datetime.datetime(2023, 1, 21, 19, 12, 6, 201584)',
                    [[['Evens', 4], ['Chelsea', 2]], [['Kylian', 2], ['Elohim', 3]], [['Seven', 2], ['Clara', 1]], [['Elodie', 0], ['Nina', 1]]]]]],
                 ['American Express', 'Paris',
                  [['Evens', 'JOSEPH', '13/06/1991', 'm', '1'],
                   ['Elodie', 'JOSEPH', '28/11/1981', 'f', '2'],
                   ['Nina', 'JOSEPH', '02/03/2023', 'f', '3'],
                   ['Kylian', 'JOSEPH', '02/03/2023', 'm', '4'],
                   ['Clara', 'JOSEPH', '02/03/2023', 'f', '5'],
                   ['Chelsea', 'JOSEPH', '12/05/2025', 'f', '6'],
                   ['Seven', 'JOSEPH', '12/05/2025', 'f', '7'],
                   ['Elohim', 'JOSEPH', '04/06/2027', 'm', '8']],
                  'bullet', 'RA', 'datetime.datetime(2023, 1, 21, 19, 11, 11, 627838)', 4,
                  [['Round n°1', '2023-01-21 19:11:26.350058', 'datetime.datetime(2023, 1, 21, 19, 11, 36, 147457)',
                    [[['Evens', 4], ['Clara', 1]], [['Elodie', 0], ['Chelsea', 2]],
                     [['Nina', 1], ['Seven', 2]], [['Kylian', 2], ['Elohim', 3]]]],
                   ['Round n°2', '2023-01-21 19:11:43.397692', 'datetime.datetime(2023, 1, 21, 19, 11, 47, 349600)',
                    [(['Evens', 4], ['Elodie', 0]), (['Seven', 2], ['Chelsea', 2]),
                     (['Kylian', 2], ['Nina', 1]), (['Clara', 1], ['Elohim', 3])]],
                   ['Round n°3', None, 'datetime.datetime(2023, 1, 21, 19, 11, 55, 29699)',
                    [[['Evens', 4], ['Kylian', 2]], [['Seven', 2], ['Chelsea', 2]], [['Elohim', 3], ['Elodie', 0]],
                     [['Nina', 1], ['Clara', 1]]]],
                   ['Round n°4', None, 'datetime.datetime(2023, 1, 21, 19, 12, 6, 201584)',
                    [[['Evens', 4], ['Chelsea', 2]], [['Kylian', 2], ['Elohim', 3]], [['Seven', 2], ['Clara', 1]],
                     [['Elodie', 0], ['Chantal', 1]]]]]]
                 ]



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


    def save(self):

        item_round = []
        item_round.append(self.start)
        item_round.append(self.end)
        item_round.append(self.matches)
        LIST_ROUNDS.append(item_round)
        #return item_round
        pass


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
                print("Tous les joueurs sont inscrits pour ce tournoi")
                print('')
                self.save()
            print('Le Tournoi  a bien a bien été créé')
            print('')
            print('Voici la liste des matchs du Round n°1')
            print('')

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

        ################################################
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
        print(type(tournament_imported))
        print("")

        # Test importation
        print(rounds_imported)
        print("")

        # Test importation
        print(type(players_imported))
        print("")

        # fonction de conversion


