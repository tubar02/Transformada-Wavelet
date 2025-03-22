import my_image_lib_0_1 as img

def main():
    imagem = img.Image("Trabalho 1\\Input\\gourds.pgm")

    img.print_grayscale_image(imagem)
    img.print_image(imagem)
    print(imagem.dimension)
    print(imagem.max, imagem.min)    
    img.plota_perfil_linha(imagem, int((3/4) * imagem.nlinha))

main()