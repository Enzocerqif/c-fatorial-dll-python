# Tutorial: Gerar DLL em C e Usar no Python

Este repositório contém um exemplo de integração entre C e Python utilizando uma função recursiva de cálculo de fatorial. O código em C é compilado em uma DLL (Dynamic Link Library) que é carregada no Python através do módulo `ctypes`. O objetivo deste projeto é demonstrar como criar bibliotecas em C e utilizá-las diretamente em scripts Python.

## Funcionalidades

- Implementação de uma função recursiva de fatorial em C.
- Compilação de código C em uma DLL.
- Integração da DLL com Python usando o módulo `ctypes`.

## Requisitos

- **Python**: Certifique-se de ter instalado o Python, com uma versão compatível com o GCC (compilador).
  - Se o Python for de 64 bits, você precisará do compilador GCC de 64 bits. Da mesma forma, se o Python for de 32 bits, o GCC deve ser a versão de 32 bits.
  
- **Compilador GCC**: Para compilar o código em C e gerar a DLL.
  - No Windows, você pode usar o **MinGW-w64** para versões de 64 bits ou **MinGW** para 32 bits.
  
  Para verificar se seu Python e GCC estão na mesma arquitetura, use os seguintes comandos:

  - Para verificar se o Python é 32 ou 64 bits:
    ```bash
    python -c "import struct; print(struct.calcsize('P') * 8)"
    ```

  - Para verificar a arquitetura do GCC:
    ```bash
    gcc -v
    ```

## Passo 1: Escreva o código em C

Crie um arquivo chamado `fatorial.c` com o seguinte código:

```c
#include <stdio.h>

__declspec(dllexport) int fatorial(int n) {
    if (n == 0 || n == 1) {
        return 1;
    } else {
        return n * fatorial(n - 1);
    }
}

## Passo 2: Gerar a DLL

Para compilar o código em C e gerar a DLL, siga os passos abaixo:

1. Abra o terminal no diretório onde o arquivo `fatorial.c` está localizado.
2. Execute o seguinte comando para compilar e gerar a DLL:

    ```bash
    gcc -shared -o fatorial.dll fatorial.c
    ```

   Este comando gera o arquivo `fatorial.dll`, que contém a função `fatorial`.

## Passo 3: Carregar a DLL no Python

Agora, você pode usar a função `fatorial` no Python através do módulo `ctypes`.

Crie um arquivo Python, por exemplo, `test_fatorial.py`, com o seguinte código:

```python
import ctypes as c

# Carregar a DLL
dll = c.CDLL('./fatorial.dll')

# Definir o tipo de argumento e o tipo de retorno da função fatorial
dll.fatorial.argtypes = (c.c_int,)
dll.fatorial.restype = c.c_int

# Usar a função fatorial da DLL
n = 6
fat = dll.fatorial(n)
print(f"O fatorial de {n} é: {fat}")

## Como o Código Funciona

### Código em C

- A função `fatorial` é recursiva e calcula o fatorial de um número inteiro positivo `n`. Se `n` for 0 ou 1, a função retorna 1. Caso contrário, ela chama a si mesma até que `n` seja reduzido a 1.
  
- O `__declspec(dllexport)` é utilizado para exportar a função, o que significa que ela ficará disponível para outros programas (como o Python) quando a DLL for carregada.

- O comando `gcc -shared` gera um arquivo de biblioteca dinâmica (`fatorial.dll`) que contém a função fatorial, disponível para ser usada por outros programas.

### Código em Python

- `ctypes.CDLL` carrega a biblioteca dinâmica gerada (`fatorial.dll`), permitindo acesso às funções exportadas.

- `dll.fatorial.argtypes` define os tipos dos argumentos que a função `fatorial` aceita. No caso, um único argumento do tipo `int` (`c.c_int`).

- `dll.fatorial.restype` define o tipo de retorno da função `fatorial`, que é um `int` (`c.c_int`).

- Finalmente, chamamos a função `dll.fatorial(n)` no Python, passando um valor inteiro como argumento e imprimimos o resultado.

## Observações

- Certifique-se de que o Python e o compilador GCC estejam na mesma arquitetura (64 bits ou 32 bits).
  
- Ao compilar no Windows, tenha certeza de que as bibliotecas do MinGW ou MinGW-w64 estão configuradas corretamente no caminho do sistema para que o GCC possa ser invocado a partir do terminal.

- Você pode carregar a DLL no Python diretamente com o caminho relativo (`'./fatorial.dll'`) ou com o caminho completo onde a DLL está armazenada.



