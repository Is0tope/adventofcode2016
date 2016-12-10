#!/bin/bash
# creates a base folder for a numbered challenge
mkdir $1
cd $1
printf "with open('test.txt') as f:\n    pass" > $1a.py
echo "" > test.txt
echo "" > input.txt
echo "" > $1b.py
