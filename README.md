# pyRedisBridge

Export keys from a redis DB to another one over a serial link (like Bridge on Arduino Yun)


Redis A <--- /dev/ttyAMA0 ---> Redis B

1. create key "tx:name" on first Redis A
2. redis-serial-sync transfer name with value on Redis B
3. key "rx:name" is set on redis B
4. key "tx:name" is delete on redis A

### Setup

```bash
sudo python3 setup.py install
```

### Fix serial port name (add symlink)

```bash
# how-to get serial string for a specific serial port
udevadm info --name=/dev/ttyUSB0 --attribute-walk | grep {serial}
# copy a udev rules file template to add symlink in /dev directory
sudo cp etc/udev/rules.d/10-usb-serial.local.rules /etc/udev/rules.d/
```

### Supervisor

```bash
sudo apt-get install supervisor
# for "bureau" rpi
sudo cp etc/supervisor/conf.d/rpi_bridge_bureau.conf /etc/supervisor/conf.d/
# for "indus" rpi
sudo cp etc/supervisor/conf.d/rpi_bridge_indus.conf /etc/supervisor/conf.d/
# for "internet" rpi
sudo cp etc/supervisor/conf.d/rpi_bridge_internet.conf /etc/supervisor/conf.d/
# reload conf
sudo supervisorctl update
```
