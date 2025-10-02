"""
Propósito: Renomear as imagens do padrão parte_0xx.png para questao-xx.png
Autor: Alexandre Nassar de Peder
Data: 02/10/2025
Comentário 1: atualizar as linhas 11, 20 (comentário para entender a lógica), 21, 22 e 23
Comentário 2: geralmente, as imagens parte_001.png das pastas é um lixinho
"""
import os

def renomear_questoes_simples():
    pasta = "questoes-paginas-29a31"
    
    if not os.path.exists(pasta):
        print(f"Pasta {pasta} não encontrada!")
        return
    
    # Mapeamento direto dos nomes antigos para os novos
    mapeamento = {}
        
    # Questões normais: parte_002 a parte_032 -> questao-46 a questao-76
    for i in range(2, 12+1):
        antigo = f"parte_{i:03d}.png"
        novo = f"questao-{i+78}.png"
        mapeamento[antigo] = novo
    
    # Aplicar o renomeamento
    for antigo, novo in mapeamento.items():
        caminho_antigo = os.path.join(pasta, antigo)
        caminho_novo = os.path.join(pasta, novo)
        
        if os.path.exists(caminho_antigo):
            os.rename(caminho_antigo, caminho_novo)
            print(f"Renomeado: {antigo} -> {novo}")
        else:
            print(f"Arquivo não encontrado: {antigo}")
    
    print("Renomeação concluída!")

# Executar
if __name__ == "__main__":
    renomear_questoes_simples()