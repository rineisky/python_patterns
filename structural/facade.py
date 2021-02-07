class CPU(object):
    def __init__(self):
        # ...
        pass

    def freeze(self):
        # ...
        pass

    def jump(self, address):
        # ...
        pass

    def execute(self):
        # ...
        pass

class Memory(object):
    def __init__(self):
        # ...
        pass

    def load(self, position, data):
        # ...
        pass

class HardDrive(object):
    def __init__(self):
        # ...
        pass

    def read(self, lba, size):
        # ...
        pass

# Фасад
class Computer(object):
    def __init__(self):
        self._cpu = CPU()
        self._memory = Memory()
        self._hardDrive = HardDrive()

    def startComputer(self):
        self._cpu.freeze()
        self._memory.load(BOOT_ADDRESS, self._hardDrive.read(BOOT_SECTOR, SECTOR_SIZE))
        self._cpu.jump(BOOT_ADDRESS)
        self._cpu.execute()

# Клиентская часть
if __name__ == "__main__":
    facade = Computer()
    facade.startComputer()