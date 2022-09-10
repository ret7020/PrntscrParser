# PrntScr Parser
Download random images from prntscr(imgur). The file name is generated randomly, then if there is such a file on the server, then it is saved to `images_png` folder. This script is multithreaded.

## How to use
Use `main.py` to parse images from imgur
```
python3 main.py <NUMBER OF THREADS>
```
Then you can visualize random images from parsed using web ui.(make sure that script parsed at least 3 images, before run webui).
</br> You have to install flask(check `requirements.txt`)
```
python3 webui.py
```
You can change some webui settings in `config.py`
```
IMAGES_PATH = "./images_png" # where images saved
FLASK_HOST = "0.0.0.0" # host to run server
FLASK_PORT = "8080" # port for server
```

## Screenshot
![image](https://user-images.githubusercontent.com/55328925/189493950-9b6fc7e9-50c5-49eb-98ce-a41ecb955e9c.png)


