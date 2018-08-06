# pyRedisBridge

Export keys from a redis DB to another one over a serial link (like Bridge on Arduino Yun)


Redis A <--- /dev/ttyAMA0 ---> Redis B

1. create key "tx:name" on first Redis A
2. redis-serial-sync transfer name with value on Redis B
3. key "rx:name" is set on redis B
4. key "tx:name" is delete on redis A

### Setup

    sudo python3 setup.py install

### Supervisor

    sudo apt-get install supervisor
    # for "bureau" rpi
    sudo cp etc/supervisor/conf.d/rpi_bridge_bureau.conf /etc/supervisor/conf.d/
    # for "indus" rpi
    sudo cp etc/supervisor/conf.d/rpi_bridge_indus.conf /etc/supervisor/conf.d/
    # for "internet" rpi
    sudo cp etc/supervisor/conf.d/rpi_bridge_internet.conf /etc/supervisor/conf.d/
    # reload conf
    sudo supervisorctl update

### Systemd (auto-start) [deprecated]

    sudo cp redis-serial-sync.service /etc/systemd/system/
    sudo systemctl enable redis-serial-sync.service
    sudo systemctl start redis-serial-sync.service
