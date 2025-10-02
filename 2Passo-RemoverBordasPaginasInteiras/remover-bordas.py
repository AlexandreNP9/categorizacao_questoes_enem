"""
Propósito: remover as bordas das páginas completas. Tive que contar pixels.
Autor: Alexandre Nassar de Peder
Data: 02/10/2025.
Comentários: pode excluir a pagina_enem_1.png porque é a capa, e o pagina_enem_32.png porque é o rascunho da redação
"""

from PIL import Image
import os

pasta_imagens = "imagens"
pasta_saida = "recortadas"

os.makedirs(pasta_saida, exist_ok=True)

for nome_arquivo in os.listdir(pasta_imagens):
    if nome_arquivo.lower().endswith(".png"):
        caminho_entrada = os.path.join(pasta_imagens, nome_arquivo)
        imagem = Image.open(caminho_entrada)

        largura, altura = imagem.size

        caixa_corte = (276, 390, largura - 276, altura - 280)
        imagem_cortada = imagem.crop(caixa_corte)

        caminho_saida = os.path.join(pasta_saida, nome_arquivo)
        imagem_cortada.save(caminho_saida)

print("Recorte das bordas concluído.")