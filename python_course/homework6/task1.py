# Создать класс TrafficLight (светофор) и определить у него один атрибут color (цвет)
# и метод running (запуск). Атрибут реализовать как приватный.
# В рамках метода реализовать переключение светофора в режимы:
# красный, желтый, зеленый.
# Продолжительность первого состояния (красный) составляет 7 секунд,
# второго (желтый) — 2 секунды, третьего (зеленый) — на ваше усмотрение.
# Переключение между режимами должно осуществляться только в указанном порядке (красный, желтый, зеленый).
# Проверить работу примера, создав экземпляр и вызвав описанный метод.
# Задачу можно усложнить, реализовав проверку порядка режимов,
# и при его нарушении выводить соответствующее сообщение и завершать скрипт.

from time import sleep
from itertools import cycle
from threading import Timer
import unittest


class TrafficLight:
    __colors = cycle((str, timer) for str, timer in {'red': 7, 'yellow': 2, 'green': 10}.items())
    __cur_color = None

    def running(self):
        tmp = next(TrafficLight.__colors)
        TrafficLight.__cur_color = tmp[0]
        print(tmp[0])
        return tmp

    def get_cur_color(self):
        return TrafficLight.__cur_color


def destroy_TrafficLight_make_chaos_AHAHAHAH():
    TrafficLight._TrafficLight__cur_color = next(TrafficLight._TrafficLight__colors)[0]


class TestTrafficLight(unittest.TestCase):

    def test_color(self):
        Timer(20.0, destroy_TrafficLight_make_chaos_AHAHAHAH).start()
        tl = TrafficLight()
        for _ in range(15):
            color, timer = tl.running()
            sleep(timer)
            self.assertEqual(color, tl.get_cur_color(), "Wrong traffic light color!")


if __name__ == '__main__':
    unittest.main()
