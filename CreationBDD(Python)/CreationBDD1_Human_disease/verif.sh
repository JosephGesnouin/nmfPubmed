#!/bin/bash

size=$(wc -l outputTestAuto.txt)
array=( $size )
l=${array[0]}
cat -n human_disease_textmining_full.tsv | sed $l!d
cat -n outputTestAuto.txt | sed $l!d