"""
Propósito: Dividir as questões concatenadas verticalmente pela faixa azul de início da questão
Autor: Alexandre Nassar de Peder
Data: 02/10/2025
Comentário: atualizar as linhas 122 e 123
Comentário 2: conferir o RGB da faixa azul no gimp. São em 0-100, não 0-255
Modificação: Validação dupla - primeiros 324px NÃO azuis + resto É azul
"""

from PIL import Image
import os

def converter_cor_gimp_para_rgb(gimp_r, gimp_g, gimp_b):
    """
    Converte valores do GIMP (0-100) para RGB (0-255)
    """
    r = int((gimp_r / 100) * 255)
    g = int((gimp_g / 100) * 255)
    b = int((gimp_b / 100) * 255)
    return (r, g, b)

def encontrar_faixa_azul(imagem, cor_alvo=(64, 193, 243), tolerancia=15, altura_faixa=10):
    """
    Encontra posições onde há uma faixa horizontal da cor especificada
    MODIFICAÇÃO: Validação dupla - primeiros 324px NÃO azuis + resto É azul
    """
    largura, altura = imagem.size
    pixels = imagem.load()
    
    posicoes_corte = []
    
    # Percorre a imagem de cima para baixo
    y = 0
    while y < altura - altura_faixa:
        # PRIMEIRA VERIFICAÇÃO: Verifica se há uma faixa de 'altura_faixa' pixels da cor alvo NO CENTRO
        faixa_encontrada = True
        
        for dy in range(altura_faixa):
            # Pega a cor do pixel atual (verifica no meio da imagem)
            pixel = pixels[largura // 2, y + dy]
            
            if len(pixel) == 4:  # RGBA
                r, g, b, a = pixel
            else:  # RGB
                r, g, b = pixel[:3]
            
            # Verifica se a cor está dentro da tolerância
            if (abs(r - cor_alvo[0]) > tolerancia or 
                abs(g - cor_alvo[1]) > tolerancia or 
                abs(b - cor_alvo[2]) > tolerancia):
                faixa_encontrada = False
                break
        
        # SEGUNDA VERIFICAÇÃO: Se encontrou faixa azul no centro, faz validação dupla
        if faixa_encontrada:
            # VALIDAÇÃO 1: Primeiros 324 pixels NÃO devem ser azuis (onde fica "QUESTÃO [XX]")
            primeiros_pixels_azuis = True
            for dx in range(324):  # Verifica os primeiros 324 pixels
                if dx >= largura:
                    break
                pixel = pixels[dx, y]
                if len(pixel) == 4:
                    r, g, b, a = pixel
                else:
                    r, g, b = pixel[:3]
                
                if (abs(r - cor_alvo[0]) <= tolerancia and 
                    abs(g - cor_alvo[1]) <= tolerancia and 
                    abs(b - cor_alvo[2]) <= tolerancia):
                    primeiros_pixels_azuis = True
                    break
                else:
                    primeiros_pixels_azuis = False
            
            # VALIDAÇÃO 2: A partir do 325º pixel até a borda direita DEVE ser continuamente azul
            resto_pixels_azuis = True
            for dx in range(325, largura):  # Verifica do 325º pixel até o final
                pixel = pixels[dx, y]
                if len(pixel) == 4:
                    r, g, b, a = pixel
                else:
                    r, g, b = pixel[:3]
                
                if (abs(r - cor_alvo[0]) > tolerancia or 
                    abs(g - cor_alvo[1]) > tolerancia or 
                    abs(b - cor_alvo[2]) > tolerancia):
                    resto_pixels_azuis = False
                    break
            
            # Só corta se PASSAR na validação dupla
            if not primeiros_pixels_azuis and resto_pixels_azuis:
                # Corta ANTES da faixa azul (no pixel anterior)
                posicao_corte = y - 13  # CORREÇÃO: definir a variável
                if posicao_corte < 0:  # Evitar posições negativas
                    posicao_corte = 0
                    
                posicoes_corte.append(posicao_corte)
                print(f"Faixa azul VÁLIDA encontrada começando em y={y}, cortando em y={posicao_corte}")
                # Pula a faixa inteira para evitar detecções múltiplas
                y += altura_faixa
            else:
                y += 1
        else:
            y += 1
    
    return posicoes_corte

def dividir_imagem_por_faixas(caminho_imagem, pasta_saida, cor_alvo=(64, 193, 243)):
    """
    Divide a imagem verticalmente cortando ANTES das faixas azuis
    """
    # Abre a imagem
    imagem = Image.open(caminho_imagem)
    largura, altura = imagem.size
    
    print(f"Imagem carregada: {largura}x{altura} pixels")
    
    # Encontra as posições das faixas azuis
    posicoes_corte = encontrar_faixa_azul(imagem, cor_alvo)
    
    if not posicoes_corte:
        print("Nenhuma faixa azul encontrada na imagem!")
        return
    
    print(f"Encontradas {len(posicoes_corte)} faixas azuis para corte")
    
    # Cria a pasta de saída se não existir
    os.makedirs(pasta_saida, exist_ok=True)
    
    # Corta as seções da imagem
    posicao_anterior = 0
    
    for i, posicao_corte in enumerate(posicoes_corte):
        # Garantir que a posição de corte é válida
        if posicao_corte <= posicao_anterior:
            continue
            
        # Corta a seção ANTES da faixa azul (do início anterior até o início da faixa)
        area_corte = (0, posicao_anterior, largura, posicao_corte)
        secao = imagem.crop(area_corte)
        
        # Salva a imagem cortada
        nome_arquivo = f"parte_{i+1:03d}.png"
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)
        secao.save(caminho_completo)
        print(f"Salvo: {caminho_completo} ({secao.width}x{secao.height}px)")
        
        # A próxima seção começa após o final desta faixa azul
        posicao_anterior = posicao_corte + 10  # Pula a faixa azul de 10 pixels
    
    # Corta a seção final (após a última faixa azul)
    if posicao_anterior < altura:
        area_corte = (0, posicao_anterior, largura, altura)
        secao = imagem.crop(area_corte)
        
        nome_arquivo = f"parte_{len(posicoes_corte)+1:03d}.png"
        caminho_completo = os.path.join(pasta_saida, nome_arquivo)
        secao.save(caminho_completo)
        print(f"Salvo: {caminho_completo} ({secao.width}x{secao.height}px)")

# Exemplo de uso
if __name__ == "__main__":
    # Configurações
    caminho_imagem = "2a14.png"  # Substitua pelo caminho da sua imagem
    pasta_saida = "questoes-paginas-2a14"
    
    # Converte a cor do GIMP (74.9, 91.8, 98.4) para RGB (0-255)
    cor_azul = converter_cor_gimp_para_rgb(74.9, 91.8, 98.4)
    print(f"Cor convertida: RGB{cor_azul}")
    
    # Executa a divisão
    dividir_imagem_por_faixas(caminho_imagem, pasta_saida, cor_azul)
    
    print("Divisão concluída!")