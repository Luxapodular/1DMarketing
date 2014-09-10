import os
import subprocess

FADE_TIME_MS = 100
HIDE_TERMINAL = True
BLINK_TOOL_PATH = "blink1-tool.exe"

def setColor(color):
  # Build color string
  r = color[0]
  g = color[1]
  b = color[2]
  colorString = "%d,%d,%d"%(r,g,b)

  # Build command strings
  rgbCommandString = "--rgb=%s"%colorString
  timeCommandString = "-m %d"%FADE_TIME_MS
  command = [BLINK_TOOL_PATH, timeCommandString, rgbCommandString]

  # Send commands to blink1-tool
  print "Sending ", colorString, "to blink(1)"
  subprocess.Popen(command, shell=HIDE_TERMINAL, creationflags=subprocess.SW_HIDE)
