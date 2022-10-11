import numpy as np

import main
import waveGenerator as wg

def additiveSawtoothWave(numModes):
  modeList = []

  for i in range(1, numModes + 1):
    modeList.append(wg.Mode(main.baseFrequency * i, (1/i)/2, main.sampleNumber))

  finalWave = np.zeros(len(modeList[0].getWaveArray()))

  for i in modeList:
    finalWave = finalWave + i.getWaveArray()

  return finalWave
