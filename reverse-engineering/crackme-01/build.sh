#!/bin/bash
# Compile crackme dari source
gcc -O0 -fno-stack-protector -o crackme crackme.c
echo "[*] Compiled: ./crackme"
chmod +x crackme
