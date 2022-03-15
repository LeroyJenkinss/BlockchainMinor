from Signature import *
from Transaction import *


def print_transaction(tx_name, tx):
    count = 0
    for i in range(len(tx.inputs)):
        for b in range(len(keys_list)):
            if tx.inputs[i][0] == keys_list[b][0]:
                print(f'In[{i+1}] {keys_list[b][1]} send {tx.inputs[i][1]} coin')
    
    for i in range(len(tx.outputs)):
        for b in range(len(keys_list)):
            if tx.outputs[i][0] == keys_list[b][0]:
                print(f'In[{i+1}] {keys_list[b][1]} recieved {tx.outputs[i][1]} coin')
        
    

if __name__ == '__main__':

    keys_list =[]
    

    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()
    rose_prv, rose_pbc = generate_keys()
    mara_prv, mara_pbc = generate_keys()

    keys_list.append([alex_pbc, 'alex'])
    keys_list.append([mike_pbc, 'mike'])
    keys_list.append([rose_pbc, 'rose'])
    keys_list.append([mara_pbc ,'mara'])
    
    print('Tx1:')
    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 0.9)
    Tx1.add_output(mike_pbc, 0.8)
    print_transaction('Tx1', Tx1)
    print('-------------------------------------------')

    print('Tx2:')
    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2.1)
    Tx2.add_output(mike_pbc, 0.9)
    Tx2.add_output(rose_pbc, 1.0)
    print_transaction('Tx2', Tx2)
    print('-------------------------------------------')

    Tx2.add_input(mara_pbc, 0.7)
    Tx2.add_input(mara_pbc, 1.1)
    Tx2.add_input(mara_pbc, 1.5)
    Tx2.add_output(mike_pbc, 1.9)
    Tx2.add_output(rose_pbc, 0.2)
    print_transaction('Tx2', Tx2)
