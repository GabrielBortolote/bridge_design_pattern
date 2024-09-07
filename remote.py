from device import Device

class Remote:
    def __init__(self, device: Device):
        self.device = device

    def toggle_power(self):
        if self.device.is_off:
            self.device.turn_on()
        else:
            self.device.turn_off()


class SimpleControl(Remote):
    def increase_volume(self):
        self.device.set_volume(self.device.get_volume() + 10)

    def decrease_volume(self):
        self.device.set_volume(self.device.get_volume() - 10)

    def increase_channel(self):
        self.device.set_channel(self.device.get_channel() + 1)

    def decrease_channel(self):
        self.device.set_channel(self.device.get_channel() - 1)


class CompleteControl(SimpleControl):
    def mute(self):
        self.device.set_volume(0)

    def set_channel(self, channel: int):
        self.device.set_channel(channel)