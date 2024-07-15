basic.showIcon(IconNames.Heart)
DFRobotMaqueenPlus.I2CInit()
DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBA, Color.OFF)
DFRobotMaqueenPlus.mototStop(Motors.ALL)
let active = false
let MOTOR_SPEED = 50
let DISTANCE_THRESHOLD_CM = 10
input.onButtonPressed(Button.A, function go() {
    /** Sets the global 'active' variable to True */
    
    active = true
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.GREEN)
})
input.onButtonPressed(Button.B, function stop() {
    /** Sets the global 'active' variable to False and stops the motors */
    
    active = false
    DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBL, Color.RED)
    DFRobotMaqueenPlus.mototStop(Motors.ALL)
})
basic.forever(function on_forever() {
    /** Main loop. Checks ultrasonic distance and turns if too close. */
    //  Check your robot! Change these numbers if needed!
    //  First argument is ultrasonic GREEN wire pin
    //  Second argument is ultrasonic BLUE wire pin    
    let distance_cm = DFRobotMaqueenPlus.ultraSonic(PIN.P1, PIN.P2)
    if (distance_cm < DISTANCE_THRESHOLD_CM) {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.BLUE)
        if (active) {
            DFRobotMaqueenPlus.mototRun(Motors.M1, Dir.CW, MOTOR_SPEED)
            DFRobotMaqueenPlus.mototRun(Motors.M2, Dir.CCW, MOTOR_SPEED)
        }
        
    } else {
        DFRobotMaqueenPlus.setRGBLight(RGBLight.RGBR, Color.PINK)
        if (active) {
            DFRobotMaqueenPlus.mototRun(Motors.ALL, Dir.CW, MOTOR_SPEED)
        }
        
    }
    
})