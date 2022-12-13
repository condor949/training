# Начните работу над проектом «Склад оргтехники».
# Создайте класс, описывающий склад.
# А также класс «Оргтехника», который будет базовым для классов-наследников.
# Эти классы — конкретные типы оргтехники (принтер, сканер, ксерокс).
# В базовом классе определить параметры, общие для приведенных типов.
# В классах-наследниках реализовать параметры, уникальные для каждого типа оргтехники.
import time


class OfficeEquipment:
    def __init__(self, model=None, lan_module=False):
        self.model = model
        self.lan_module = lan_module


class Printer(OfficeEquipment):
    def __init__(self, model=None, lan_module=False, double_sided_print=False, print_time=5, *args):
        self.double_sided_print = double_sided_print
        self.print_time = print_time
        self.printable_formats = args
        OfficeEquipment.__init__(model, lan_module)

    def print(self):
        print("Begin print! Please wait!")
        time.sleep(self.print_time*2 if self.double_sided_print else self.print_time)
        print("End print!")


class Scanner(OfficeEquipment):
    def __init__(self, model=None, lan_module=False, scan_time=20):
        self.scan_time = scan_time
        OfficeEquipment.__init__(model, lan_module)

    def scan(self):
        print("Begin scan! Please wait!")
        time.sleep(self.scan_time)
        print("End scan!")


class Xerox(Printer, Scanner):
    def __init__(self, model=None, lan_module=False, double_sided_print=False, scan_time=20, print_time=5,
                 *args):
        Printer.__init__(model, lan_module, double_sided_print, print_time, *args)
        Scanner.__init__(model, lan_module, scan_time)

    def copy(self):
        print("Begin copy! Please wait!")
        self.scan()
        self.print()
        print("End copy!")
