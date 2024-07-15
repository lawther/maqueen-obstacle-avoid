basic.show_icon(IconNames.HEART)
DFRobotMaqueenPlus.i2c_init()
DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBA, Color.OFF)
DFRobotMaqueenPlus.motot_stop(Motors.ALL)

active = False
MOTOR_SPEED = 50

DISTANCE_THRESHOLD_CM = 10

# Check your robot! Change these pins if needed!
ULTRASONIC_GREEN_PIN = PIN.P1
ULTRASONIC_BLUE_PIN = PIN.P2

def go():
    """Sets the global 'active' variable to True"""
    global active
    active = True
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.GREEN)

input.on_button_pressed(Button.A, go)

def stop():
    """Sets the global 'active' variable to False and stops the motors"""
    global active
    active = False
    DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.motot_stop(Motors.ALL)

input.on_button_pressed(Button.B, stop)

def on_forever():
    """Main loop. Checks ultrasonic distance and turns if too close."""
    distance_cm = DFRobotMaqueenPlus.ultra_sonic(ULTRASONIC_GREEN_PIN, ULTRASONIC_BLUE_PIN)
    if distance_cm < DISTANCE_THRESHOLD_CM:
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.BLUE)
        if active:
            DFRobotMaqueenPlus.motot_run(Motors.M1, Dir.CW, MOTOR_SPEED)
            DFRobotMaqueenPlus.motot_run(Motors.M2, Dir.CCW, MOTOR_SPEED)
    else:
        DFRobotMaqueenPlus.set_rgb_light(RGBLight.RGBR, Color.PINK)
        if active:
            DFRobotMaqueenPlus.motot_run(Motors.ALL, Dir.CW, MOTOR_SPEED)

basic.forever(on_forever)