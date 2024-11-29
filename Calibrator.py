import keyboard
import pyautogui
import time
import pywinauto

# List to store the recorded coordinates
click_coordinates = {}
vrs= ["WireID_paster", "add_button",
      "edit_note","length","absolute", "apply"]


def on_click(x, y, button, pressed, vr):
    if pressed:
        coords = (x, y)
        print(f"{vr}= {coords}")
        return False  # Returning False to stop the listener after the first click

def record_click_coordinates():
    print("Press 'q' to record coordinates (Press 'Esc' to stop)..")
    
    try:
        for vr in vrs:
            print ("# Recording for "+vr)
            while True:
                if keyboard.is_pressed('q'):
                    
            # Wait for mouse click event
                    coords = pyautogui.position()
                    click_coordinates[vr] = (coords[0],coords[1] )
                    pyautogui.click(coords)
                    on_click(coords[0], coords[1], None, True, vr)
                    time.sleep(0.5) 
                    break
                # Adding a short delay to avoid rapid fire of click events
                elif keyboard.is_pressed('esc'):
                    print(f"{vr}= {coords}")
                    return
            
    except KeyboardInterrupt:
            print("Stopped recording.")
            print("Recorded coordinates:", click_coordinates)

# Start recording coordinates
record_click_coordinates()
