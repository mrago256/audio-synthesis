import numpy as np

import main
import waveGenerator as wg

def additiveSquareWave(numModes):
  modeList = []

  for i in range(1, numModes + 1, 2):
    modeList.append(wg.Mode(main.baseFrequency * i, 1/i, main.sampleNumber))

  finalWave = np.zeros(len(modeList[0].getWaveArray()))

  for i in modeList:
    finalWave = finalWave + i.getWaveArray()

  return finalWave

def clampedSquareWave():
  Mode1 = wg.Mode(main.baseFrequency * 1, 1, main.sampleNumber)
  mode1Wave = Mode1.getWaveArray()

  mode1Wave[mode1Wave > 0] = 1
  mode1Wave[mode1Wave < 0] = -1

  return mode1Wave
