#include <stdio.h>
#include <locale.h>

int main(int argc, char *argv[]){

    setlocale(LC_ALL, ".UTF-8");

    FILE *arquivo = fopen(argv[1], "rb");

    fseek(arquivo, 54, SEEK_SET);

    int byte_atual = 0;
    char caracteres_montados = 0;
    int bits_lidos = 0; 

    while ((byte_atual = fgetc(arquivo)) != EOF) {

        if(byte_atual % 2 == 0){
            caracteres_montados = caracteres_montados << 1;
        } else {
            caracteres_montados = (caracteres_montados << 1) + 1;
        }
        bits_lidos++;
        
        if(bits_lidos == 8){
            if(caracteres_montados == 0){
                break;
            } 
            
            printf("%c", caracteres_montados);
            caracteres_montados = 0;
            bits_lidos = 0; 
        }
        
    }

    fclose(arquivo);
    return 0; 
}