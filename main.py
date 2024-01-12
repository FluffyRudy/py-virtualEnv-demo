try:
  import pyautogui
except ImportError:
  print("No module named pyautogui")
else:
  pyautogui.write("Imported Successfully")
  print("\n\nFinished run")
