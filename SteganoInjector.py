from PIL import Image
import sys

if len(sys.argv) < 2:
    print("Erro: Você precisa passar o nome da imagem!")
    sys.exit()

mensagem = str(input("Digite sua mensagem: "))

fila = ""

mensagem_bytes = mensagem.encode('utf-8')

for byte in mensagem_bytes:
    bits = format(byte, '08b') 
    fila += bits
    
fila += "00000000"

indice_bit = 0

imagem = Image.open(sys.argv[1]).convert('RGB')
largura, altura = imagem.size

for y in range(altura - 1, -1, -1):
    for x in range(largura):
        r, g, b = imagem.getpixel((x, y))
        if indice_bit < len(fila):
            if fila[indice_bit] == "0" and b % 2 == 1:
                    b -= 1 
            elif fila[indice_bit] == "1" and b % 2 == 0:
                    b += 1
            indice_bit += 1
        if indice_bit < len(fila):
            if fila[indice_bit] == "0" and g % 2 == 1:
                    g -= 1 
            elif fila[indice_bit] == "1" and g % 2 == 0:
                    g += 1
            indice_bit += 1
        if indice_bit < len(fila):
            if fila[indice_bit] == "0" and r % 2 == 1:
                    r -= 1 
            elif fila[indice_bit] == "1" and r % 2 == 0:
                    r += 1
            indice_bit += 1
        imagem.putpixel((x, y), (r, g, b))

imagem.save(f"escondido_{sys.argv[1]}")

print("Mensagem codificada com sucesso!")