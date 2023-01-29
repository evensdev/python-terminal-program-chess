class Display:

    def affiche(self, message):
        print(message)

    def affiche_menu(self, list):
        index = 1
        for choice in list:
            print(index, " - ", choice)
            index += 1

    def get_input(self, message, format):
        if format == 'number':
            response = input(message)
            try:
                return int(response)

            except ValueError:
                print('mauvais format : ', format)
                self.get_input(message, format)

        if format == 'string':
            response = input(message)
