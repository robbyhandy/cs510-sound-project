import numpy as np

def determine_dominant_freq(a, frame_rate):
    """ Performs an FFT to determine the dominant frequency. """
    ft = np.fft.fft(a)
    freqs = np.fft.fftfreq(len(ft))
    idx = np.argmax(abs(ft))
    return abs(freqs[idx] * frame_rate)
    
def determine_freq_shift(orig_freq, final_freq):
    """ Determines the frequency shift needed """
    return final_freq / orig_freq

def strech_wavelength(arr, scale_factor, window_size, overlap):
    scaled_arr = np.zeros(int(len(arr) / scale_factor + window_size))
    
    # Use hanning for smoothing
    hanning = np.hanning(window_size)
    
    # Keeping track of phase
    phase = np.zeros(window_size)

    index_arr = np.arange(0, len(arr) - window_size + overlap, scale_factor * overlap).astype(np.int32)

    for i in index_arr:
        # Get the two windows
        a0 = arr[i : i + window_size]
        a1 = arr[i + overlap : i + window_size + overlap]
        
        if (len(a0) < window_size):
            a0 = np.append(a0, np.zeros(window_size - len(a0)))
        if (len(a1) < window_size):
            a1 = np.append(a1, np.zeros(window_size - len(a1)))
        
        # Smooth them for better FFT
        a0 = hanning * a0
        a1 = hanning * a1
        
        ft0 = np.fft.fft(a0)
        ft1 = np.fft.fft(a1)
        
        # Ensure the phase is in sync
        phase = (phase + np.angle(ft1/ft0)) % 2*np.pi
        
        # Change a1 to be in phase with a0
        a1 = np.fft.ifft(np.abs(ft1) * np.exp(1j * phase))
        a1 *= hanning
        
        scaled_arr[int(i/scale_factor): int(i/scale_factor) + window_size] += np.real(a1)
        
    return scaled_arr
        
def resample(arr, scale_factor):
    indexes = np.round(np.arange(0, len(arr), scale_factor))
    indexes = indexes[indexes < len(arr)]
    indexes = np.asarray(indexes, dtype=np.int32)
    return arr[indexes]
    