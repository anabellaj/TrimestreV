# Imprimir el cliente mas rico
def get_wealth (accounts):
    max_wealth = 0
    for lista in accounts:
        if sum(lista)> max_wealth:
            max_wealth = sum(lista)
    return max_wealth

def main():
    accounts = [
        [1,2,3],
        [3,2,1]
    ]
    wealth = get_wealth(accounts)
    print ('The max wealth is', wealth)

main()