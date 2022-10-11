import threading
import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt

import squareWaves as sw
import triangleWaves as tw
import sawtoothWaves as stw

def setSamplesGraphed(samples):
  global samplesGraphed
  if samples <= sampleNumber:
    samplesGraphed = samples
  else:
    samplesGraphed = sampleNumber

def playWave(waveArray):
  sd.play(waveArray, sampleRate)
  sd.wait()

def showGraph(waveArray):
  plt.title("Wave Preview")
  plt.xlabel("Sample Number")
  plt.ylabel("Amplitude")
  plt.axhline(y=0, c="black")
  plt.plot(np.arange(samplesGraphed), waveArray[:samplesGraphed])

  plt.show()

sampleRate = 44100
numHarmonics = 25
sampleNumber = 44100
baseFrequency = 440

# 235 is a good value to see additions for a sample rate of 44100
setSamplesGraphed(235)

# prevents ALSA underrun most times
plt.title("")

if __name__ == "__main__":
  additiveSquare = sw.additiveSquareWave(numHarmonics)
  clampedSquare = sw.clampedSquareWave()

  additiveTriangle = tw.additiveTriangleWave(numHarmonics)

  additiveSawtooth = stw.additiveSawtoothWave(numHarmonics)

  t1 = threading.Thread(target=playWave, args=(additiveSquare,))
  t2 = threading.Thread(target=playWave, args=(clampedSquare,))
  t3 = threading.Thread(target=playWave, args=(additiveTriangle,))
  t4 = threading.Thread(target=playWave, args=(additiveSawtooth,))

  t1.daemon = True
  t2.daemon = True
  t3.daemon = True
  t4.daemon = True

  t1.start()
  showGraph(additiveSquare)

  t2.start()
  showGraph(clampedSquare)

  t3.start()
  showGraph(additiveTriangle)

  t4.start()
  showGraph(additiveSawtooth)

  t1.join()
  t2.join()
  t3.join()
  t4.join()
