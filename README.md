# Deploying Mnist digit classifier 
Deploying a basic mnist digit classifier using pytorch and flask

## Getting started
`git clone https://github.com/rtharungowda/mnist-flask-pytorch`</br>
Then
`cd mnist-flsk-pytorch`

## Installing dependencies
It is suggested to create a new virtual env</br>
Install venv `pip3 install python3-venv`</br>
Create a new venv in the folder mnist-flask-pytorch
```
python3 -m venv <venv>
. <venv>/bin/activate
```
</br>Then install dependencies, PS [Note](#note)
```
pip3 install -r requirements.txt
```
#### Note
Pytorch version (i.e, is torch and torchvision) support only cpu , as for deployment a gpu is always not available and the task is light weight
</br> Hence comment out `torch` `torchvision` and the first line and use the commands given in [Pytorch website](https://pytorch.org/) </br>
depeding on system and availability of cuda

### Full vedio tutorial
[Link](https://www.youtube.com/watch?v=bA7-DEtYCNM&feature=youtu.be)


### Creating Heruko account
[Heruko account](https://signup.heroku.com/) </br>
[Cli download](https://devcenter.heroku.com/articles/heroku-cli)
