from warnings import warn
import sys
from numpy import abs

# setup an example variable that polls the voltage on a GPIO pin that needs to be within +/- 0.3 V of 5 V, 
# and will give unreliable operation if it deviates more than +/- 0.5 V

voltage_from_gpio_pin = [5.0, 5.1, 5.3, 4.5, 5.0, 2.0, 5.5, 5.0]

for v in voltage_from_gpio_pin:
    volt_deviation = abs(v - 5.0)
    
    if volt_deviation > 0.5:
        # 0 is normal termination
        # 1 is abnormal termination
        sys.exit("voltage has deviated too much (%.1f V)!" % volt_deviation)
    if volt_deviation > 0.3:
        warn("Voltage is drifting a bit too much.")
    else:
        print("Voltage is within tolerance.")
