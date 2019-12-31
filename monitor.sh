#!/bin/sh

ping 8.8.8.8 | ts %s | sed -u 's/time=//' | stdbuf -o0 grep -v "PING" | tee pingstats
