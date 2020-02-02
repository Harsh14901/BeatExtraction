import librosa as lb
import numpy as np
path = "./song.wav"
y, sr = lb.load(path)
# print(sr)
o_env = lb.onset.onset_strength(y, sr=sr)
o_times = lb.onset.onset_detect(y, sr=sr, onset_envelope=o_env)
# print(o_times.shape)
tempo,beats = lb.beat.beat_track(sr=sr,onset_envelope=o_env)
wait = 0;

if tempo > 120:
    wait = 5
else:
    wait = np.random.randint(low=0,high=5,dtype="float32")

peaks = lb.util.peak_pick(o_env, 5, 5, 5, 5, 0.3,wait) #ideally the parameters should depend on the tempo of the music.
peaks = lb.frames_to_time(peaks)
# print(peaks.shape)

f = open("tempo.txt", 'w')
for peak in peaks:
    f.write(str(peak) + "\n")
f.close()
