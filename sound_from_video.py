import subprocess
import sys

sampling_rate = 16000
audio_channels = 2

path_to_file = sys.argv[1]
output_file = sys.argv[2]
#command = "ffmpeg -i " + path_to_file + " -ab 160k -ac 2 -ar 44100 -vn " + output_file
command = "avconv  -i " + path_to_file + " -ac " + str(audio_channels) + " -ar " + str(sampling_rate) + " -vn " + output_file

subprocess.call(command, shell=True)


