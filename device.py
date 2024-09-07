from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self):
        self._is_off = True
        self._volume = 0
        self._channel = 0

    @abstractmethod
    def play(self):
        pass

    def display_volume(self):
        print(f'Volume is: {self._volume}')
    
    def turn_on(self):
        self._is_off = False

    def turn_off(self):
        self._is_off = True

    def get_volume(self) -> int:
        return self._volume
    
    def set_volume(self, volume: int):
        if 0 <= volume <= 100:
            self._volume = volume
        else:
            raise ValueError('invalid volume')
        
    def get_channel(self) -> int:
        return self._channel
    
    def set_channel(self, channel: int):
        if 0 <= channel <= 999:
            self._channel = channel
        else:
            raise ValueError('invalid channel')


class TV(Device):
    def play(self):
        if self._channel == 24:
            print('You are watching SBT')
        elif self._channel == 29:
            print('You are watching TV Cultura')
        elif self._channel == 32:
            print('You are watching Globo')
        elif self._channel == 45:
            print('You are watching Record')
        else:
            print('TV is flickering')


class Radio(Device):
    def play(self):
        if self._channel == 1:
            print('You are listening California FM')
        elif self._channel == 2:
            print('You are watching Radio Jovem')
        else:
            print('Radio is flickering')



