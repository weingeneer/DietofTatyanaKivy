from kivy.app import App
from kivy.uix.button import Button
from kivy.uix.floatlayout import FloatLayout
from kivy.graphics import Color, Rectangle
from kivy.uix.label import Label
import random

class DietOfTatyanaApp(App):

    def build(self):
        self.root = root = RootWidget()
        root.bind(size=self._update_rect, pos=self._update_rect)
        self.rect = Rectangle(size=root.size, pos=root.pos)

        return root

    def _update_rect(self, instance, value):
        self.rect.pos = instance.pos
        self.rect.size = instance.size

class RootWidget(FloatLayout):

    def __init__(self, **kwargs):
        super(RootWidget, self).__init__(**kwargs)
        self.draw_button()

    def draw_button(self):
        self.add_widget(
            Button(
                text="Random Soup",
                size_hint=(.3, .2),
                pos_hint={'x': .05, 'y': .7}
            )
        )
        self.add_widget(
            Button(
                text="Random Dish",
                size_hint=(.3, .2),
                pos_hint={'x': .35, 'y': .7}
            )
        )
        self.add_widget(
            Button(
                text="Random Bread",
                size_hint=(.3, .2),
                pos_hint={'x': .65, 'y': .7}
            )
        )
        self.add_widget(
            Button(
                text="Random Compote",
                size_hint=(.3, .2),
                pos_hint={'center_x': .35, 'center_y': .6}
            )
        )
        self.add_widget(
            Button(
                text="Random Candies",
                size_hint=(.3, .2),
                pos_hint={'center_x': .65, 'center_y': .6}
            )
        )

    def draw_header(self):
        pass

# def get_random_soup():
#     data_soup = [
#         'Суп с курицей ,картошкой,марковкой',
#         'Суп с рыбой,яйцом, картошкой',
#         'Суп с гречкой и курица',
#         'Суп с рисом и курица',
#         'Суп с вермишелью',
#         'Суп с фрикадельками и рисом',
#         'Суп с фрикадельками и вермишелью',
#         'Суп с фрикадельками и гречкой',
#         'Суп с фрикадельками и овощами',
#     ]
#     return random.choice(data_soup)
#
# def get_random_second_dish():
#     data_dish = [
#         'Овощное рагу',
#         'Отварной картофель с рыбой',
#         'Отварной картофель с курицей',
#         'Отварной картофель с котлетами',
#         'Отварной картофель с фрикадельками',
#         'Картошка в мундире в духовке',
#         'Макароны с котлетами из курицы',
#         'Макароны с рыбой',
#         'Макароны с курицей',
#         'Макароны с фрикадельками',
#         'Овощи в горшочке с фаршем',
#         'Овощи в горшочке с курицей',
#         'Овощи в горшочке с рыбой',
#         'Картофельное пюре и рыба на пару',
#         'Картофельное пюре с рыбной котлетой',
#         'Картофельное пюре с куриной котлетой',
#         'Картофельное пюре и фрикадельки с соусом',
#         'Гречневая каша с рыбой',
#         'Гречневая каша с рыбной котлетой',
#         'Гречневая каша с куриной котлетой',
#         'Гречневая каша с фрикадельками',
#         'Овсянная каша со сливочным маслом',
#         'Рисовая каша со сливочным маслом',
#         'Рисовая каша с рыбой на пару',
#         'Рисовая каша с рыбной котлетой на пару',
#         'Рисовая каша с куриной котлетой',
#         'Рисовая каша с фрикадельками',
#         'Суфле рыбное с картофельным пюре',
#         'Суфле куриное с картофельным пюре',
#         'Суфле рыбное с гречневой кашей',
#         'Суфле рыбное с рисовой кашей',
#         'Суфле рыбное с овощами',
#         'Суфле куриное с гречневой кашей',
#         'Суфле куриное с рисовой кашей',
#         'Суфле куриное с овощами',
#         'Манная каша со сливочным маслом',
#         'Рыба с картошкой запечённая в духовке',
#         'Рыба с овощами запечённая в духовке',
#         'Курица с картошкой запечённая в духовке',
#         'Курица с овощами запечённая в духовке',
#     ]
#     return random.choice(data_dish)
#
# def get_random_bread():
#     data_bread = [
#         'Сухари',
#         'Тосты',
#         'Омлет',
#         'Крекеры',
#         'Галетное печенье',
#         'Бутерброд из вчерашнего хлеба с домашним паштетом',
#         'Бутерброд из вчерашнего хлеба с сыром',
#     ]
#     return random.choice(data_bread)
#
# def get_random_compote():
#     return 'Кампот только из сухофруктов, другого нельзя!'
#
# def get_random_candies():
#     return 'А сладкое нельзя!'
#
# def main():
#     print('Не знаете что готовить?')
#     print('Слуайный генератор поможет вам в этом нелегком выборе!')
#     print('Выберите Суп, Второе, Хлеб, Компот или Сладкое')
#     data_sel = {
#         'суп': get_random_soup(),
#         'второе': get_random_second_dish(),
#         'хлеб': get_random_bread(),
#         'компот': get_random_compote(),
#         'сладкое': get_random_candies(),
#     }
#     user_sel = input('Ваш выбор ->')
#     print(data_sel.get(user_sel.lower(), 'Не понятно'))
#
if __name__ == '__main__':
    DietOfTatyanaApp().run()
