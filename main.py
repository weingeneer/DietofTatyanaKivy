__version__ = '0.2.6'

from kivy.core.window import Window
from kivy.lang import Builder

from kivymd.app import MDApp
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.tab import MDTabsBase
from kivymd.uix.floatlayout import MDFloatLayout
from kivymd.uix.menu import MDDropdownMenu
from kivymd.uix.button import MDFlatButton
from kivymd.uix.behaviors.toggle_behavior import MDToggleButton
from kivymd.uix.dialog import MDDialog
import random

# Window.size = (1080, 2400)
Window.size = (270, 600)

DATA_SOUP = [
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
DATA_DISH = [
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
DATA_BREAD = [
    'Сухари',
    'Тосты',
    'Крекеры',
    'Галетное печенье',
    'Бутерброд из вчерашнего хлеба с домашним паштетом',
    'Бутерброд из вчерашнего хлеба с сыром',
]
DATA_COMPOTE = [
    'Компот из сухофруктов'
]
DATA_CANDIES = [
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

KV = '''
<MyButton@MDFillRoundFlatButton>

    size_hint: 1.0, 0.3
    text_size: '30sp'
    
<MyLabel@MDLabel>

    text: 'Случай не использован'
    text_size: '30sp'
    halign: 'center'

<AddButton@MDFloatingActionButton>

    icon: 'pencil-plus-outline'
    pos_hint: {'center_x': .9, 'center_y': .5}   

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
                    root.screen_manager.current = "eats"

            OneLineListItem:
                text: "История"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "history"
                    
            OneLineListItem:
                text: "Группы"
                on_press:
                    root.nav_drawer.set_state("close")
                    root.screen_manager.current = "groups"

MDScreen:

    MDNavigationLayout:
        x: toolbar.height

        ScreenManager:
            id: screen_manager

            MDScreen:
                name: "eats"

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Что приготовить?"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)

                        Tab:
                            id: tab1
                            title: 'Первое'
                            icon: ''

                            MDBoxLayout:
                                padding: '20dp', '100dp', '20dp', '60dp'
                                orientation: 'vertical'

                                MyButton:
                                    text: 'Доверься случаю!'
                                    size_hint: 1.0, 0.3
                                    on_release: app.click_soup()

                                MyLabel:
                                    id: soup_id
                                
                                AddButton:
                                    on_release: screen_manager.current = 'add' 
                                    
                        Tab:
                            id: tab2
                            title: 'Второе'
                            icon: ''

                            MDBoxLayout:
                                padding: '20dp', '100dp', '20dp', '60dp'
                                orientation: 'vertical'

                                MyButton:
                                    text: 'Доверься случаю!'
                                    size_hint: 1.0, 0.3
                                    on_release: app.click_dish()

                                MyLabel:
                                    id: dish_id
                                    
                                AddButton:
                                    on_release: screen_manager.current = 'add' 

                        Tab:
                            id: tab3
                            title: 'Закуска'
                            icon: ''

                            MDBoxLayout:
                                padding: '20dp', '100dp', '20dp', '60dp'
                                orientation: 'vertical'

                                MyButton:
                                    text: 'Доверься случаю!'
                                    size_hint: 1.0, 0.3
                                    on_release: app.click_bread()

                                MyLabel:
                                    id: bread_id
                                    
                                AddButton:
                                    on_release: screen_manager.current = 'add' 

                        Tab:
                            id: tab4
                            title: 'Напиток'
                            icon: ''

                            MDBoxLayout:
                                padding: '20dp', '100dp', '20dp', '60dp'
                                orientation: 'vertical'

                                MyButton:
                                    text: 'Доверься случаю!'
                                    size_hint: 1.0, 0.3
                                    on_release: app.click_compote()

                                MyLabel:
                                    id: compote_id
                                    
                                AddButton:
                                    on_release: screen_manager.current = 'add'                      

                        Tab:
                            id: tab5
                            title: 'Сладкое'
                            icon: ''

                            MDBoxLayout:
                                padding: '20dp', '100dp', '20dp', '60dp'
                                orientation: 'vertical'

                                MyButton:
                                    id: candies_title
                                    text: 'Доверься случаю!'
                                    size_hint: 1.0, 0.3
                                    on_release: app.click_candies()

                                MyLabel:
                                    id: candies_id
                                    
            MDScreen:
                name: "history"

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
            
            MDScreen:
                name: "groups"

                MDBoxLayout:
                    orientation: 'vertical'

                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Группы"
                        left_action_items: [["menu", lambda x: nav_drawer.set_state("open")]]

                    MDTabs:
                        id: tabs
                        on_tab_switch: app.on_tab_switch(*args)

                        Tab:
                            id: tab10
                            title: 'Первое'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история первого'
                                halign: 'center'

                        Tab:
                            id: tab11
                            title: 'Второе'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история второго'
                                halign: 'center'

                        Tab:
                            id: tab12
                            title: 'Закуска'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история закуски'
                                halign: 'center'

                        Tab:
                            id: tab13
                            title: 'Напиток'
                            icon: ''

                            MDLabel:
                                text: 'Здесь должна быть история напитков'
                                halign: 'center'
            
            MDScreen:
                name: 'add'
                                 
                MDBoxLayout:
                    orientation: 'vertical'
                    spacing: '20sp'
                    
                    MDToolbar:
                        id: toolbar
                        pos_hint: {"top": 1}
                        elevation: 10
                        title: "Добавить блюдо"
                        
                    MDTextField:
                        id: field
                        pos_hint: {'center_x': .5, 'center_y': .6}
                        size_hint_x: None
                        width: "200dp"
                        hint_text: "Выберите группу блюд"
                        required: True
                        input_filter: 'callable'
                        helper_text: "Обязательное поле"
                        helper_text_mode: "on_error"
                        on_focus: if self.focus: app.menu.open()
                        
                    MDTextField:
                        id: dish
                        pos_hint: {'center_x': .5, 'center_y': .6}
                        size_hint_x: None
                        width: "200dp"
                        hint_text: 'Введите желаемое блюдо'
                        required: True
                        helper_text: "Обязательное поле"
                        helper_text_mode: "on_error"
                    
                    MDBoxLayout:
                        adaptive_size: True
                        pos_hint: {"center_x": .5, "center_y": .5}
                        
                        MyToggleButton:
                            id: cancel_change
                            text: 'Назад'
                            group: 'x'
                            on_release: screen_manager.current = 'eats'
                            
                        MyToggleButton:
                            id: confirm_change
                            text: 'OK'
                            group: 'x'
                            on_release: app.dialogs() 
                                                                              
                    Widget:
                                        
        MDNavigationDrawer:
            id: nav_drawer

            ContentNavigationDrawer:
                screen_manager: screen_manager
                nav_drawer: nav_drawer
'''


class DietOfTatyanaApp(MDApp):
    title = 'Diet of Tatyana'
    by_who = 'by DenKung'
    dialog_confirm = None
    dialog_error = None

    def __init__(self, data_soup, data_dish, data_bread, data_compote, data_candies, **kwargs):
        super().__init__(**kwargs)
        self.screen = Builder.load_string(KV)
        menu_items = [
            {
                'viewclass': "OneLineListItem",
                'text': i,
                'height': 56,
                'on_release': lambda x=i: self.set_item(x),
            } for i in ['Первое', 'Второе', 'Закуски', 'Напитки']]
        self.menu = MDDropdownMenu(
            caller=self.screen.ids.field,
            items=menu_items,
            position="bottom",
            width_mult=4,
        )
        self._click = 0
        self._data_soup = data_soup
        self._data_dish = data_dish
        self._data_bread = data_bread
        self._data_compote = data_compote
        self._data_candies = data_candies

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

    def set_item(self, text__item):
        self.screen.ids.field.text = text__item
        self.menu.dismiss()

    def click_soup(self):
        self.screen.ids.soup_id.text = random.choice(self._data_soup)

    def click_dish(self):
        self.screen.ids.dish_id.text = random.choice(self._data_dish)

    def click_bread(self):
        self.screen.ids.bread_id.text = random.choice(self._data_bread)

    def click_compote(self):
        if len(self._data_compote) == 1 and self._click >= 5:
            self.screen.ids.compote_id.text = 'Шо тыкаешь? Другого нельзя!'
            self._click = 0
        else:
            self.screen.ids.compote_id.text = random.choice(self._data_compote)
            self._click += 1

    def click_candies(self):
        self.screen.ids.candies_title.text = 'Вместо сладкого:'
        self.screen.ids.candies_id.text = 'Ты ' + random.choice(self._data_candies) + '!'

    def dialogs(self):
        if self.screen.ids.field.text and self.screen.ids.dish.text:
            if not self.dialog_confirm:
                self.dialog_confirm = MDDialog(
                    text="Внести изменения?",
                    buttons=[
                        MDFlatButton(
                            text="Назад",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.dialog_confirm_close
                        ),
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.add_eats
                        ),
                    ],
                )
            self.dialog_confirm.open()
        else:
            if not self.dialog_error:
                self.dialog_error = MDDialog(
                    text="Заполните обязательные поля",
                    buttons=[
                        MDFlatButton(
                            text="OK",
                            theme_text_color="Custom",
                            text_color=self.theme_cls.primary_color,
                            on_release=self.dialog_error_close
                        ),
                    ],
                )
            self.dialog_error.open()

    def dialog_error_close(self, *args):
        self.dialog_error.dismiss()

    def dialog_confirm_close(self, *args):
        self.dialog_confirm.dismiss()

    def add_eats(self, *args):
        dict_eats = {
            'Первое': self._data_soup,
            'Второе': self._data_dish,
            'Закуски': self._data_bread,
            'Напитки': self._data_compote,
        }

        group_eats = self.screen.ids.field.text
        dish = self.screen.ids.dish.text
        dict_eats[group_eats].append(dish)
        self.dialog_confirm_close()
        self.screen.ids.screen_manager.current = 'eats'


class ContentNavigationDrawer(MDBoxLayout):
    pass


class Tab(MDFloatLayout, MDTabsBase):
    pass


class MyToggleButton(MDFlatButton, MDToggleButton):
    pass

if __name__ == '__main__':
    DietOfTatyanaApp(DATA_SOUP, DATA_DISH, DATA_BREAD, DATA_COMPOTE, DATA_CANDIES).run()
