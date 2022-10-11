import math
import itertools
import numpy as np

import main

def calcSin(frequency, amplitude, sampleRate):
  stepSize = (2 * math.pi * frequency) / sampleRate
  return (math.sin(x) * amplitude for x in itertools.count(0, stepSize))

def createWaveArray(frequency, amplitude, numSamples):
  sinVals = calcSin(frequency, amplitude, main.sampleRate)
  waveArray = np.array([next(sinVals) for i in range(numSamples)])

  return waveArray

class Mode:
  def __init__(self, frequency, amplitude, numSamples):
    self.waveArray = createWaveArray(frequency, amplitude, numSamples)

  def getWaveArray(self):
    return self.waveArray
