 wget https://github.com/prometheus/node_exporter/releases/download/v0.16.0/node_exporter-0.16.0.linux-amd64.tar.gz
 tar xvf node_exporter-0.16.0.linux-amd64.tar.gz
 sudo useradd --no-create-home --shell /bin/false node_exporter
 sudo cp node_exporter-0.16.0.linux-amd64/node_exporter /usr/local/bin
 sudo chown node_exporter:node_exporter /usr/local/bin/node_exporter
 vim /etc/systemd/system/node_exporter.service

 [Unit]
Description=Node Exporter
Wants=network-online.target
After=network-online.target

[Service]
User=node_exporter
Group=node_exporter
Type=simple
ExecStart=/usr/local/bin/node_exporter

[Install]
WantedBy=multi-user.target
```

systemctl start node_exporter
 systemctl status node_exporter
 systemctl enable node_exporter
 显示：Created symlink from /etc/systemd/system/multi-user.target.wants/node_exporter.service to /etc/systemd/system/node_exporter.service.




