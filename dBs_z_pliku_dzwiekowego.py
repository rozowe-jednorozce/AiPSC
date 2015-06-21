import pyaudio
import wave
import sys
from array import array
import audioop
import math

CHUNK_SIZE = 256
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 48000

dB_dla_testu = -9.03107793667 # = -3 LU
LU_przelicznik = -3 - dB_dla_testu
normalize_amplitude = 65536

if len(sys.argv) < 2:
    print("Converts wav file into dBs.\n\nUsage: %s filename.wav" % sys.argv[0])
    sys.exit(-1)

wf = wave.open(sys.argv[1], 'rb')
p = pyaudio.PyAudio()
stream = p.open(format = FORMAT,
                channels = CHANNELS,
                rate = RATE,
                input = True,
                frames_per_buffer = CHUNK_SIZE)
data = wf.readframes(CHUNK_SIZE)

while data != '':
    audio_data = array('i', data)
    rms = audioop.rms(audio_data, 2)
    amplitude = float(rms)/normalize_amplitude
    if amplitude == 0:
        dbs = 0
    else:
        dbs = 20 * math.log10(amplitude)
    print str(dbs + LU_przelicznik) + " LU"
    data = wf.readframes(CHUNK_SIZE)

stream.stop_stream()
stream.close()
p.terminate()
