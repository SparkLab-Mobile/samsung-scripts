#!/usr/bin/env python3
import serial
import time

port = "/dev/ttyACM0"
baudrate = 115200
ser = serial.Serial(port, baudrate=baudrate)
print(f"Using port {port} set to {baudrate} baud...")

def write_and_read(ser, command):
    try:
        ser.write(command.encode())
        time.sleep(1)   # TODO: check when serial port
        print(ser.read_all().replace(b'\r\n', b'\n').decode("utf-8"))
    except Exception:
        pass

def send_at_cmd(ser):
    print("Sending AT Commands...")

    for command in [
        # For example: Reboot to Download Mode
        "AT+SUDDLMOD=0,0\r\n",
    ]:
        write_and_read(ser, command)

send_at_cmd(ser)
