#!/usr/bin/env bash

cd backend
activate () {
  . $PWD/python-venv/bin/activate
}
activate
python api.py &
cd ../frontend
yarn run dev &
