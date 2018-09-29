# 7526-tp-grupal-2c2018
Resolución de trabajo práctico grupal de Simulación - FIUBA - 2c2018

# Setup (Ubuntu)

## 1º Instalar pip

`sudo apt install python-pip`

`sudo python -m pip install --upgrade pip setuptools wheel`

## 2º Instalar librerías necesarias en el ambiente del usuario (*)

* pylint

`python -m pip install -U "pylint<2.0.0" --user`

* matplotlib

`python -m pip install -U matplotlib --user`

* python-tk

`python -m pip install -U python-tk --user`

* plotly

`python -m pip install plotly --user`

* rope

`python -m pip install -U rope --user`

* autopep8

`python -m pip install -U autopep8 --user`

* scipy

`python -m pip install scipy`

(*) La opción `--user` indica que se instala para el usuario actual. Me daba problemas usando el IDE cuando instalaba cosas como super user.
