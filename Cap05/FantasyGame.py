inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }

def displayInventory(inventory):
    print('Inventário:')
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal += v
        print(v, k, sep = ' ')
    print('o total de itens é de:', itemTotal, sep = ' ')

displayInventory(inventory)