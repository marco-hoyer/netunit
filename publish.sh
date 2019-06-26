#!/usr/bin/env bash

rm dist/*
python setup.py sdist
python -m twine upload dist/netunit-*.tar.gz
