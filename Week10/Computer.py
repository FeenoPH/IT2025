from CPU import CPU
from RAM import RAM
from HardDisk import HardDisk
from GPU import GPU

class Computer:
    def __init__(self, CPU, RAM, HardDisk, GPU):
        self.CPU = CPU
        self.RAM = RAM
        self.HardDisk = HardDisk
        self.GPU = GPU
        self.price = 0
    def start(self):
        self.CPU.compute()
        self.HardDisk.load_os()
    def compute(self):
        self.CPU.compute()
        self.GPU.compute()
    def calculate_price(self):
        self.price = self.CPU.price + self.RAM.price + self.HardDisk.price + self.GPU.price
    def print_price(self):
        if self.price == 0:
            self.calculate_price()
        print(f"Price: ${self.price}")

CPU_1 = CPU(100, "Intel", 7600)
RAM_1 = RAM(59, "Corsair", "DDR4", 16)
HardDisk_1 = HardDisk(139, "Samsung", "SSD", 2000)
GPU_1 = GPU(275, "Nvidia", "RTX 2080", 1515)

my_computer = Computer(CPU_1, RAM_1, HardDisk_1, GPU_1)
my_computer.start()
my_computer.compute()
my_computer.print_price()
