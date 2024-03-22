from kivy.uix.accordion import Accordion, AccordionItem
from kivy.uix.label import Label
from kivy.app import App
from kivy.lang import Builder

class CustomLabel(Label):
    pass

Builder.load_string('''
[CustomAccordionItemTitle@CustomLabel]:
    text: ctx.title
    normal_background: ctx.item.background_normal if ctx.item.collapse else ctx.item.background_selected
    disabled_background: ctx.item.background_disabled_normal if ctx.item.collapse else ctx.item.background_disabled_selected
    canvas.before:
        Color:
            rgba: self.disabled_color if self.disabled else self.color
        BorderImage:
            source: self.disabled_background if self.disabled else self.normal_background
            pos: self.pos
            size: self.size
        PushMatrix
        Translate:
            xy: self.center_x, self.center_y
        Rotate:
            angle: 90 if ctx.item.orientation == 'horizontal' else 0
            axis: 0, 0, 1
        Translate:
            xy: -self.center_x, -self.center_y
    canvas.after:
        PopMatrix
''')


class Contact:
    def __init__(self, name, address, city, mobile):
        self.name = name
        self.address = address
        self.city = city
        self.mobile = mobile


class AccordionApp(App):
    def __init__(self):
        super().__init__()
        self.contacts_dict = {
                    "Angel Hogan": Contact("Angel Hogan", "Chapel St. 368 ", "Clearwater", "0311 1823993"),
                    "Felicia Patton": Contact("Felicia Patton", "Annadale Lane 2", "Knoxville", "0368 1244494"),
                    "Geraldine Mccoy": Contact("Geraldine Mccoy", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    "Gretchen Little": Contact("Gretchen Little", "Cedar St. 3", "Baltimore", "0311 1823993"),
                    }

    def build(self):
        root = Accordion(orientation='vertical')
        for contact_name, contact in self.contacts_dict.items():
            # when collapsed is passed, it erros with
            #  TypeError: Properties ['collapsed'] passed to __init__ may not be existing property names.
            # Valid properties are ['accordion', 'background_disabled_normal', 'background_disabled_selected', 'background_normal', 'background_selected', 'center', 'center_x', 'center_y', 'children', 'cls', 'collapse', 'collapse_alpha', 'container', 'container_title', 'content_size', 'disabled', 'height', 'ids', 'min_space', 'motion_filter', 'opacity', 'orientation', 'parent', 'pos', 'pos_hint', 'right', 'size', 'size_hint', 'size_hint_max', 'size_hint_max_x', 'size_hint_max_y', 'size_hint_min', 'size_hint_min_x', 'size_hint_min_y', 'size_hint_x', 'size_hint_y', 'title', 'title_args', 'title_template', 'top', 'width', 'x', 'y']

            # what shoudl be the type of title_template?
            #      raise Exception('Unknown <%s> template name' % name)
            #  Exception: Unknown </home/shyamnath/Shyam/pycon_de/kivy_contactlist/custom_accordian_style.kv> template name
            item = AccordionItem(title=contact_name, title_template="CustomAccordionItemTitle")
            item.add_widget(Label(text=f"{contact.name}\n{contact.address}\n{contact.city}\n{contact.mobile}\n"))
            root.add_widget(item)
        return root


if __name__ == '__main__':
    AccordionApp().run()