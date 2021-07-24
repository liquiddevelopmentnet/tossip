# :heavy_exclamation_mark: Still in Development
# Tossip
A library to easily communicate with iOS Devices natively.

- Implementation of the most commands.
- Easily interact with the Device.
- support for python >= 3.6

Feel free to contribute!

## Install using pip
```
pip install tossip
```
For Linux distributions with both python2 and python3 (e.g. Debian, Ubuntu, ...) you need to run
```
pip3 install tossip
```

## Usage

### Get every UDID of the iOS Devices that are connected to the Computer as an Array.
```python
from tossip import functions

def collectUDIDs():
    print(functions.getConnectedDeviceUDIDs())
```

## Authors
- **LiquidDevelopmentNET**

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details