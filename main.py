import threading
import numpy as np
import sounddevice as sd
from matplotlib import pyplot as plt

import squareWaves as sw

sampleRate = 10500
sampleNumber = 44100
baseFrequency = 440

# prevents ALSA underrun most times
plt.title("")

def playWave(waveArray):
  sd.play(waveArray, sampleRate)
  sd.wait()

def showGraph(waveArray):
  plt.title("Wave Preview")
  plt.xlabel("Sample Number")
  plt.ylabel("Amplitude")
  plt.axhline(y=0, c="black")
  plt.plot(np.arange(235), waveArray[:235])

  plt.show()


if __name__ == "__main__":
  additiveSquare = sw.additiveSquareWave()
  clampedSquare = sw.clampedSquareWave()

  # something be broken with the threading when low sample rate
  t1 = threading.Thread(target=playWave, args=(additiveSquare,))
  t2 = threading.Thread(target=playWave, args=(clampedSquare,))

  t1.daemon = True
  t2.daemon = True

  t1.start()
  showGraph(additiveSquare)

  t2.start()
  showGraph(clampedSquare)

  t1.join()
  t2.join()
