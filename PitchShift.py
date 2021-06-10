import sys
import wave
from scipy.io import wavfile
import numpy as np
import Retune
from FrequencyCalculator import FrequencyCalculator


def write_wave(filename, data):
    wf = wave.open(filename, 'wb')
    data = data.astype(np.int16)
    wf.setnchannels(1)
    wf.setsampwidth(2)
    wf.setframerate(44100)
    wf.writeframes(data)
    wf.close()
    
def retune(filename, tuning):
        frame_rate, data = wavfile.read(filename)
        dom_freq = Retune.determine_dominant_freq(data, frame_rate)
        
        fc = FrequencyCalculator()
        note = fc.determine_note(dom_freq)
        
        freq = None
        if (tuning == 'equal'):
            freq = fc.get_equal_temperment(note)
        elif (tuning == 'pythagorean'):
            freq = fc.get_pythagorean_tuning(note)
        
        dom_freq = Retune.determine_dominant_freq(data, frame_rate)
        scale_factor = Retune.determine_freq_shift(dom_freq, freq)
        
        stretched = Retune.strech_wavelength(data, scale_factor, 1024, 512)
        resampled = Retune.resample(stretched, scale_factor)
        return resampled
            
filename = sys.argv[1]
tuning = sys.argv[2]

retuned = retune(filename, tuning)
write_wave('retuned-' + filename, retuned)