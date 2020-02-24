#-------------------------------------------------------------------------
#
#		Name: 		Eng. William R. Fröhlich
#
#		Project: 	MFRC522 - RFID Orientation
#
#		Date: 		2019.03.30
#
#-------------------------------------------------------------------------

# Enable SPI
raspi-config

# Edit the file config.txt
sudo nano /boot/config.txt

# Add the line
dtoverlay=spi-bcm2708

# Test SPI
ls /dev/spi*
## Answer: /dev/spidev0.0 /dev/spidev0.1

dmesg | grep spi
## answer: 	[ 6.240564] bcm2708_spi 3f204000.spi: master is unqueued, this is deprecated
			[ 6.241262] bcm2708_spi 3f204000.spi: SPI Controller at 0x3f204000 (irq 80)

# Install the package Python-dev
sudo apt-get install python-dev

# Install the Library for the SPI
git clone https://github.com/lthiery/SPI-Py.git
cd SPI-Py
sudo python setup.py install

# Download the Package MFRC522
mkdir -p /home/pi/leitor-rfid
/home/pi/leitor-rfid
git clone https://github.com/pimylifeup/MFRC522-python