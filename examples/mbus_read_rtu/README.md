# mbus_read_rtu

Read some modbus values in RTU and export it with the redis bridge


### Setup

    sudo cp mbus-read-rtu.service /etc/systemd/system/
    sudo systemctl enable mbus-read-rtu.service
    sudo systemctl start mbus-read-rtu.service
  
