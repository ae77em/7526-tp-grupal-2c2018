# 7526-tp-grupal-2c2018
Resolución de trabajo práctico grupal de Simulación - FIUBA - 2c2018

# Setup (Ubuntu)

## 1º Instalar pip

`sudo apt install python-pip`

`sudo python -m pip install --upgrade pip setuptools wheel`

## 2º Instalar librerías necesarias en el ambiente del usuario (*)

* simpy

`python -m pip install -U simpy --user`

* scipy

`python -m pip install -U scipy --user`

* sympy

`python -m pip install -U sympy --user`

(*) La opción `--user` indica que se instala para el usuario actual. Me daba problemas usando el IDE cuando instalaba cosas como super user.
