#!/bin/sh

grep "[0-9]$" $1 | awk '{print $2}' | termeter -d lcd
