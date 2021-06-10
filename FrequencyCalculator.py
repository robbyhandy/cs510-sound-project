import numpy as np

class FrequencyCalculator:
    # Everything is tuned based off of C4
    
    C4_FREQ = 261.6256
    C4_MIDI = 60
    
    NOTE_INDEX = ['C', 'C#', 'D', 'D#', 'E', 'F', 'F#', 'G', 'G#', 'A', 'A#', 'B'] 
    
    PYTHAGOREAN_TUNING = [1, 256/243, 9/8, 32/27, 81/64, 4/3, 729/512, 3/2, 27/16, 16/9, 243/168]
    
    def determine_note(self, freq):
        """ Determines the note that this is supposed to be. 
        Just finds the note that is closest in equal temperment. """
        
        n = 12 * np.log(freq / self.C4_FREQ)
        diff = np.round(n)
        
        note_midi = self.C4_MIDI + diff
        octave = int((note_midi - 12) / 12)
        note_name = self.NOTE_INDEX[int(note_midi % 12)]
        return note_name + str(octave)
            
        
    def get_octave_freq(self, note):
        """ Gets the frequency of the C note in the notes octave. """
        octave = int(note[-1])
        octave_diff = octave - 4
        return self.C4_FREQ * 2 ** octave_diff
        
    def get_equal_temperment(self, note):
        start_freq = self.get_octave_freq(note)
        note_index = self.NOTE_INDEX.index(note[:-1])
        return start_freq * 2 ** (note_index / 12)
    
    def get_pythagorean_tuning(self, note):
        start_freq = self.get_octave_freq(note)
        note_index = self.NOTE_INDEX.index(note[:-1])
        return start_freq * self.PYTHAGOREAN_TUNING[note_index]