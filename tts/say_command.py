import os

def say_command(msg):
  print("Text to Speech: {}".format(msg))
  os.system("python polly.py " + msg + " >/dev/null 2>&1")
  return
