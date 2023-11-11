# robo-cleaner

# ATIVIDADE AVALIATIVA - AGENTE RACIONAL

Implementar um Agente Racional que limpa um quarto com o mínimo possível de ações, e o objetivo é que todo o ambiente esteja limpo e o agente retorne ao lar (localização de início A). 

# Conhecimento Prévio:
• Todo o ambiente é dividido em quadrados de 4 por 4.

• O agente (aspirador de pó) tem uma energia inicial de 100 pontos.

• O agente pode se mover apenas para o Norte, Sul, Leste ou Oeste. Ele não pode se
mover diagonalmente.

• Cada ação custa 1 ponto de energia. Por exemplo, cada movimento custa 1 ponto de
energia, cada aspiração custa 1 ponto de energia.

• O agente possui uma bolsa que coleta sujeira. A capacidade máxima é de 10.

• Após cada aspiração, o agente precisa verificar sua bolsa; se estiver cheia, ele deve voltar para Casa (localização A), esvaziar a bolsa e começar a aspirar novamente.

<h1 align="center"> PARTE A </h1>

# PEAS (Medida de Desempenho, Ambiente, Atuadores e Sensores).

|AGENTE |MEDIDA DE DESEMPENHO | AMBIENTE| ATUADORES | SENSORES |
| -------- | -------- | -------- |-------- | -------- |
|ASPIRADOR DE PÓ |A medida de desempenho é o numero de ações necessária para limpar todo o ambiente e retornar à localização de inicio A. O objetivo é minimizar este número de ações.| O ambiente consiste em um quarto com varias localizações (de A a P). Cada localização pode estar limpa ou suja.| Os atuadores do agente podem ser definidos como a capacidade de mover-se para diferentes localizações (motor) e um aspirador para limpar a sujeira e retornar a localização de início A. | Os sensores do agente permitem que ele detecte se uma localização está suja e determine sua própria posição no ambiente.

### EQUIPE:
1. Anne Caroline Pinho Valentim
2. Vitor Oliveira Rattes
