from machine import Pin
from machine import ADC
import time

def EMG_sensor(analog_pin):
  adc = ADC(Pin(analog_pin))
  adc.atten(ADC.ATTN_11DB)
  adc.width(ADC.WIDTH_12BIT)
  
  sensorValue = 0
  EMA_a = 0.2
  EMA_S = 1
  highpass = 0

  EMA_S = adc.read()

  while True:
    sensorValue = adc.read()
    EMA_S = (EMA_a * sensorValue) + ((1 - EMA_a) * EMA_S)
    highpass = sensorValue - EMA_S
    print(str('EMG') + "=" + str('%.2f' %highpass))
    time.sleep_ms(20)
