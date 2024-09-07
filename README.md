# Bridge

This project implements a use case for a Design Pattern, the Bridge. To know more about this pattern you can access [this website](https://refactoring.guru/design-patterns/bridge).

## What it is?

Bridge is a structural design pattern that lets you split a large class or a set of closely related classes into two separate hierarchies—abstraction and implementation—which can be developed independently of each other.

## Project

Let's implement the interaction between devices and remote controls. First we implement the device, the device will be controlled by the remote, you can check device code on *device.py* and remote code on *remote.py*, this is the final result:

```bash
python main.py 
Testing TV
TV is flickering
Volume is: 0
Volume is: 10
Volume is: 20
Volume is: 30
Volume is: 0
You are watching Globo
You are watching TV Cultura
--------------------------------------------------
Testing Radio
Radio is flickering
Volume is: 0
Volume is: 30
You are listening California FM
You are watching Radio Jovem
```

Thanks for reading.
