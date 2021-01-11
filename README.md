# Docker container for DHT11

[日本語ドキュメント(より詳細)](./README-jp.md)

## Usage

```sh
docker-compose up -d
# or
docker run --privileged -d hiroyukiosaki/raspi-py-dht11
```

## Appendix: Installation of docker-compose on Raspbian

```sh
sudo apt-get install libffi-dev libssl-dev
sudo apt install python3-dev
sudo apt-get install -y python3 python3-pip
sudo pip3 install docker-compose
```

## Copyright notice

package dht11: Copyright (c) 2016 Zoltan Szarvas.