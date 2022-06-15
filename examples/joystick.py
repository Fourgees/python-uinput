import uinput
from inputs import get_gamepad

def main():
    # What events can proc on the virtual xbox controller
    events = (
    uinput.BTN_A,
    uinput.BTN_B,
    uinput.BTN_X,
    uinput.BTN_Y,
    uinput.BTN_TL,
    uinput.BTN_TR,
    uinput.BTN_THUMBL,
    uinput.BTN_THUMBR,
    uinput.ABS_X + (0, 255, 0, 0),
    uinput.ABS_Y + (0, 255, 0, 0),)
    
    #Intialize virtual joystick
    device = uinput.Device(
    events,
    vendor=0x045e,
    product=0x028e,
    version=0x110,
    name="Microsoft X-Box 360 pad",)
    
    # Give the device a second to initialize
    time.sleep(1)
    # Center Joystick
    device.emit(uinput.ABS_X, 128, syn=False)
    device.emit(uinput.ABS_Y, 128)
    
    while True:
        time.sleep(1)
        device.emit(uinput.ABS_Y, 255)  # Max Y
        print("Max y")
        time.sleep(1)
        #device.emit(uinput.ABS_Y, 0)  # Zero Y
        device.emit(uinput.ABS_X,255)
        print("0 Y")
        print("Sleep for 2 seconds")
        time.sleep(1)
        device.emit(uinput.BTN_A, 1)
        print("Press a")
        time.sleep(1)
        print("Release a")
        device.emit(uinput.BTN_A, 0)

if __name__ == "__main__":
    main()
