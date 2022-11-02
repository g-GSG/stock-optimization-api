# Example of use of the Pulp libray for 15-382
# Modeling and solution of a simple knapsack problem
# Giulia Chiucchi e Gustavo Gomes

from pulp import *
import time
import json

def optimize(items, maxVolume): 

    print(items)

    # number of items
    itemCount = len(items)

    # Initialize the problem and specify the type
    model = LpProblem(name="Maximizar Lucro", sense=LpMaximize)

    # Initialize the decision variables
    x = LpVariable.dicts('Quantidade de produtos', range(itemCount), lowBound = 0, cat=LpInteger)

    # Adicionar funcao objetivo
    model += lpSum([ x[i] * items[i]["lucro"] for i in range(itemCount) ]) # "Objetivo: Maximizar lucro"

    # Adicionar restricoes ao modelo
    for i in range(itemCount):
        model += x[i] <= items[i]["quantidade"] # "Quantidade de produtos <= quantidade disponível"
    
    model += (lpSum([ x[i] * items[i]["volume"] for i in range(itemCount) ]) <= maxVolume, "VolumeProds")

    model.solve()

    # The optimised objective function value is printed to the screen
    print(value(model.objective))

    for var in model.variables():
        print(f"{var.name}: {var.value()}")

    used_items = []

    for i in range(itemCount):
        item = {
            "nome": items[i]["nome"],
            "quantidade": x[i].varValue,
            "volume": items[i]["volume"],
            "lucro": items[i]["lucro"]
        }
        used_items.append(item)
        
    # Return the solution
    return json.dumps({
        "status": LpStatus[model.status],
        "lucro": value(model.objective),
        "max_volume": maxVolume,
        "items": used_items 
    })