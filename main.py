servos.P1.set_range(0, 180)

def on_every_interval():
    servos.P1.set_angle(pins.analog_read_pin(AnalogPin.P0) / 5.68333333333)
loops.every_interval(100, on_every_interval)
