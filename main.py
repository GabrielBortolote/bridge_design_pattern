from device import TV, Radio
from remote import CompleteControl, SimpleControl


if __name__ == "__main__":
    print('Testing TV')

    tv = TV()
    tv_remote = CompleteControl(tv)
    tv.play()
    tv.display_volume()

    # change volume
    tv_remote.increase_volume()
    tv.display_volume()
    tv_remote.increase_volume()
    tv.display_volume()
    tv_remote.increase_volume()
    tv.display_volume()
    tv_remote.mute()
    tv.display_volume()

    # set channel
    tv_remote.set_channel(32)
    tv.play()

    tv_remote.set_channel(29)
    tv.play()

    print('-'*50)
    print('Testing Radio')

    radio = Radio()
    radio_remote = SimpleControl(radio)
    radio.play()
    radio.display_volume()

    # change volume
    radio_remote.increase_volume()
    radio_remote.increase_volume()
    radio_remote.increase_volume()
    radio.display_volume()

    # set channel
    radio_remote.increase_channel()
    radio.play()

    radio_remote.increase_channel()
    radio.play()