from Signature import *

from Transaction import *

def print_transaction(tx_name, tx):
    count = 0
    print('-------------------')
    print(f'-- {tx_name}:')
    for i in range(len(tx.inputs)):
        for b in range(len(keys_list)):
           
            if tx.inputs[i][0] == keys_list[b][2]:
                print(f'In[{i+1}] {keys_list[b][0]} send {tx.inputs[i][1]} coin')
    
    for i in range(len(tx.outputs)):
        for b in range(len(keys_list)):
            if tx.outputs[i][0] == keys_list[b][2]:
                print(f'Out[{i+1}] {keys_list[b][0]} recieved {tx.outputs[i][1]} coin')
    
    for sign in tx.sigs:
        for key in keys_list:
            ver = verify(tx.concateLists(), sign, key[2])
            if ver == True:
                print(f'{tx_name} is signed by {key[0]}')

if __name__ == "__main__":
    
    keys_list =[]

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', mara_prv, mara_pbc))

    # --------------------------------------
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 1)
    Tx1.add_output(mike_pbc, 1)
    Tx1.sign(alex_prv)

    # --------------------------------------
    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2)
    Tx2.add_output(mike_pbc, 1)
    Tx2.add_output(rose_pbc, 1)
    Tx2.sign(alex_prv)

    # --------------------------------------
    Tx3 = Tx()
    Tx3.add_input(rose_pbc, 1.2)
    Tx3.add_output(alex_pbc, 1.1)
    Tx3.sign(rose_prv)
    Tx3.sign(mara_prv)

    # --------------------------------------
    for tx in [Tx1, Tx2, Tx3]: 
        tx_name = [k for k,v in locals().items() if v == tx][0]
        print_transaction(tx_name, tx)
        