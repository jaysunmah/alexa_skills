import os
import sys
f = open(os.devnull, 'wb')
sys.stdout = f

command = "aws polly synthesize-speech --output-format mp3 --voice-id Joanna --text '" + " ".join(sys.argv[1:]) + "' output.mp3"

os.system(command)
os.system("mpg123 output.mp3")
