from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.properties import ListProperty, StringProperty, NumericProperty
# from kivy.lang import Builder
# from kivymd.uix.button import (
#     MDButton,
# )

# Floatingactionbutton is by default in Flet. A custom implementation is needed for Kivy. See .kv file

# canvas gives the idea of point, but its basically a container of all the widgets


class FloatButton(MDFloatLayout):
    def on_press(self):
        print('Floating button pressed')


class Contact:
    def __init__(self, name, address, city, mobile):
        self.name = name
        self.address = address
        self.city = city
        self.mobile = mobile


class ContactView(MDBoxLayout):
    name = StringProperty()
    address = StringProperty()
    city = StringProperty()
    mobile = StringProperty()


class ContactListItem(MDBoxLayout):
    name = StringProperty()
    address = StringProperty()
    city = StringProperty()
    mobile = StringProperty()


# creating the root widget used in .kv file
class MainWindow(MDBoxLayout):
    data = ListProperty()


# creating the App class in which name
# .kv file is to be named main.kv
class ContactManager(MDApp):
    def __init__(self, **kwargs):
        super(ContactManager, self).__init__(**kwargs)
        self.contacts_dict = {
                    "Angel Hogan": Contact("Angel Hogan", "Chapel St. 368 ", "Clearwater", "0311 1823993"),
                    "Felicia Patton": Contact("Felicia Patton", "Annadale Lane 2", "Knoxville", "0368 1244494"),
                    "Geraldine Mccoy": Contact("Geraldine Mccoy", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    "Gretchen Little": Contact("Gretchen Little", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    }

    # defining build()
    def build(self):
        # returning the instance of root class
        # Builder.load_file('contactmanager.kv')
        MainWindow.data = [{'name': contact.name, 'address': contact.address, "city": contact.city, "mobile": contact.mobile}
                           for contact in self.contacts_dict.values()]
        return MainWindow()

    def display_contact(self, name):
        contact = self.contacts_dict[name]


# run the app
if __name__ == '__main__':
    ContactManager().run()