haartraining.exe -data cascades -vec vector/vector.vec -bg negative/bg.txt -nstages 12 -mem 4096 -npos 567 -nneg 4000 -w 60 -h 60 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -mode ALL -precalcValBufSize 4096 -precalcIdxBufSize 4096 -featureType HAAR

rem -nonsym

pause