__version__ = '0.2.1'

from kivymd.app import MDApp
from kivy.uix.gridlayout import GridLayout
from kivy.properties import ObjectProperty
from kivy.core.window import Window
from kivy.lang import Builder
from kivymd.theming import ThemeManager
import random

# Window.size = (1080, 2400)
#Window.size = (270, 600)

Builder.load_string('''
#:import MDLabel kivymd.label.MDLabel
#:import MDRaisedButton kivymd.button.MDRaisedButton

<RootWidget>:
    rows: 2

    soup: soup_id
    dish: dish_id
    bread: bread_id
    compote: compote_id
    candies: candies_id
    candies_title: candies_title

    AnchorLayout:
        size_hint_y: .15
        ItemLabel:
            text: 'Не знаешь что готовить? Доверься случаю!'
            font_size: '20sp'
            halign: 'center'

    BoxLayout:
        orientation: 'vertical'
        padding: [30, 20, 30, 50]
        spacing: 10

        UsButton:
            text: 'Cуп'
            on_release: root.click_soup()

        ItemLabel:
            id: soup_id
            text: 'Случай не разыгран'

        UsButton:
            text: 'Второе'
            on_release: root.click_dish()

        ItemLabel:
            id: dish_id
            text: 'Случай не разыгран'

        UsButton:
            text: 'Хлеб'
            on_release: root.click_bread()

        ItemLabel:
            id: bread_id
            text: 'Случай не разыгран'

        UsButton:
            text: 'Компот'
            on_release: root.click_compote()

        ItemLabel:
            id: compote_id
            text: 'Случай не разыгран'

        UsButton:
            id: candies_title
            text: 'А сладкое?'
            on_release: root.click_candies()

        ItemLabel:
            id: candies_id
            text: 'А сладкое нельзя!'
            
<ItemLabel@MDLabel>:
    text_size: self.size
    font_size: '15sp'
    halign: 'left'
    valign: 'middle'

<UsButton@MDRaisedButton>:
    font_size: '20sp'
    text_size: self.size
    halign: 'center'
    valign: 'middle'
    size_hint_x: 1.0
    ''')


class DietOfTatyanaApp(MDApp):
    theme_cls = ThemeManager()
    title = 'Diet of Tatyana'

    def build(self):
        self.theme_cls.theme_style = 'Light'
        return RootWidget()


class RootWidget(GridLayout):

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
        ]
        self.dish.text = random.choice(data_dish)
        self.dish.text_size = self.dish.size

    def click_bread(self):
        data_bread = [
            'Сухари',
            'Тосты',
            'Омлет',
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
