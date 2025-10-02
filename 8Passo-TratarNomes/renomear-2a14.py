import os

def renomear_questoes_simples():
    pasta = "questoes-paginas-2a14"
    
    if not os.path.exists(pasta):
        print(f"Pasta {pasta} não encontrada!")
        return
    
    # Mapeamento direto dos nomes antigos para os novos
    mapeamento = {}
    
    # Inglês: parte_002 a parte_006 -> questao-1-ingles a questao-5-ingles
    for i in range(2, 7):
        antigo = f"parte_{i:03d}.png"
        novo = f"questao-{i-1}-ingles.png"
        mapeamento[antigo] = novo
    
    # Espanhol: parte_007 a parte_011 -> questao-1-espanhol a questao-5-espanhol
    for i in range(7, 12):
        antigo = f"parte_{i:03d}.png"
        novo = f"questao-{i-6}-espanhol.png"
        mapeamento[antigo] = novo
    
    # Questões normais: parte_001 a parte_012 -> questao-6 a questao-34
    for i in range(1, 12):
        antigo = f"parte_{i:03d}.png"
        novo = f"questao-{i-6}.png"
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