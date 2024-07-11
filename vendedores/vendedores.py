class Vendedor:
    def __init__(self, nome: str, tipo: str, produtos: list, raça: str):
        self.produtos = produtos
        self.nome     = nome
        self.tipo     = tipo
        self.raça     = raça

villager = Vendedor(nome='Villager do Mine', tipo='Sealer of Potions', produtos=['Poção de Vida', 'Poção de Cura', 'Poção de Força'], raça='Bruxo')

print(f'Nome: {villager.nome} // Tipo: {villager.tipo} // Raça: {villager.raça}')

for produtos in villager.produtos:
    print(produtos)