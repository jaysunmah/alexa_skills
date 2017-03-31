import os
import sys


command = "aws polly synthesize-speech --output-format mp3 --voice-id Joanna --text '" + " ".join(sys.argv[1:]) + "' output.mp3"

os.system(command)
os.system("afplay output.mp3")
