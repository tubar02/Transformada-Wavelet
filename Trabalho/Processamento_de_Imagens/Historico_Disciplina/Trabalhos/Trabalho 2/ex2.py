import my_image_lib_0_2 as img

def imag_e_hist(imagem, titulo = ''):
    img.print_grayscale_image(imagem)
    img.plota_histograma(imagem, titulo)

def main():
    imagem = img.Image("Trabalho 2\\Input\\leaf.pgm")
    imag_e_hist(imagem)
    
    normalizado = img.normaliza_hist(imagem.hist)
    img.plota_histograma(imagem, "Histograma Normalizado", normalizado) 

    escurece = imagem.transformacao_linear("Trabalho 2\\Output\\leaf_dark.pgm", 1, -120)
    
    imagem2 = img.Image("Trabalho 2\\Input\\chest.pgm")
    
    menos_contr = imagem2.transformacao_linear("Trabalho 2\\Output\\chest_less.pgm", 0.5, 60)
    
    equaliza1 = imagem.transformacao_linear("Trabalho 2\\Output\\leaf_equalize.pgm", 2.2, -300)
    
    equaliza2 = imagem2.transformacao_linear("Trabalho 2\\Output\\chest_equalize.pgm", 1.25, -30)
    
    mask_bin = imagem.mascara_bin(209)
    mascarada = imagem.aplica_mascara("Trabalho 2\\Output\\leaf_mask.pgm", mask_bin)

    dict_img = {escurece: "Histograma da Imagem Escurecida",
                imagem2: "Histograma da Imagem 2",
                menos_contr: "Histograma da Imagem 2 com menos Contraste",
                equaliza1: "Histograma da Imagem Equalizada",
                equaliza2: "Histograma da Imagem 2 Equalizada",
                mascarada: "Histograma da Imagem Mascarada"}
    
    for k in dict_img:
        imag_e_hist(k, dict_img[k])

main()