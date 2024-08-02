#!/bin/bash
pip install pipenv
pipenv install

aws sts get-caller-identity
aws ec2 describe-instances --region us-east-2

pipenv run python main.py

