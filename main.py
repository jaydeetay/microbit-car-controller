x_cal = 0
y_cal = 0
joyx = 0
joyy = 0
ymin = 0
xmin = 0
basic.show_icon(IconNames.HOUSE)
radio.set_group(1)
xmax = 1023
ymax = 1023
xcenter = (xmax - xmin) / 2
ycenter = (ymax - ymin) / 2
centertol = 100

def on_forever():
    global joyx, x_cal, y_cal, joyy
    joyx = bitcommander.read_joystick(BCJoystick.X)
    x_cal = 0
    if abs(joyx - xcenter) > centertol:
        x_cal = (joyx - xcenter) * 2 / (xmax - xmin)
    # basic.showNumber(x_cal)
    # basic.pause(1000)
    radio.send_value("lr", x_cal)
    if x_cal > 0:
        basic.show_arrow(ArrowNames.EAST)
    elif x_cal < 0:
        basic.show_arrow(ArrowNames.WEST)
    else:
        basic.show_icon(IconNames.DIAMOND)
    y_cal = 0
    joyy = bitcommander.read_joystick(BCJoystick.Y)
    if abs(joyy - ycenter) > centertol:
        y_cal = (joyy - ycenter) * 2 / (ymax - ymin)
    # basic.showNumber(x_cal)
    # basic.pause(1000)
    radio.send_value("fb", y_cal)
    if y_cal > 0:
        basic.show_arrow(ArrowNames.NORTH)
    elif y_cal < 0:
        basic.show_arrow(ArrowNames.SOUTH)
    else:
        basic.show_icon(IconNames.SMALL_DIAMOND)
    # Without the delay the messages seem to 
    # overwhelm the recipient and cause very laggy response.
    # Yes the LEDs are clearly not cycling 20 times per
    # second so something else in the code is really slow.
    # TODO: find out if it's the LEDs.
    basic.pause(50)
basic.forever(on_forever)
