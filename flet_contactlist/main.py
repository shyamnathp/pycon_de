# Write a Flet Python application for a contact manager application that has the ability the add, delete and see all the contacts.
# The contacts should be listed by the name of the person. On clicking the contact in the list, it should show the address, city and mobile number of the person.

# https://flet.dev/docs/controls/expansiontile/#trailing
#  Icon cross reference does not exits


# https://flet.dev/docs/tutorials/python-todo
# what is the `e` in addclicked(e)

import flet as ft
from flet import (
    Column,
    FloatingActionButton,
    IconButton,
    Page,
    Row,
    TextField,
    UserControl,
    colors,
    icons,
    Text,
    ListTile,
    ExpansionTile,
    ElevatedButton
)


class Contact:
    def __init__(self, name, address, city, mobile):
        self.name = name
        self.address = address
        self.city = city
        self.mobile = mobile


class DisplayContact(UserControl):
    def __init__(self, contact: Contact):
        super().__init__()
        self.contact = contact
        self.name = self.contact.name
        self.address = self.contact.address
        self.city = self.contact.city
        self.mobile = self.contact.mobile

    def build(self):
        return Column(
            [
                ListTile(
                    leading=IconButton(icon=icons.LOCATION_CITY),
                    title=Text(self.contact.address, color=colors.BLACK),
                    subtitle=Text(self.contact.address, color=colors.BLACK),
                ),
                ListTile(
                    leading=IconButton(icon=icons.PHONE),
                    title=Text(self.contact.mobile, color=colors.BLACK),
                ),
            ]
        )


class CustomExpansionTile(UserControl):
    def __init__(self, contact: Contact):
        super().__init__()
        self.contact = contact

    def build(self):
        expansion_tile = ExpansionTile(title=Text(self.contact.name), controls=[DisplayContact(self.contact)],
                                       trailing=IconButton(icons.DELETE_OUTLINE, on_click=self.delete_clicked),
                                       bgcolor=colors.INDIGO_50, text_color=colors.BLACK)
        return expansion_tile

    def delete_clicked(self, e):
        self.page.remove(self)


class AddContact(UserControl):
    def __init__(self, contact_dict):
        super().__init__()
        self.contact_dict = contact_dict

    def build(self):
        self.name = TextField(label="Name", icon=icons.PERSON)
        self.address = TextField(label="Address", icon=icons.LOCATION_CITY)
        self.city = TextField(label="City", icon=icons.LOCATION_CITY)
        self.mobile = TextField(label="Mobile", icon=icons.PHONE)
        submit_button = ElevatedButton(text="Submit", on_click=self.add_contact)
        cancel_button = ElevatedButton(text="Cancel", on_click=self.close_dlg)
        self.submit_cancel_button = Row([submit_button, cancel_button])
        return Column(
            [
                self.name,
                self.address,
                self.city,
                self.mobile,
                self.submit_cancel_button
            ]
        )

    def add_contact(self, e):
        name = self.name.value
        address = self.address.value
        city = self.city.value
        mobile = self.mobile.value
        self.contact_dict[name] = Contact(name, address, city, mobile)
        # passing a str to name gives the error "AttributeError: 'str' object has no attribute '_set_attr_internal'"
        self.page.add(CustomExpansionTile(self.contact_dict[name]))
        self.name.value = ""
        self.address.value = ""
        self.city.value = ""
        self.mobile.value = ""
        self.update()
        self.page.dialog.open = False
        self.page.update()

    def close_dlg(self, e):
        self.page.dialog.open = False
        self.page.update()


def main(page: Page):
    contacts_dict = {
                    "Angel Hogan": Contact("Angel Hogan", "Chapel St. 368 ", "Clearwater", "0311 1823993"),
                    "Felicia Patton": Contact("Felicia Patton", "Annadale Lane 2", "Knoxville", "0368 1244494"),
                    "Geraldine Mccoy": Contact("Geraldine Mccoy", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    "Gretchen Little": Contact("Gretchen Little", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    }
    page.title = "ConactManager App"
    page.appbar = ft.AppBar(title=ft.Text("Contacts"), bgcolor=colors.INDIGO_300)

    add_dialog = ft.AlertDialog(
                                modal=True,
                                title=ft.Text("Add new contact"),
                                content=AddContact(contacts_dict)
                                )

    def add_pressed(e):
        page.dialog = add_dialog
        add_dialog.open = True
        page.update()

    page.floating_action_button = FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_pressed, bgcolor=colors.INDIGO
    )

    # add the contact namees to the list view
    for key in contacts_dict.keys():
        # shyam was passing just contact.name and it errored with `AttributeError: 'str' object has no attribute '_build_add_commands'``
        page.add(CustomExpansionTile(contacts_dict[key]))


ft.app(target=main)
