# Retuning
## Robert Handy

### Summary
In this project, I attempt to change the tuning of a note using pitch shifting. It does this by processing a .wav file, determining the dominant note, and using that as a basis for its pitch shifting. It then calcualtes the factor that it has to change the wavelength by to achieve the desired pitch and uses that factor to strech the sound wave and then resample to the original sound rate.

### Current State
Currently this is a ghostifyer. During the processing of the audio, there is a lot of noise that is being introduced. This is still being worked on to remove that noise. An example can be seen with the original Ebm.wav file and the retuned-Ebm.wav file.

Currently this supports retuning to two different tunings: Equal temperment and Pythagorean.

### Running the Program
The program is simple to run. Simply run `python PitchShift.py <input-filename> <desired-tuning>`.

### Testing
So far, the testing that has been done is using the provided Ebm.wav file and the focus has been on identifying and removing the noise.

### Overal Result
Currently the program doesn't work as intended. Reducing the noise is a large part of what needs to be done. This is something that I will be actively working on to remove, and then to verify that the tuning is correct.