import random
import numpy as np
import time
environment = np.random.choice([0, 1], size=(4, 4), p=[0.5, 0.5])

class RoboAspirador:
    def _init_(self):
        # Definindo o ambiente
        self.ambiente = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P']
        self.posicao = random.choice(self.ambiente)  # Posição inicial aleatória
        self.energia = 100
        self.bolsa_sujeira = 0
        self.capacidade_maxima_bolsa = 10

    def acao_tomar(self):
        if self.bolsa_sujeira == self.capacidade_maxima_bolsa:
            return 'voltar_casa'
        elif self.energia <= 0:
            return 'sem_energia'
        elif self.energia > 0 and self.bolsa_sujeira < self.capacidade_maxima_bolsa:
            return random.choice(['mover', 'aspirar'])

    def direcao_seguir(self):
        direcoes_possiveis = ['Norte', 'Sul', 'Leste', 'Oeste']
        return random.choice(direcoes_possiveis)

    def aspirar(self):
        print(f"Aspirando sujeira em {self.posicao}")
        self.bolsa_sujeira += 1
        self.energia -= 1

        if self.bolsa_sujeira == self.capacidade_maxima_bolsa:
            print("Bolsa cheia. Voltando para casa.")
            self.voltar_para_casa()

    def mover(self, direcao):
        print(f"Movendo para {direcao}")
        self.posicao = self.nova_posicao(direcao)
        self.energia -= 1

    def voltar_para_casa(self):
        rota = self.identificar_rota_casa()
        for direcao in rota:
            self.mover(direcao)
        self.esvaziar_bolsa()

    def identificar_rota_casa(self):
        # Simplesmente volta para A
        return ['Norte'] * (ord(self.posicao) - ord('A'))

    def esvaziar_bolsa(self):
        print("Esvaziando a bolsa.")
        self.bolsa_sujeira = 0

    def objetivo_alcancado(self):
        return self.bolsa_sujeira == 0 and self.energia > 0

    def nova_posicao(self, direcao):
        if direcao == 'Norte':
            return chr(max(ord(self.posicao) - 4, ord('A')))
        elif direcao == 'Sul':
            return chr(min(ord(self.posicao) + 4, ord('P')))
        elif direcao == 'Leste':
            return chr(min(ord(self.posicao) + 1, ord('P')))
        elif direcao == 'Oeste':
            return chr(max(ord(self.posicao) - 1, ord('A')))

    time.sleep(1)

    # Função principal
def main():
    robo = RoboAspirador()

    while not robo.objetivo_alcancado():
        print(f"Posição atual: {robo.posicao}, Energia: {robo.energia}, Bolsa: {robo.bolsa_sujeira}")

        acao = robo.acao_tomar()

        if acao == 'mover':
            direcao = robo.direcao_seguir()
            robo.mover(direcao)
        elif acao == 'aspirar':
            robo.aspirar()
        elif acao == 'voltar_casa':
            robo.voltar_para_casa()
        elif acao == 'sem_energia':
            print("O robô ficou sem energia. Tarefa interrompida.")
            break

    print("Tarefa concluída! O robô voltou para casa.")
    print(f"Energia restante: {robo.energia}, Bolsa: {robo.bolsa_sujeira}")