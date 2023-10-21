"""
This is an example of how to light a strip of ws2812b pixels with the Raspberry Pi Pico using
a motion detector and a light sensor.
"""
import time

from machine import Pin
from neopixel import NeoPixel

# How many pixels do we have?
PIXEL_COUNT = 65

# How long should we keep the light on?
LIGHT_MINUTES = 3

# Which pin controls the light strip?
PIXEL_PIN = Pin(0)

# Which pin controls the motion detector?
MOTION_DETECTION_PIN = 1

# Which pin is connected to the light sensor?
LIGHT_SENSOR_PIN = 22

# Define the color we want to use for the light strip
WHITE = (127, 127, 127)

# Define how we want to turn off the light strip
OFF = (0, 0, 0)

# How long should we stay on after detecting motion?
SHINE_TIME = 60 * LIGHT_MINUTES


def set_color(strip, color):
    """
    Set the color of the pixel strip
    Args:
        strip (): The pixel strip name
        color (): The color to set

    Returns:
        Nothing
    """
    strip.fill(color)
    strip.write()


pixels = NeoPixel(PIXEL_PIN, PIXEL_COUNT)
motion = Pin(MOTION_DETECTION_PIN, Pin.IN, Pin.PULL_DOWN)
light_sensor = Pin(LIGHT_SENSOR_PIN, Pin.IN, Pin.PULL_DOWN)

set_color(pixels, OFF)

while True:
    is_movement = bool(motion.value())
    is_dark = bool(light_sensor.value())

    print(f"MAIN: movement: {is_movement} darkness: {is_dark}")

    if is_movement and is_dark:
        print("MAIN: Turning ON strip")
        set_color(pixels, WHITE)
        time.sleep(SHINE_TIME)
        print("MAIN: Turning OFF strip")
        set_color(pixels, OFF)

    time.sleep(0.01)  # Adjust the sleep duration as needed for responsiveness
