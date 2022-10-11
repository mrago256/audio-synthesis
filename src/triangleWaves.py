import numpy as np

import main
import waveGenerator as wg

def additiveTriangleWave(numModes):
  modeList = []
  sign = 1

  for i in range(1, numModes + 1, 2):
    modeList.append(wg.Mode(main.baseFrequency * i * sign, 1/(i ** 2), main.sampleNumber))
    sign *= -1

  finalWave = np.zeros(len(modeList[0].getWaveArray()))

  for i in modeList:
    finalWave = finalWave + i.getWaveArray()

  return finalWave
