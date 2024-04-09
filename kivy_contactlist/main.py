from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.app import MDApp
from kivy.properties import ListProperty, StringProperty, NumericProperty
from kivy.uix.screenmanager import ScreenManager, Screen, SlideTransition
from kivymd.uix.dialog import MDDialog
from kivymd.uix.button import MDFlatButton
# couple of examples are broken in KivyMD
from kivymd.uix.expansionpanel import MDExpansionPanel, MDExpansionPanelOneLine
from kivy.core.window import Window

# Floatingactionbutton is by default in Flet. A custom implementation is needed for Kivy. See .kv file
# canvas gives the idea of point, but its basically a container of all the widgets


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

class AddContactContent(MDBoxLayout):
    pass

# creating the App class in which name
# .kv file is to be named main.kv
class ContactManager(MDApp):
    dialog = None

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
        self.theme_cls.theme_style = "Dark"
        Window.bind(on_keyboard=self.adjust_dialog_position)
        self.main_window = MainWindow()
        self.main_window.data = [{'name': contact.name, 'address': contact.address, "city": contact.city, "mobile": contact.mobile}
                                 for contact in self.contacts_dict.values()]
        # self.transition = SlideTransition(duration=.35)
        # self.root = ScreenManager(transition=self.transition)
        # self.root.add_widget(self.main_window)
        return self.main_window

    def adjust_dialog_position(self, window, keyboard_height, *args):
        if keyboard_height > 0:
            # If the keyboard is visible, move the dialog up
            if self.dialog:
                self.dialog.pos_hint = {"center_y": 0.5 + keyboard_height / Window.height}
        else:
            # If the keyboard is not visible, center the dialog
            if self.dialog:
                self.dialog.pos_hint = {"center_y": 0.5}

    def on_start(self):
        for contact in self.contacts_dict.values():
            # Note: Having a delete button is a hard task
            self.main_window.ids.contact_list.add_widget(MDExpansionPanel(icon="account",
                                                                          content=ContactView(name=contact.name, address=contact.address, city=contact.city, mobile=contact.mobile),
                                                                          panel_cls=MDExpansionPanelOneLine(text=contact.name)))

    def add_contact_dialog(self):
        self.dialog = MDDialog(title="Add Contact",
                          type="custom",
                          content_cls=AddContactContent(),
                          buttons=[
                                MDFlatButton(
                                    text="CANCEL",
                                    theme_text_color="Custom",
                                    text_color=self.theme_cls.primary_color,
                                    on_release=lambda x: self.dialog.dismiss()
                                ),
                                MDFlatButton(
                                    text="OK",
                                    theme_text_color="Custom",
                                    text_color=self.theme_cls.primary_color,
                                    on_release=lambda x: self.add_contact()
                                ),
                            ],
                         )
        self.dialog.open()


# run the app
if __name__ == '__main__':
    ContactManager().run()