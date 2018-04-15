import RPi.GPIO as GPIO
import time

ch_num=4

cs_pin=29
clk_pin=31
mosi_pin=33
miso_pin=35		#Data in

t_SUCS=100e-9
t_SU=50e-9


GPIO.setmode(GPIO.BOARD)
GPIO.setup(cs_pin,GPIO.OUT)
GPIO.setup(clk_pin,GPIO.OUT)
GPIO.setup(mosi_pin,GPIO.OUT)
GPIO.setup(miso_pin,GPIO.IN)

'''
if (ch_num>7 || ch_num<1)
	print("The channel must be 0 < ch_num < 8")
	break
'''
try:
        while True:
                
                GPIO.output(cs_pin,GPIO.HIGH)
                GPIO.output(clk_pin,GPIO.LOW)
                GPIO.output(cs_pin,GPIO.LOW)

                for i in range(0,5,1):
                        GPIO.output(clk_pin,GPIO.HIGH)
                        GPIO.output(clk_pin,GPIO.LOW)
                        
                        GPIO.output(mosi_pin,GPIO.HIGH)   #start
                        GPIO.output(mosi_pin,GPIO.HIGH)   #SGL/DIFF
                        GPIO.output(mosi_pin,GPIO.LOW)    #0,0,0 Channel0
                        GPIO.output(mosi_pin,GPIO.LOW)
                        GPIO.output(mosi_pin,GPIO.LOW)
                
                for j in range(0,12,1):
                        GPIO.output(clk_pin,GPIO.HIGH)
                        GPIO.output(clk_pin,GPIO.LOW)
                        
                        adcout=GPIO.input(miso_pin)
                

                GPIO.output(cs_pin,GPIO.HIGH)
except:
        GPIO.cleanup()
