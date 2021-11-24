import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)
GPIO.setwarnings(False)

LED = 7
Button = 10
CancelButton = 11

GPIO.setup(LED, GPIO.OUT)
GPIO.setup(Button, GPIO.IN, pull_up_down=GPIO.PUD_UP)
GPIO.setup(CancelButton, GPIO.IN, pull_up_down=GPIO.PUD_UP)

codeBool = True
userMorse = ""


def interruptcode(channel):
    print("Button was pushed")
    userInp = raw_input("Would you like to input again? (y/n)\n")
    if userInp == 'y':
        userMorse = ""
        codeBool = True
        print("Continuing...")

    elif userInp == 'n':
        print("Program ended.")
        codeBool = False

    else:
        print("Invalid answer. Program ended.")
        codeBool = False

GPIO.add_event_detect(CancelButton, GPIO.RISING, callback=interruptcode)

while codeBool == True:
    button_state = GPIO.input(Button)
    
    if button_state == 0:
        GPIO.output(LED, GPIO.HIGH)
        buttonStatus = 0
        start_time = time.time()

        while GPIO.input(Button) == 0:  # Wait for the button to release
            pass
        buttonTime = time.time() - start_time   # How long was the button down?

        if buttonTime >=  .15:
            buttonStatus = 2
            userMorse += "-"
        else:
            #elif buttonTime >= .05     # 1 unit = .05
            buttonStatus = 1
            userMorse += "."
        
        print(userMorse)

    elif len(userMorse) > 0 and userMorse[-1] == " ":
        pass
    else:
        GPIO.output(LED, GPIO.LOW)

        start_time = time.time()
        while GPIO.input(Button) == 1:  # Wait for the button to be pressed
            pass
        buttonTime = time.time() - start_time

        if buttonTime >= .35:
            userMorse += " /"   # Word separator
            print(userMorse)

        elif buttonTime >= .15:
            userMorse += " "
            print(userMorse)

GPIO.cleanup()


