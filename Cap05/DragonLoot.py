inventory = {'rope': 1, 'torch': 6, 'gold coin': 42, 'dagger': 1, 'arrow': 12 }
dragonLoot = ['gold coin', 'dagger', 'gold coin', 'gold coin', 'ruby']
treasureChest = ['mirror shield', 'broadsword', 'cloak', 'boots']

#imprime um inventário
def displayInventory(inventory):
    print('Inventário:')
    itemTotal = 0
    for k, v in inventory.items():
        itemTotal += v
        print(v, k, sep = ' ')
    print('o total de itens é de:', itemTotal, sep = ' ')

#adiciona uma lista de itens em um inventário
def addToInventory(inventory, loot):
    for item in loot:
        if item in inventory:
            inventory[item] += 1
        else:
            inventory.setdefault(item, 0)
            inventory[item] += 1
    return inventory

displayInventory(inventory)

inventory = addToInventory(inventory, dragonLoot)
print()
displayInventory(inventory)

inventory = addToInventory(inventory, treasureChest)
print()
displayInventory(inventory)