#!/bin/bash

while :; do
	size=$(wc -l outputTestAuto.txt)
	array=( $size )
	echo ${array[0]}
	python3 automatique.py ${array[0]}
	sleep 80
done
