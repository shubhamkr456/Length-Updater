import pyperclip
import time
from pywinauto import Application
from pywinauto.keyboard import send_keys
from pywinauto.mouse import click
from pywinauto import findwindows, Desktop
import pyautogui
import keyboard
import gc
import pandas as pd
from sys import exit


# --------variable declaration---------------------
WireID_paster= (679, 925)
# Recording for add_button
add_button= (1451, 612)
# Recording for edit_note
edit_note= (1038, 520)
# Recording for apply
apply= (1455, 962)

# Path where the analysed excel has been placed----
path = r"C:\Users\vu378e\Desktop\Peer\Analysed_Output"


###--------------------------------------------------
def HarnessADDSelector():
    pyautogui.moveTo(add_button)
    pyautogui.click()


def WireIDpaster():
    pyautogui.moveTo(WireID_paster)
    pyautogui.click()
    send_keys("{BACKSPACE}" * 30, with_spaces=True)
    time.sleep(0.2)
    send_keys("^v")  # Paste the clipboard content


def curmover(tupl):
    pyautogui.moveTo(tupl)
    time.sleep(0.5)
    pyautogui.click()

z = input("Enter File name with extension")
file = path + "\\" + z
# Main Execution
variable_value = ""
try:
    df = pd.read_excel(file, dtype=str, sheet_name='RunLetters')
except:
    df=df = pd.read_excel(file, dtype=str)

df.fillna("", inplace=True)
if "Master_Run_letter" not in df.columns:
    print("Master_Run_letter column missing.")
    print(
            "Master_run_letter is not having data. Check for Run_letter_status :-- SAME"
        )
    exit()

df = df[df["Run_letter_Status"] == "Different"]
# Time Calculation

print(f"Estimated time: {(df.shape[0]* 9.77)/60} mins")

# Select the Harnes Window
time.sleep(8)
# HarnessWinSelector()

start_time = time.time()

for index, row in df.iterrows():
    
    if keyboard.is_pressed("esc"):
        print("Program paused. Press 'tab' to resume.")
        # Pause the loop until 'r' is pressed
        while not keyboard.is_pressed("tab"):
            time.sleep(0.1)
        print("Resuming program...")
    
    
    # Wire ID is selcted
    variable_value = row["WIRE ID"]
    pyperclip.copy(variable_value)
    note_ = "SIGNAL_CODE"
    note_text = row["Master_Run_letter"]
    backspacepress = len(row["SIGNAL_CODE"]) + 4
    time.sleep(0.1)
    screen_width, screen_height = pyautogui.size()
    pyautogui.moveTo(screen_width // 2, screen_height // 3)
    pyautogui.click()
    ## Type the wireID
    WireIDpaster()
    # if notecode1 and note 2 is empty or not
    HarnessADDSelector()
    # This selects the type box -----edit_note
    curmover(edit_note)
    time.sleep(0.7)
    pyautogui.click()
    # Delete the selected text using the Backspace key
    send_keys("{BACKSPACE}" * 30, with_spaces=True)
    send_keys(note_ * 1)
    time.sleep(0.2)
    send_keys("{ENTER}", with_spaces=True)
    time.sleep(0.5)
    send_keys("{BACKSPACE}" * backspacepress, with_spaces=True)
    send_keys(note_text * 1, with_spaces=True)
    curmover(apply)  # apply

gc.collect()
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Execution time: {elapsed_time} seconds")
