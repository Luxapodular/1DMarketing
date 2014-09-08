import os
import subprocess

def setColor(color):
  r = color[0]
  g = color[1]
  b = color[2]
  colorString = "%d,%d,%d"%(r,g,b)

  print colorString
  rgbCommandString = "--rgb=%s"%colorString
  timeCommandString = "-m 100"
  subprocess.Popen(["blink1-tool.exe", timeCommandString, rgbCommandString], shell=True, creationflags=subprocess.SW_HIDE)
