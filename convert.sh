#!/bin/bash
# Converting the audio files from .wav to .opus reduces the total file size from 6.9G down to 366M
for i in *.wav; do
	ffmpeg -i "$i" -y "${i%.*}.opus";
done

