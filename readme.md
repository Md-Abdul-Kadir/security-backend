# How to run the backend

pip install -r requirement.txt

Download pretrained models from [Link text Here](https://drive.google.com/drive/u/0/folders/1-KiwRxHOWfSFxlANekYvvLbRCUoMgX2Y) and place then in the `Models` folder (if there is not `Models` folder then create one folder named as `Models` and another folder named `Uploads` for uploading the files sent from the client side application)

python3 app.py (Run the application)

You will get a `public link` of proxy server put that link in the `axios` instance in the front-end `/utils/axios.js` file in order to connect the front-end with the back-end

or simply comment the `38 no line` of the app.py file in case if you don't want to use a proxy server

`public_url = ngrok.connect(port,"http",remote_addr="http://127.0.0.1:3000").public_url
`

then start the project

in case if you want to run the project in debug mode then simply run the command

flask --debug run

but make sure that you are not using a proxy server while running the project in debug mode

in case if you want to run the project in google colab then follow this [notebook](https://colab.research.google.com/drive/1T0PTdpvAACpkrPFAYuhrDTH2o-nzLy7V#scrollTo=xvqEMFuVEg1p) instructions

But remember, if you are running the project on google colab you need to use the proxy server so make sure in the project the `line no 38` is not commented
