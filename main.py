from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle, Line
from kivy.uix.label import Label
import random

class DietOfTatyanaApp(App):

    def build(self):
        self.root = root = RootWidget()
        # root.bind(size=self._update_rect, pos=self._update_rect)
        #
        #
        # with root.canvas.before:
        #     Color(0, 0, 0, 0)
        #     self.rect = Rectangle(size=root.size, pos=root.pos)
        #     self.line = Line(points=[100, 200, 300, 400])

        return root

    # def _update_rect(self, instance, value):
    #     self.rect.pos = instance.pos
    #     self.rect.size = instance.size

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.draw_button()
        self.draw_header()
        self.draw_footer()

    def click_soup(self, instance):
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
        self.soup.halign = 'center'
        self.soup.valign = 'center'

    def click_dish(self, instance):
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
        self.dish.text_size = self.soup.size
        self.dish.halign = 'center'
        self.dish.valign = 'center'

    def click_bread(self, instance):
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
        self.bread.text_size = self.soup.size
        self.bread.halign = 'center'
        self.bread.valign = 'center'

    def click_compote(self, instance):
        self.compote.text = 'Кампот только из сухофруктов, другого нельзя!'
        self.compote.text_size = self.soup.size
        self.compote.halign = 'center'
        self.compote.valign = 'center'

    def click_candies(self, instance):
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
        self.candies.text = '''
        Вместо сладкого:
        Таня, ты 
        ''' + random.choice(data_candies)
        self.candies.text_size = self.soup.size
        self.candies.halign = 'center'
        self.candies.valign = 'center'
        self.candies.pos_hint = {'center_x': .63, 'center_y': .09}

    def draw_button(self):
        self.add_widget(
            Button(
                text="Случайный суп",
                size_hint=(.3, .2),
                pos_hint={'x': .05, 'y': .7},
                on_press=self.click_soup
            )
        )
        self.add_widget(
            Button(
                text="Случайное второе",
                size_hint=(.3, .2),
                pos_hint={'x': .35, 'y': .7},
                on_press=self.click_dish
            )
        )
        self.add_widget(
            Button(
                text="Случайная прикуска",
                size_hint=(.3, .2),
                pos_hint={'x': .65, 'y': .7},
                on_press=self.click_bread
            )
        )
        self.add_widget(
            Button(
                text="Случайный компот",
                size_hint=(.3, .2),
                pos_hint={'center_x': .35, 'center_y': .6},
                on_press=self.click_compote
            )
        )
        self.add_widget(
            Button(
                text="Случайное сладкое?",
                size_hint=(.3, .2),
                pos_hint={'center_x': .65, 'center_y': .6},
                on_press=self.click_candies
            )
        )

    def draw_header(self):
        self.add_widget(
            Label(
                text='Не знаешь что приготовить? Доверься случаю!',
                size_hint=(1.0, .1),
                pos_hint={'x': .0, 'y': .9}
            )
        )

    def draw_footer(self):
        self.soup = Label(
            text='Не выбрано',
            size_hint=(.2, .15),
            pos_hint={'x': .1, 'y': .25}
        )
        self.dish = Label(
                text='Не выбрано',
                size_hint=(.2, .15),
                pos_hint={'x': .4, 'y': .25}
        )
        self.bread = Label(
            text='Не выбрано',
            size_hint=(.2, .15),
            pos_hint={'x': .7, 'y': .25}
        )
        self.compote = Label(
                text='Не выбрано',
                size_hint=(.2, .15),
                pos_hint={'center_x': .35, 'center_y': .09}
        )
        self.candies = Label(
                text='А сладкое нельзя!',
                size_hint=(.2, .15),
                pos_hint={'center_x': .65, 'center_y': .09}
        )

        self.add_widget(
            Label(
                text='Твой суп сегодня:',
                size_hint=(.3, .05),
                pos_hint={'x': .05, 'y': .4}
            )
        )
        self.add_widget(
            self.soup
        )

        self.add_widget(
            Label(
                text='Твое второе сегодня:',
                size_hint=(.3, .05),
                pos_hint={'x': .35, 'y': .4}
            )
        )
        self.add_widget(
            self.dish
        )

        self.add_widget(
            Label(
                text='Твоя прикуска сегодня:',
                size_hint=(.3, .05),
                pos_hint={'x': .65, 'y': .4}
            )
        )
        self.add_widget(
            self.bread
        )

        self.add_widget(
            Label(
                text='Твой компот сегодня:',
                size_hint=(.3, .05),
                pos_hint={'center_x': .35, 'center_y': .2}
            )
        )
        self.add_widget(
            self.compote
        )

        self.add_widget(
            Label(
                text='Твое сладкое сегодня:',
                size_hint=(.3, .05),
                pos_hint={'center_x': .65, 'center_y': .2}
            )
        )
        self.add_widget(
            self.candies
        )

if __name__ == '__main__':
    DietOfTatyanaApp().run()
