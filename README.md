# 🇧🇷 Projeto Esteganografia BMP (Python & C) 

Este projeto implementa um sistema de esteganografia utilizando a técnica LSB (Least Significant Bit - Bit Menos Significativo) em imagens no formato `.bmp`. 

O projeto demonstra a interoperabilidade entre uma linguagem de alto nível (Python), usada para manipular a imagem e injetar a mensagem, e uma linguagem de baixo nível (C), usada para fazer o parsing binário puro do arquivo e extrair o texto oculto.

## Como Funciona?

1. **Injeção (`SteganoInjector.py`):** 
   * Converte o texto da mensagem para bytes UTF-8 (suportando acentos).
   * Abre a imagem BMP e, seguindo a estrutura nativa do arquivo (ordem de pixels BGR e leitura de baixo para cima), altera o bit menos significativo de cada canal de cor para esconder a fila de bits da mensagem.
   * Salva uma nova imagem com o prefixo `escondido_`.

2. **Extração (`SteganoReader.C`):**
   * Abre o arquivo BMP gerado em modo binário puro.
   * Pula os 54 bytes do cabeçalho estrutural do BMP para alcançar a matriz de pixels.
   * Varre os bytes, extrai o bit LSB de cada um e reconstrói os caracteres originais usando operações de bitwise.
   * Interrompe a leitura ao encontrar o caractere nulo, finalizando a exibição da mensagem secreta.

## Como Executar

### 1. Ocultar a mensagem (Python)
No terminal, execute o injetor passando a imagem alvo como argumento:
'''bash
py SteganoInjector.py sua_imagem.bmp
Após isso, digite a sua mensagem secreta quando o terminal solicitar e dê Enter. Isso gerará um novo arquivo chamado escondido_sua_imagem.bmp com os bits ocultos.

### 2. Revelar a mensagem (C) 
Primeiro, compile o código do leitor utilizando o gcc:
gcc SteganoReader.C -o SteganoReader
⚠️ Antes de rodar o decodificador, se você estiver utilizando o Windows PowerShell, execute o comando abaixo para configurar a janela do terminal para o padrão UTF-8. Isso garante que letras com acentos sejam renderizadas corretamente na tela:
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Agora, execute o programa compilado passando a imagem modificada para extrair o segredo:
.\SteganoReader.exe escondido_sua_imagem.bmp
⚠️(Caso esteja utilizando um terminal baseado em Linux/Git Bash, utilize ./SteganoReader escondido_sua_imagem.bmp).

----------------------------------------------------------------------------------------------------------

# 🇺🇸 BMP Steganography Project (Python & C) 

This project implements a steganography system using the **LSB (Least Significant Bit)** technique in `.bmp` images. 

The project demonstrates interoperability between a high-level language (Python), used to manipulate the image and inject the message, and a low-level language (C), used to perform pure binary parsing of the file and extract the hidden text.

## How It Works

1. **Injection (`SteganoInjector.py`):**
   * Converts the message text into UTF-8 bytes (supporting accents and special characters).
   * Opens the BMP image and, following the file's native structure (BGR pixel order and bottom-up reading), alters the least significant bit of each color channel to hide the message's bit stream.
   * Saves a new image with the `escondido_` prefix.

3. **Extraction (`SteganoReader.C`):**
   * Opens the generated BMP file in pure binary mode (`rb`).
   * Skips the 54 bytes of the BMP structural header (`fseek`) to reach the pixel matrix.
   * Scans the bytes, extracts the LSB bit from each one, and reconstructs the original characters using bitwise operations (**Bit Shift `<<`**).
   * Stops reading upon encountering the null character (`\0`), finalizing the display of the secret message.

## How to Run

### 1. Hide the Message (Python)
In the terminal, run the injector script passing the target image as an argument:
'''bash
py SteganoInjector.py your_image.bmp
After that, type your secret message when prompted by the terminal and press Enter. This will generate a new file named escondido_your_image.bmp containing the hidden bits.

### 2. Reveal the Message (C)
First, compile the reader code using gcc:
gcc SteganoReader.C -o SteganoReader
⚠️ Before running the decoder, if you are using Windows PowerShell, run the command below to configure the terminal window to the UTF-8 standard. This ensures that letters with accents are rendered correctly on the screen:
[Console]::OutputEncoding = [System.Text.Encoding]::UTF8
Now, execute the compiled program passing the modified image to extract the secret text:
.\SteganoReader.exe escondido_your_image.bmp
⚠️(If you are using a Linux-based terminal or Git Bash, use ./SteganoReader escondido_your_image.bmp).
