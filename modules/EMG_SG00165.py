from machine import Pin
from machine import ADC
import time

def EMG_sensor(analog_pin):
  adc = ADC(Pin(analog_pin))
  adc.atten(ADC.ATTN_11DB)
  adc.width(ADC.WIDTH_12BIT)
  Adc_out = adc.read()
  time.sleep_ms(20)

  return Adc_out



