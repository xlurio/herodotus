#! /bin/bash

./venv/bin/flit install
./venv/bin/pip install pylint
clear

./venv/bin/pylint --disable=R0903 herodotus tests