#! /bin/bash

./venv/bin/pip install black
clear

./venv/bin/black herodotus tests
