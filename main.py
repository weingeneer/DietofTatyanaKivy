__version__ = '0.2.5'

from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.screen import MDScreen
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.icon_definitions import md_icons
import random

# Window.size = (1080, 2400)
Window.size = (270, 600)

KV = '''
<ContentNavigationDrawer>

    orientation: "vertical"
    padding: "8dp"
    spacing: "8dp"

    AnchorLayout:
        anchor_x: "left"
        size_hint_y: None
        height: avatar.height

        Image:
            id: avatar
            size_hint: None, None
            size: "56dp", "56dp"
            source: "data/logo/logo_light.jpg"

    MDLabel:
        text: app.title
        font_style: "Button"
        size_hint_y: None
        height: self.texture_size[1]

    MDLabel:
        text: app.by_who
        font_style: "Caption"
        size_hint_y: None
        height: self.texture_size[1]

    ScrollView:

        MDList:

            OneLineListItem:
                text: "Что приготовить?"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 1"

            OneLineListItem:
                text: "История"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "scr 2"

MDScreen:
    soup: soup_id
    dish: dish_id

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "scr 1"

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Доверься случаю!"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)

                        Tab:
                            id: tab1
                            title: 'Первое'
                            icon: ''

                            MDBoxLayout:
                                padding: [20, 100, 20, 60]
                                orientation: 'vertical'

                                MDFillRoundFlatButton:
                                    text: 'Cуп'
                                    size_hint: 1.0, 1.0
                                    on_release: app.click_soup()

                                MDLabel:
                                    id: soup_id
                                    text: 'Случай не использован'
                                    halign: 'center'

                        Tab:
                            id: tab2
                            title: 'Второе'
                            icon: ''

                            MDBoxLayout:
                                padding: [20, 100, 20, 60]
                                orientation: 'vertical'

                                MDFillRoundFlatButton:
                                    text: 'Второе'
                                    size_hint: 1.0, 1.0
                                    on_release: app.click_dish()

                                MDLabel:
                                    id: dish_id
                                    text: 'Случай не использован'
                                    halign: 'center'

                        Tab:
                            id: tab3
                            title: 'Закуска'
                            icon: ''

                            MDBoxLayout:
                                padding: [20, 100, 20, 60]
                                orientation: 'vertical'

                                MDFillRoundFlatButton:
                                    text: 'Закуска'
                                    size_hint: 1.0, 1.0
                                    on_release: app.click_bread()

                                MDLabel:
                                    id: bread_id
                                    text: 'Случай не использован'
                                    halign: 'center'

                        Tab:
                            id: tab4
                            title: 'Напиток'
                            icon: ''

                            MDBoxLayout:
                                padding: [20, 100, 20, 60]
                                orientation: 'vertical'

                                MDFillRoundFlatButton:
                                    text: 'Напиток'
                                    size_hint: 1.0, 1.0
                                    on_release: app.click_compote()

                                MDLabel:
                                    id: compote_id
                                    text: 'Случай не использован'  
                                    halign: 'center'                      

                        Tab:
                            id: tab5
                            title: 'Сладкое'
                            icon: ''

                            MDBoxLayout:
                                padding: [20, 100, 20, 60]
                                orientation: 'vertical'

                                MDFillRoundFlatButton:
                                    id: candies_title
                                    text: 'Сладкое'
                                    size_hint: 1.0, 1.0
                                    on_release: app.click_candies()

                                MDLabel:
                                    id: candies_id
                                    text: 'А сладкое нельзя!'
                                    halign: 'center'

            MDScreen:
                name: "scr 2"

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "История"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)

                        Tab:
                            id: tab6
                            title: 'Первое'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история первого'
                                halign: 'center'

                        Tab:
                            id: tab7
                            title: 'Второе'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история второго'
                                halign: 'center'

                        Tab:
                            id: tab8
                            title: 'Закуска'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история закуски'
                                halign: 'center'

                        Tab:
                            id: tab9
                            title: 'Напиток'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история напитков'
                                halign: 'center'

        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class DietOfTatyanaApp(MDApp):
    title = 'Diet of Tatyana'
    by_who = 'by DenKung'

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        self.click = 0

    def build(self):
        self.theme_cls.primary_palette = 'Green'
        self.theme_cls.theme_style = 'Light'
        self.theme_cls.material_style = 'M3'

        return self.screen

    def on_start(self):
        pass

    def on_tab_switch(
            self, instance_tabs, instance_tab, instance_tab_label, tab_text
    ):
        pass

    def click_soup(self):
        data_soup = [
            'Суп с курицей, картошкой, марковкой',
            'Суп с рыбой, яйцом, картошкой',
            'Суп с гречкой и курица',
            'Суп с рисом и курица',
            'Суп с вермишелью',
            'Суп с фрикадельками и рисом',
            'Суп с фрикадельками и вермишелью',
            'Суп с фрикадельками и гречкой',
            'Суп с фрикадельками и овощами',
        ]
        self.screen.ids.soup_id.text = random.choice(data_soup)

    def click_dish(self):
        data_dish = [
            'Овощное рагу',
            'Отварной картофель с рыбой',
            'Отварной картофель с курицей',
            'Отварной картофель с котлетами',
            'Отварной картофель с фрикадельками',
            'Картошка в мундире в духовке',
            'Макароны с котлетами из курицы',
            'Макароны с рыбой',
            'Макароны с курицей',
            'Макароны с фрикадельками',
            'Овощи в горшочке с фаршем',
            'Овощи в горшочке с курицей',
            'Овощи в горшочке с рыбой',
            'Картофельное пюре и рыба на пару',
            'Картофельное пюре с рыбной котлетой',
            'Картофельное пюре с куриной котлетой',
            'Картофельное пюре и фрикадельки с соусом',
            'Гречневая каша с рыбой',
            'Гречневая каша с рыбной котлетой',
            'Гречневая каша с куриной котлетой',
            'Гречневая каша с фрикадельками',
            'Овсянная каша со сливочным маслом',
            'Рисовая каша со сливочным маслом',
            'Рисовая каша с рыбой на пару',
            'Рисовая каша с рыбной котлетой на пару',
            'Рисовая каша с куриной котлетой',
            'Рисовая каша с фрикадельками',
            'Суфле рыбное с картофельным пюре',
            'Суфле куриное с картофельным пюре',
            'Суфле рыбное с гречневой кашей',
            'Суфле рыбное с рисовой кашей',
            'Суфле рыбное с овощами',
            'Суфле куриное с гречневой кашей',
            'Суфле куриное с рисовой кашей',
            'Суфле куриное с овощами',
            'Манная каша со сливочным маслом',
            'Рыба с картошкой запечённая в духовке',
            'Рыба с овощами запечённая в духовке',
            'Курица с картошкой запечённая в духовке',
            'Курица с овощами запечённая в духовке',
            'Омлет',
        ]
        self.screen.ids.dish_id.text = random.choice(data_dish)

    def click_bread(self):
        data_bread = [
            'Сухари',
            'Тосты',
            'Крекеры',
            'Галетное печенье',
            'Бутерброд из вчерашнего хлеба с домашним паштетом',
            'Бутерброд из вчерашнего хлеба с сыром',
        ]
        self.screen.ids.bread_id.text = random.choice(data_bread)

    def click_compote(self):
        self.click += 1
        if self.click == 5:
            self.screen.ids.compote_id.text = 'Шо тыкаешь? Другого нельзя!'
            self.click = 0
        else:
            self.screen.ids.compote_id.text = 'Компот из сухофруктов'

    def click_candies(self):
        data_candies = [
            'красивая', 'умная', 'заботливая', 'привлекательная', 'сексуальная',
            'добрая', 'нежная', 'милая', 'очаровательная', 'обворожительная',
            'неповторимая', 'неописуемая', 'незабываемая', 'неотразимая',
            'шикарная', 'ослепительная', 'страстная', 'недоступная', 'божественная',
            'завораживающая', 'ангельская', 'лучезарная', 'сексапильная', 'яркая',
            'пушистая', 'обалденная', 'сногсшибательная', 'стройная', 'обольстительная',
            'кокетливая', 'утончённая', 'грациозная', 'весёлая', 'энергичная', 'креативная',
            'стильная', 'коммуникабельная', 'тактичная', 'любвеобильная', 'романтичная',
            'краса моих глаз', 'сказочная', 'симпатичная', 'пылкая', 'свет очей моих',
            'ласковая', 'сладенькая', 'умопомрачительная', 'желанная', 'непредсказуемая',
            'загадочная', 'цветущая', 'безупречная', 'гармоничная', 'отзывчивая', 'совершенная',
            'лучшая', 'скромная', 'изысканная', 'шаловливая', 'отпадная', 'искренняя',
            'дружелюбная', 'понимающая', 'экстравагантная', 'мечтательная', 'ароматная',
            'искромётная', 'чистолюбивая', 'манящая', 'восторженная', 'бескорыстная',
            'непосредственная', 'соблазнительная', 'одурманивающая', 'жизнерадостная',
            'прелестная', 'улыбчивая', 'застенчивая', 'зажигательная', 'честная', 'возбуждающая',
            'чистосердечная', 'игривая', 'обаятельная', 'непредсказуемая', 'целеустремлённая',
            'дивная', 'женственная', 'блаженная', 'бесподобная', 'лучезарная', 'ненаглядная',
            'необходимая', 'изумительная', 'сказочная', 'трогательная', 'миниатюрная',
            'любимая', 'самая-самая',
        ]
        self.screen.ids.candies_title.text = 'Вместо сладкого:'
        self.screen.ids.candies_id.text = 'Ты ' + random.choice(data_candies) + '!'


class ContentNavigationDrawer(MDBoxLayout):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MyScreen(MDScreen):
    click = 0

    soup = ObjectProperty()
    dish = ObjectProperty()
    bread = ObjectProperty()
    compote = ObjectProperty()
    candies = ObjectProperty()
    candies_title = ObjectProperty()

    def click_soup(self):
        data_soup = [
            'Суп с курицей, картошкой, марковкой',
            'Суп с рыбой, яйцом, картошкой',
            'Суп с гречкой и курица',
            'Суп с рисом и курица',
            'Суп с вермишелью',
            'Суп с фрикадельками и рисом',
            'Суп с фрикадельками и вермишелью',
            'Суп с фрикадельками и гречкой',
            'Суп с фрикадельками и овощами',
        ]
        self.soup.text = random.choice(data_soup)
        self.soup.text_size = self.soup.size

    def click_dish(self):
        data_dish = [
            'Овощное рагу',
            'Отварной картофель с рыбой',
            'Отварной картофель с курицей',
            'Отварной картофель с котлетами',
            'Отварной картофель с фрикадельками',
            'Картошка в мундире в духовке',
            'Макароны с котлетами из курицы',
            'Макароны с рыбой',
            'Макароны с курицей',
            'Макароны с фрикадельками',
            'Овощи в горшочке с фаршем',
            'Овощи в горшочке с курицей',
            'Овощи в горшочке с рыбой',
            'Картофельное пюре и рыба на пару',
            'Картофельное пюре с рыбной котлетой',
            'Картофельное пюре с куриной котлетой',
            'Картофельное пюре и фрикадельки с соусом',
            'Гречневая каша с рыбой',
            'Гречневая каша с рыбной котлетой',
            'Гречневая каша с куриной котлетой',
            'Гречневая каша с фрикадельками',
            'Овсянная каша со сливочным маслом',
            'Рисовая каша со сливочным маслом',
            'Рисовая каша с рыбой на пару',
            'Рисовая каша с рыбной котлетой на пару',
            'Рисовая каша с куриной котлетой',
            'Рисовая каша с фрикадельками',
            'Суфле рыбное с картофельным пюре',
            'Суфле куриное с картофельным пюре',
            'Суфле рыбное с гречневой кашей',
            'Суфле рыбное с рисовой кашей',
            'Суфле рыбное с овощами',
            'Суфле куриное с гречневой кашей',
            'Суфле куриное с рисовой кашей',
            'Суфле куриное с овощами',
            'Манная каша со сливочным маслом',
            'Рыба с картошкой запечённая в духовке',
            'Рыба с овощами запечённая в духовке',
            'Курица с картошкой запечённая в духовке',
            'Курица с овощами запечённая в духовке',
            'Омлет',
        ]
        self.dish.text = random.choice(data_dish)
        self.dish.text_size = self.dish.size

    def click_bread(self):
        data_bread = [
            'Сухари',
            'Тосты',
            'Крекеры',
            'Галетное печенье',
            'Бутерброд из вчерашнего хлеба с домашним паштетом',
            'Бутерброд из вчерашнего хлеба с сыром',
        ]
        self.bread.text = random.choice(data_bread)
        self.bread.text_size = self.bread.size

    def click_compote(self):
        self.click += 1
        if self.click == 5:
            self.compote.text = 'Шо тыкаешь? Другого нельзя!'
            self.click = 0
        else:
            self.compote.text = 'Компот из сухофруктов'
            self.compote.text_size = self.compote.size

    def click_candies(self):
        data_candies = [
            'красивая', 'умная', 'заботливая', 'привлекательная', 'сексуальная',
            'добрая', 'нежная', 'милая', 'очаровательная', 'обворожительная',
            'неповторимая', 'неописуемая', 'незабываемая', 'неотразимая',
            'шикарная', 'ослепительная', 'страстная', 'недоступная', 'божественная',
            'завораживающая', 'ангельская', 'лучезарная', 'сексапильная', 'яркая',
            'пушистая', 'обалденная', 'сногсшибательная', 'стройная', 'обольстительная',
            'кокетливая', 'утончённая', 'грациозная', 'весёлая', 'энергичная', 'креативная',
            'стильная', 'коммуникабельная', 'тактичная', 'любвеобильная', 'романтичная',
            'краса моих глаз', 'сказочная', 'симпатичная', 'пылкая', 'свет очей моих',
            'ласковая', 'сладенькая', 'умопомрачительная', 'желанная', 'непредсказуемая',
            'загадочная', 'цветущая', 'безупречная', 'гармоничная', 'отзывчивая', 'совершенная',
            'лучшая', 'скромная', 'изысканная', 'шаловливая', 'отпадная', 'искренняя',
            'дружелюбная', 'понимающая', 'экстравагантная', 'мечтательная', 'ароматная',
            'искромётная', 'чистолюбивая', 'манящая', 'восторженная', 'бескорыстная',
            'непосредственная', 'соблазнительная', 'одурманивающая', 'жизнерадостная',
            'прелестная', 'улыбчивая', 'застенчивая', 'зажигательная', 'честная', 'возбуждающая',
            'чистосердечная', 'игривая', 'обаятельная', 'непредсказуемая', 'целеустремлённая',
            'дивная', 'женственная', 'блаженная', 'бесподобная', 'лучезарная', 'ненаглядная',
            'необходимая', 'изумительная', 'сказочная', 'трогательная', 'миниатюрная',
            'любимая', 'самая-самая',
        ]
        self.candies_title.text = 'Вместо сладкого:'
        self.candies.text = 'Ты ' + random.choice(data_candies) + '!'
        self.candies.text_size = self.candies.size


if __name__ == '__main__':
    DietOfTatyanaApp().run()
