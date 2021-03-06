## yapay-zeka-haarcascade-nesne-tanima
- Python ile nesnelerin haarcascade algoritmasiyla xml dosyasinin hazirlanmasi ve kamerada canli olacak tanimlanmasi projesi

## Kurulum
- Download - [python-3.7.2.exe](https://www.python.org/ftp/python/3.7.2/python-3.7.2.exe)
- İndirdikten sonra kurulumunu gerçekleştirin.
- **Konsola Kodu Girin**
- pip install opencv-python opencv-contrib-python opencv-python-headless opencv-contrib-python-headless
- Download - [opencv_python-3.4.5-cp37-cp37m-win32.whl](https://download.lfd.uci.edu/pythonlibs/r5uhg2lo/opencv_python-3.4.5-cp37-cp37m-win32.whl)
- Download - [numpy-1.16.0rc2+mkl-cp37-cp37m-win32.whl](https://download.lfd.uci.edu/pythonlibs/r5uhg2lo/numpy-1.16.0rc2+mkl-cp37-cp37m-win32.whl)
- pip install opencv_python-3.4.5-cp37-cp37m-win32.whl
- pip install numpy-1.16.0rc2+mkl-cp37-cp37m-win32.whl

## Resim Deposu
- image-net.org //resimlerin aldigi yer

## Algoritmaya Nesne Tanitma Alani
- mkdir data
- mkdir info
- opencv_createsamples -img positive_images/*.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.5 -maxyangle -0.5 -maxzangle 0.5 -num 15360 //3840 dosya icindeki resim sayisi
- opencv_createsamples -info info/info.lst -num 1282 -w 20 -h 20 -vec positives.vec
- opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 1000 -numStages 10 -w 20 -h 20

- nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1800 -numNeg 900 -numStages 5 -w 20 -h 20 & //numStages kac stage olustuysa o yazilacak.

- opencv_createsamples -img positive_images/ball4.png -bg bg.txt -info info/info.lst -pngoutput info -maxxangle 0.0 -maxyangle 0.0 -maxzangle 0.3 -w 48 -h 48 -num 3840
- opencv_createsamples -info info/info.lst -bg bg.txt -num 3840 -w 48 -h 48 -vec positives.vec
- opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1200 -numNeg 1000 -numStages 10 -w 48 -h 48


- opencv_createsamples -info sampleImageDirectory/positives.txt -bg negativeImageDirectory/negatives.txt -vec cropped.vec -num 1920 -w 48 -h 48

- nohup opencv_traincascade -data data -vec positives.vec -bg bg.txt -numPos 1000 -numNeg 600 -numStages 20 -mode ALL -precalcValBufSize 1024 -precalcIdxBufSize 1024 -featureType HAAR -minHitRate 0.995 -maxFalseAlarmRate 0.5 -numThreads 2 -w 48 -h 48 &
