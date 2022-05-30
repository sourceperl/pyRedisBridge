# pyRedisBridge

Export keys from a redis DB to another one over a serial link.


Redis 1 (remote = node2) <--- /dev/ttyUSB0 ---> Redis 2 (remote = node1) 

```bash
# on redis 1
redis-serial-sync --remote node1 /dev/ttyUSB0 9600
# on redis 2
redis-serial-sync --remote node2 /dev/ttyUSB0 9600
```

1. create key "tx:node2:keyname" on first Redis 1
2. redis-serial-sync transfer key and it's value to Redis 2
3. key "tx:node2:keyname" is delete on redis 1
4. key "rx:node1:keyname" is set on redis 2

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
# for bridge "bureau"
sudo cp etc/supervisor/conf.d/redis-bridges-bureau.conf /etc/supervisor/conf.d/redis-bridges.conf
# for bridge "indus"
sudo cp etc/supervisor/conf.d/redis-bridges-indus.conf /etc/supervisor/conf.d/redis-bridges.conf
# for bridge "internet"
sudo cp etc/supervisor/conf.d/redis-bridges-internet.conf /etc/supervisor/conf.d/redis-bridges.conf
# reload conf
sudo supervisorctl update
```
