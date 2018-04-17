import spidev
import time
import os

# open(bus, device) : open(X,Y) will open /dev/spidev-X.Y
spi = spidev.SpiDev()
spi.open(0,0)

# Read SPI data from MCP3008, Channel must be an integer 0-7
def ReadADC(ch):
    if ((ch > 7) or (ch < 0)):
       return -1
    adc = spi.xfer2([1,(8+ch)<<4,0])
    data = ((adc[1]&3) << 8) + adc[2]
    return data

delay = 3

try:
    while True:
      adcout = ReadADC(6)
      print (adcout)
      time.sleep(delay)

except:
    pass
