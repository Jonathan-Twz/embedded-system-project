import serial           
import sys

try:
  ser = serial.Serial('/dev/ttyACM0', 9600)
except Exception:
  print('open serial failed.')
  exit(1)

while True:
  # echo
  s = ser.read()
  if(s!='#'):
    ser.write(s)
  # write to stdout and flush it
    sys.stdout.write(s)
    sys.stdout.flush()