import requests

resp = requests.post('https://mnist-pytorch-flask.herokuapp.com/predict', files={'file':open('seven.png','rb')})
print(resp.text)