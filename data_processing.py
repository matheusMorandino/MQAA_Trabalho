import pandas as pd

#importando os dados do .csv para o dataframe 'pokemons'
pokemons = pd.read_csv("Pokemon.csv")
#visualizando as 5 primeiras entradas
print(pokemons.head())

# pokemons.loc[pokemons['Type 2'].isnull(), 'Type 2'] = "None"

#carregando em listas cada série de tipos de pokemons
type_1 = pokemons.get("Type 1").tolist()
type_2 = pokemons.get("Type 2").tolist()     

#lendo cada elemento em cada lista
for i in range(0, len(type_1), 1):
    #verificando se um elemento na lista de 'Type_2' é NaN
    if(isinstance(type_2[i], float)):
        #Se for subistituir pelo tipo 'None'
        type_2[i] = "None"

#convertendo cada lista de volta em séries
type_1 = pd.Series((i for i in type_1))
type_2 = pd.Series((i for i in type_2))

#retirando a coluna da série 'Type_2' antiga
del pokemons["Type 2"]
#inserindo a nova série de 'Type_2'
pokemons.insert(3, "Type 2", type_2, True)

#Visualizando os novos 5 primeiros elementos
print("\n")
print(pokemons.head())

#Carregando o novo dataframe em uma arquivo novo chamado 'Pokemon_new.csv'
pokemons.to_csv("Pokemon_new.csv", sep=',', index=False)