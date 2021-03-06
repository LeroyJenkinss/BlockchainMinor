from blockChain import *

leading_zero = 2

dataG = 'Root'
data1 = 'It is B1'
data2 = 'It is B2'
data3 = 'It is B3'
data4 = 'It is B4'
data5 = 'It is B5'

if __name__ == '__main__':

    Gn = CBlock(dataG, None)
    B1 = CBlock(data1, Gn)
    B2 = CBlock(data2, B1)
    B3 = CBlock(data3, B2)
    B4 = CBlock(data4, B3)

    print('\n--- Blocks are created --- Hashes and Nonces should not match!')
    print('begin first set')

    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")
    print('end first set')
    print('---------------------------------------------')
    print('begin second set')
    for b, name in [(Gn, 'Gn'), (B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        print(f'\nMining {name} ...')
        b.mine(leading_zero)

    print('\n--- Blocks are mined --- Hashes and Nonces must match!')
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")

    print('end second set')
    print('---------------------------------------------')
    

    data3t = 'It is B3t'
    B3.data = data3t
    
    print('\n--- Block3 is tampered --- Hashes and Nonces of blocks after B3 should not match!')
    print('begin third set')
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")

    print('end third set set')
    print('-------------------------------------------------')
    for b, name in [(Gn, 'Gn'), (B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        print(f'\nMining {name} ...')
        b.mine(leading_zero)
    print('begin fouth set set')
    
    print('\n--- Blocks are mined again --- Hashes and Nonces must match again!')
    for b, name in [(B1, 'B1'), (B2, 'B2'), (B3, 'B3'), (B4, 'B4')]:
        if b.is_valid_hash():
            print("Success! "+name+" hash matches")
        else:
            print("Fail! " +name+" hash does not match")
    print('end fourth set set')
    print('-------------------------------------------------')