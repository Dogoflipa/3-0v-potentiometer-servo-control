servos.P1.setRange(0, 180)
loops.everyInterval(100, function () {
    servos.P1.setAngle(pins.analogReadPin(AnalogPin.P0) / 5.68333333333)
})
