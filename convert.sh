#!/bin/zsh
# Converting the audio files from .wav to .opus reduces the total file size from 6.9G down to 366M
for i in *.wav; do
	ffmpeg -i "$i" -y -loglevel 16 "${i%.*}.opus";
	printf "$(ls *.opus | wc -l)/9848 %.2f%%\\n" "$(( $(ls *.opus | wc -l) / 9848.0 * 100.0 ))";
done

