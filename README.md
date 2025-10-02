# categorizacao_questoes_enem
Projeto para categorização das questões do ENEM de acordo com os descritores e habilidades previstas na matriz de referência do exame.

# O QUE É?
Este projeto busca criar um banco de dados estruturado com questões do ENEM, categorizadas por:  
Conteúdo da questão (descritor)  
Habilidades avaliadas  
Metadados (ano, caderno, etc.)  

Matriz disponível em https://download.inep.gov.br/download/enem/matriz_referencia.pdf

Futuramente, também pretendo associar os descritores e habilidades à BNCC.

# COMO FUNCIONA?
1. Pré-processamento das questões  
Separação das imagens por questão.  
Organização dos dados básicos.  

2. Extração de texto  
Uso da API do Google Lens para OCR (reconhecimento de caracteres).  

3. Classificação semântica  
Envio do enunciado para uma LLM, identificando o conteúdo principal e a habilidade associada.  

4. Construção do banco de dados  
Possibilitando consultas como:  
Todas as questões de Trigonometria  
Todas as questões de História do Brasil  

# STATUS DO PROJETO
Semi-automático: diversos processos já foram automatizados via código, mas ainda existem etapas que precisam ser realizadas manualmente.  
Em desenvolvimento 🚧  

# FUTURO
Ampliar automações para reduzir o trabalho manual.  
Criar uma interface de pesquisa sobre o banco de questões.  
Explorar métodos alternativos de OCR e classificação.  