#!/usr/bin/env bash

pkill -f python
cd backend
activate () {
  . $PWD/python-venv/bin/activate
}
activate
python api.py &
