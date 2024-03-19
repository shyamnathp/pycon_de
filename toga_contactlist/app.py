import toga
from toga.style import Pack
from toga.style.pack import COLUMN
from toga import (
    Button,
    TextInput,
    DetailedList,
    Selection
)


class Contact:
    def __init__(self, name, address, city, mobile):
        self.name = name
        self.address = address
        self.city = city
        self.mobile = mobile


class ContactManager(toga.App):
    def startup(self):
        print("startup is called")
        self.contacts = {
                        "A": [Contact("Angel Hogan", "Chapel St. 368 ", "Clearwater", "0311 1823993")],
                        "F": [Contact("Felicia Patton", "Annadale Lane 2", "Knoxville", "0368 1244494")],
                        "G": [Contact("Geraldine Mccoy", "Cedar St. 3", "Baltimore", "0311 1823993"), Contact("Gretchen Little", "Cedar St. 3", "Baltimore", "0311 1823993")],
                        }

        # Main box containing the contact management interface
        main_box = toga.Box(style=Pack(direction=COLUMN, padding=10))

        # Box for input fields
        input_box = toga.Box(style=Pack(direction=COLUMN, padding=(0, 0, 10, 0)))

        self.name_input = TextInput(placeholder='Name')
        self.address_input = TextInput(placeholder='Address')
        self.city_input = TextInput(placeholder='City')
        self.mobile_input = TextInput(placeholder='Mobile')

        # Button to add a new contact
        add_button = Button('Add', on_press=self.add_contact)
        temp_data = [
                    {"name": contact, "address": contact.address, "city": contact.city}
                    for key in self.contacts.keys()
                    for contact in self.contacts[key]
                    ]

        # Detailed list to display contacts
        self.contact_list = DetailedList(
            accessors=["name", "address", "city", ],
            data=[
                {"name": contact.name, "address": contact.address, "city": contact.city}
                for key in self.contacts.keys()
                for contact in self.contacts[key]
            ],
            on_select=self.display_contact_details,
            missing_value="Missing",
            style=Pack(flex=1),
        )

        # Box for list
        list_box = toga.Box(style=Pack(padding=(0, 10)))
        list_box.add(self.contact_list)

        # Add widgets to input box
        input_box.add(self.name_input)
        input_box.add(self.address_input)
        input_box.add(self.city_input)
        input_box.add(self.mobile_input)
        input_box.add(add_button)

        # Add input and list boxes to main box
        main_box.add(input_box)
        main_box.add(list_box)

        # Create the main window
        self.main_window = toga.MainWindow(title=self.formal_name)
        self.main_window.content = main_box
        self.main_window.show()

    def add_contact(self, widget):
        name = self.name_input.value.strip()
        address = self.address_input.value.strip()
        city = self.city_input.value.strip()
        mobile = self.mobile_input.value.strip()

        if name and address and city and mobile:
            contact = Contact(name, address, city, mobile)
            first_letter = name[0].upper()
            if first_letter not in self.contacts:
                self.contacts[first_letter] = []
            self.contacts[first_letter].append(contact)
            self.update_contact_list()
            self.name_input.value = ''
            self.address_input.value = ''
            self.city_input.value = ''
            self.mobile_input.value = ''
        else:
            self.main_window.info_dialog(
                'Error',
                'Please enter all contact details.'
            )

    def display_contact_details(self, widget, **kwargs):
        if widget.selection is not None:
            contact = widget.selection
            self.main_window.info_dialog(
                'Contact Details',
                f'Name: {contact.name}\nAddress: {contact.address}\nCity: {contact.city}'
            )

    def update_contact_list(self):
        contact_data = []
        for letter, contacts in sorted(self.contacts.items()):
            contact_data.append(Selection(letter))
            for contact in contacts:
                contact_data.append(Selection(contact, parent=letter))
        self.contact_list.data = contact_data


def main():
    return ContactManager("ContactsList", "org.shyam.app.contactlist")


if __name__ == '__main__':
    app = main()
    app.main_loop()
