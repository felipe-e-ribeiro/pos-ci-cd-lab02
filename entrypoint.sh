#!/bin/bash

if [ -z "$1" ] || [ -z "$2" ] || [ -z "$3" ]; then
    echo "Usage: $0 <preco> <desconto> <aliquota>"
    exit 1
fi

python /app/calculadora.py --preco $1 --desconto $2 --aliquota $3