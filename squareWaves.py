import main
import waveGenerator as wg

def additiveSquareWave():
  mode1 = wg.createWaveArray(main.baseFrequency * 1, 1, main.sampleNumber)
  mode3 = wg.createWaveArray(main.baseFrequency * 3, (1/3), main.sampleNumber)
  mode5 = wg.createWaveArray(main.baseFrequency * 5, (1/5), main.sampleNumber)
  mode7 = wg.createWaveArray(main.baseFrequency * 7, (1/7), main.sampleNumber)
  mode9 = wg.createWaveArray(main.baseFrequency * 9, (1/9), main.sampleNumber)
  mode11 = wg.createWaveArray(main.baseFrequency * 11, (1/11), main.sampleNumber)
  mode13 = wg.createWaveArray(main.baseFrequency * 13, (1/13), main.sampleNumber)
  mode15 = wg.createWaveArray(main.baseFrequency * 15, (1/15), main.sampleNumber)

  finalWave = mode1 + mode3 + mode5 + mode7 + mode9 + mode11 + mode13 + mode15

  return finalWave

def clampedSquareWave():
  mode1 = wg.createWaveArray(main.baseFrequency * 1, 1, main.sampleNumber)

  mode1[mode1 >= 0] = 1
  mode1[mode1 < 0] = -1

  return mode1
