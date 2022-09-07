#! /bin/bash

./venv/bin/flit install
./venv/bin/pip install coverage
./venv/bin/coverage run --source=./herodotus -m pytest
clear

./venv/bin/coverage report 