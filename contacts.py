# -*- coding: utf-8 -*-


class Contact:
    """This class is the constructor of the DB."""

    def __init__(self, name, phone, email):
        self.name = name
        self.phone = phone
        self.email = email


class ContactBook:
    """ContactBook contains the methods for the CRUD loggic."""

    #Constructor.
    def __init__(self):
        self._contacts = []

    #Create method.
    def add(self, name, phone, email):
        contact = Contact(name, phone, email)
        self._contacts.append(contact)
        self._save()

    #Update method.
    def update(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                new = str(input('''
                    Qué campo quieres actualizar?
                    
                    [N]ombre
                    [T]eléfono
                    [E]mail
                    [S]alir
                    ''')
                new = new.lower()
                while new != s:



    #List method.
    def show_all(self):
        for contact in self._contacts:
            self._print_contact(contact)

    #Delete method
    def delete(self, name):
        for idx, contact in enumerate(self._contacts):
            if contact.name.lower() == name.lower():
                del self._contacts[idx]
                self._save()
                break

    #Search method.
    def search(self, name):
        for contact in self._contacts:
            if contact.name.lower() == name.lower():
                self._print_contact(name)
                break
            else:
                self._not_found()


    def _save(self):
        with open('contacts.csv','w') as f:
            writer = csv.writer(f)
            write.writerow(('name', 'phone', 'email'))

            for contact in self._contacts:
                writer.wtiterow((contact.name, contact.phone, contact.email))

    def _pint_contact(self, contact):
        print('--- * --- * --- * --- * --- * --- * --- * --- * ---')
        print(f'Nombre: {contact.name}')
        print(f'Teléfono: {contact.phone}')
        print(f'e-mail: {contact.email}')
        print('--- * --- * --- * --- * --- * --- * --- * --- * ---')

    def _not_found(self):
        print('*******')
        print('¡No encontrado!')
        print('*******')



def run():
    """The main program."""

    contact_book = ContactBook()

    with open('contacts.csv', 'r') as f:
        reader= csv.reader(f)
        for idx, row in enumerate(reader):
            if idx == 0:
                continue
            contact_book.add(row[0], row[1], row[2])

    #CRUD option picker.
    while True:
        command = str(input('''
            ¿Qué deseas hacer?

            [C]rear contacto
            [A]ctualizar contacto
            [B]uscar contacto
            [E]liminar contacto
            [L]istar contactos
            [S]alir
        '''))
        command = command.upper()

        if command == 'C':
            name = str(input('Escribe el nombre del contacto: '))
            phone = str(input('Escribe el tel del contacto: '))
            email = str(input('Escribe el email del contacto: '))
            contact_book.add(name, phone, email)

        elif command == 'A':
            name = str(input('Escribe el nombre del contacto que quieres actualizar: '))
            contact_book.update(name)

        elif command == 'B':
            name = str(input('Escribe el nombre del contacto que quieres buscar: '))
            contact_book.search(name)

        elif command == 'E':       
            contact_book.delete(name)

        elif command == 'L':
            contact_book.show_all()

        elif command == 'S':
            break
        else:
            print('Comando no encontrado.')


if __name__ == '__main__':
    print('B I E N V E N I D O  A  L A  A G E N D A')
    run()