"""
Propósito: concatenas verticalmente as imagens de cada pasta vinda do passo 5
Autor: Alexandre Nassar de Peder
Data: 02/10/2025
Comentários: atualizar as linhas 12 e 13 para cada pasta
Comnetário 2: não fazer para a página 15, 19 e 28. Só criar a pasta manualmente e adicionar a imagem.
"""

from PIL import Image
import os
import re

pasta_imagens = "paginas-29a31"
pasta_saida = "29a31"
os.makedirs(pasta_saida, exist_ok=True)

# Função para extrair o número da página e ordenar corretamente
def get_sort_key(nome_arquivo):
    # Extrai o número da página
    numero = int(re.search(r'pagina_enem_(\d+)_', nome_arquivo).group(1))
    # Define a ordem: esquerda primeiro (0), depois direita (1)
    lado = 0 if 'esquerda' in nome_arquivo else 1
    return (numero, lado)

# Pegar e ordenar as imagens corretamente
arquivos = [f for f in os.listdir(pasta_imagens) if f.endswith('.png')]
arquivos.sort(key=get_sort_key)

# Abrir todas as imagens na ordem correta
imagens = []
for arquivo in arquivos:
    caminho = os.path.join(pasta_imagens, arquivo)
    imagens.append(Image.open(caminho))
    print(f"Adicionando: {arquivo}")  # Para verificar a ordem

# Encontrar a largura máxima
largura_max = max(img.width for img in imagens)

# Concatenar verticalmente
altura_total = sum(img.height for img in imagens)
imagem_final = Image.new('RGB', (largura_max, altura_total))

y = 0
for img in imagens:
    imagem_final.paste(img, (0, y))
    y += img.height

# Salvar
imagem_final.save(os.path.join(pasta_saida, 'todas_juntas.png'))
print("Imagens concatenadas na ordem correta!")
print(f"Ordem dos arquivos: {arquivos}")