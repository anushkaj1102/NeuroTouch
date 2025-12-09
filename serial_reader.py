# serial_reader.py
import serial

def read_serial_line(port="/dev/tty.HC-05", baud=9600):
    ser = serial.Serial(port, baud, timeout=1)

    while True:
        line = ser.readline().decode(errors="ignore").strip()
        if line == "":
            continue

        parts = line.split(";")
        parsed = {}

        for p in parts:
            if "=" in p:
                k, v = p.split("=")
                try:
                    parsed[k] = float(v)
                except:
                    parsed[k] = v

        yield parsed
