# 16. Criando um dicionário com 5 países e suas capitais
paises_capitais = {
    "Brasil": "Brasília",
    "Argentina": "Buenos Aires",
    "França": "Paris",
    "Japão": "Tóquio",
    "Alemanha": "Berlim"
}

# Exibindo a capital do Brasil
print("A capital do Brasil é:", paises_capitais["Brasil"])

# 17. Modificando a capital de um dos países
paises_capitais["Alemanha"] = "Berlim (atualizada)"

# 18. Adicionando um novo país e sua capital
paises_capitais["Canadá"] = "Ottawa"

# 19. Removendo um dos países do dicionário
del paises_capitais["França"]

# 20. Convertendo o dicionário em duas listas
paises = list(paises_capitais.keys())
capitais = list(paises_capitais.values())

# Exibindo os resultados
print("Dicionário atualizado:", paises_capitais)
print("Lista de países:", paises)
print("Lista de capitais:", capitais)


