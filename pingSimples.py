## Importa o módulo OS
import os

## Imprime o caractere '#' 60 vezes
print('#' * 60)

## Variável ip_or_host recebe o valor do host a ser pingado
ip_or_host = input('Digite o IP ou Host a ser verificado: ')

## Imprime o caractere '-' 60 vezes
print('-' * 60)

## Executa o ping
os.system('ping -c 6 '.format(ip_or_host))
