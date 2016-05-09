#!/usr/bin/python
import RPi.GPIO as GPIO
import time

# Use physical pin numbers
GPIO.setmode(GPIO.BOARD)
# Set up header pin 12 (GPIO18) as an input
led13Pin = 13
led38Pin = 38
led40Pin = 40
led31Pin = 31
led33Pin = 33
led35Pin = 35
led37Pin = 37
print "Setup Pin 12 is OutPut..."
GPIO.setup(led13Pin, GPIO.OUT)
GPIO.setup(led38Pin, GPIO.OUT)
GPIO.setup(led40Pin, GPIO.OUT)
GPIO.setup(led31Pin, GPIO.OUT)
GPIO.setup(led33Pin, GPIO.OUT)
GPIO.setup(led35Pin, GPIO.OUT)
GPIO.setup(led37Pin, GPIO.OUT)

print "Starting... "

while True:

  if True:  
    print "Spark"
    GPIO.output(led13Pin, False)
    time.sleep(1)
    GPIO.output(led13Pin, True)
    time.sleep(1)

  if True:
    print "cold white"
    GPIO.output(led38Pin, True)
    time.sleep(1)
    GPIO.output(led38Pin, False)

    print "warm white"
    GPIO.output(led40Pin, True)
    time.sleep(1)
    GPIO.output(led40Pin, False)
  
  if True:
    print "Red"
    GPIO.output(led31Pin, True)
    time.sleep(1)
    GPIO.output(led31Pin, False)

    print "Green"
    GPIO.output(led33Pin, True)
    time.sleep(1)
    GPIO.output(led33Pin, False)

    print "Blue"
    GPIO.output(led35Pin, True)
    time.sleep(1)
    GPIO.output(led35Pin, False)

    print "White"
    GPIO.output(led37Pin, True)
    time.sleep(1)
    GPIO.output(led37Pin, False)

GPIO.cleanup()
