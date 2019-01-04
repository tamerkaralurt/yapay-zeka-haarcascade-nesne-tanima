pip install opencv-python
pip install opencv-contrib-python
pip install opencv-python-headless
pip install opencv-contrib-python-headless

image-net.org //resimlerin aldigi yer

mkdir data
mkdir info
opencv_createsamples -img positive_images/ball.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 1950 //1950 dosya icindeki resim sayisi
opencv_createsamples -info info/info.lst -num 1950 -w 20 -h 20 -vec positives.vec
nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 5 -w 20 -h 20 & //numStages kac stage olustuysa o yazilacak.