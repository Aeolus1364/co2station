#!/usr/bin/env bash

wget http://www.airspayce.com/mikem/bcm2835/bcm2835-1.56.tar.gz
tar -zxf bcm2835-1.56.tar.gz
cd bcm2835-1.56
./configure
sudo make check
sudo make install
cd ..
git clone https://github.com/paulvha/twowire
cd twowire
sudo make install
cd ..
git clone https://github.com/paulvha/scd30_on_raspberry
cd scd30_on_raspberry
make
