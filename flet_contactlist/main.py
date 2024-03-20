# Write a Flet Python application for a contact manager application that has the ability the add, delete and see all the contacts.
# The contacts should be listed by the name of the person. On clicking the contact in the list, it should show the address, city and mobile number of the person.

import flet as ft
from flet import (
    Checkbox,
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
    TextButton
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
                    title=Text(self.contact.address),
                    subtitle=Text(self.contact.address),
                ),
                ListTile(
                    leading=IconButton(icon=icons.PHONE),
                    title=Text(self.contact.mobile),
                ),
            ]
        )


class AddContact(UserControl):
    def __init__(self, contact_dict):
        print("reach here 1")
        self.contact_dict = contact_dict

    def build(self):
        self.name = TextField(label="Name", icon=icons.PERSON)
        self.address = TextField(label="Address", icon=icons.LOCATION_CITY)
        self.city = TextField(label="City", icon=icons.LOCATION_CITY)
        self.mobile = TextField(label="Mobile", icon=icons.PHONE)
        self.submit_button = TextButton(text="Submit", on_click=self.add_contact)
        return Column(
            [
                self.name,
                self.address,
                self.city,
                self.mobile,
                self.submit_button
            ]
        )

    def add_contact(self, e):
        name = self.name.value
        address = self.address.value
        city = self.city.value
        mobile = self.mobile.value
        self.contact_dict[name] = Contact(name, address, city, mobile)
        self.page.add(ExpansionTile(title=name, controls=[DisplayContact(self.contact_dict[name])]))
        self.name.value = ""
        self.address.value = ""
        self.city.value = ""
        self.mobile.value = ""
        self.update()


def main(page: Page):
    page.title = "ToDo App"
    contacts_dict = {
                    "Angel Hogan": Contact("Angel Hogan", "Chapel St. 368 ", "Clearwater", "0311 1823993"),
                    "Felicia Patton": Contact("Felicia Patton", "Annadale Lane 2", "Knoxville", "0368 1244494"),
                    "Geraldine Mccoy": Contact("Geraldine Mccoy", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    "Gretchen Little": Contact("Gretchen Little", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    }

    def close_dlg(e):
        add_dialog.open = False
        page.update()

    add_dialog = ft.AlertDialog(
                                modal=True,
                                title=ft.Text("Add new contact"),
                                content=AddContact(contacts_dict),
                                actions=[
                                    ft.TextButton("Cancel", on_click=close_dlg),
                                ],
                                actions_alignment=ft.MainAxisAlignment.END,
                                on_dismiss=lambda e: print("Modal dialog dismissed!"),
                                )

    def add_pressed(e):
        page.dialog = add_dialog
        add_dialog.open = True
        page.update()

    page.floating_action_button = ft.FloatingActionButton(
        icon=ft.icons.ADD, on_click=add_pressed, bgcolor=ft.colors.LIME_300
    )

    # add the contact namees to the list view
    for key in contacts_dict.keys():
        # shyam was passing just contact.name and it errored with `AttributeError: 'str' object has no attribute '_build_add_commands'``
        page.add(ExpansionTile(title=Text(key), controls=[DisplayContact(contacts_dict[key])]))


ft.app(target=main)
