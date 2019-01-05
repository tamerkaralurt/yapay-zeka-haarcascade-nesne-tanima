pip install opencv-python
pip install opencv-contrib-python
pip install opencv-python-headless
pip install opencv-contrib-python-headless

image-net.org //resimlerin aldigi yer

mkdir data
mkdir info
opencv_createsamples -img positive_images/ball.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1282 //1282 dosya icindeki resim sayisi
opencv_createsamples -info info/info.lst -num 1282 -w 20 -h 20 -vec positives.vec
opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 1000 -numStages 10 -w 20 -h 20

nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 5 -w 20 -h 20 & //numStages kac stage olustuysa o yazilacak.
opencv_traincascade -data classifier -vec pos.vec -bg negatives.txt -numStages 20 -minHitRate 0.999 -maxFalseAlarmRate 0.5 -numPos 2728 -numNeg 16000 -w 16 -h 16 -mode ALL -precalcValBufSize 256 -precalcIdxBufSize 256 -acceptanceRatioBreakValue 10e-5 -nonsym -baseFormatSave -featureType LBP
