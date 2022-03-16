import string
from Signature import *
from Transaction import *


def print_transaction(tx_name, tx):
    count = 0
    for i in range(len(tx.inputs)):
        for b in range(len(keys_list)):
            if tx.inputs[i][0] == keys_list[b][2]:
                print(f'In[{i+1}] {keys_list[b][0]} send {tx.inputs[i][1]} coin')
    
    for i in range(len(tx.outputs)):
        for b in range(len(keys_list)):
            # if tx.outputs[i][0] != keys_list[b][2]:
            if tx.outputs[i][0] == keys_list[b][2]:
                print(f'Out[{i+1}] {keys_list[b][0]} recieved {tx.outputs[i][1]} coin')


if __name__ == '__main__':
    
    keys_list =[]

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', mara_prv, mara_pbc))

    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 0.9)
    Tx1.add_output(mike_pbc, 0.8)
    print_transaction('Tx1', Tx1)
    
    
  
    Tx1_alex_signature = sign(bytes(str(Tx1).encode()), alex_prv)
    verified = verify(bytes(str(Tx1).encode()), Tx1_alex_signature, alex_pbc)

    if verified:
        print('Success: Valid signature is verified.')
    else:
        print('Fail: Valid signature is not verified.')
    
    
    #if mike sign it to perform illegal transfer
    Tx1_mike_signature = sign(bytes(str(Tx1).encode()), mike_prv)
    verified = verify(bytes(str(Tx1).encode()), Tx1_mike_signature, alex_pbc)

    if verified:
        print('Fail: Invalid signature is accepted.')
    else:
        print('Success: Invalid signature is not verified.')

    Tx2 = Tx()
    Tx2.add_input(alex_pbc, 2.1)
    Tx2.add_output(mike_pbc, 0.9)
    Tx2.add_output(rose_pbc, 1.0)
    Tx2.add_input(mara_pbc, 0.7)
    Tx2.add_input(mara_pbc, 1.1)
    Tx2.add_input(mara_pbc, 1.5)
    Tx2.add_output(mike_pbc, 1.9)
    Tx2.add_output(rose_pbc, 0.2)
    print_transaction('Tx2', Tx2)

    
    Tx2_alex_signature = sign(bytes(str(Tx2).encode()), alex_prv)
    Tx2_mara_signature = sign(bytes(str(Tx2).encode()), mara_prv)

    alex_verified = verify(bytes(str(Tx2).encode()), Tx2_alex_signature, alex_pbc)
    mara_verified = verify(bytes(str(Tx2).encode()), Tx2_mara_signature, mara_pbc)

    if alex_verified and mara_verified:
        print('Success: A valid Transaction is verified.')
    else:
        print('Fail: A Valid Transaction is not verified.')
    
    Tx2_alex_signature = sign(bytes(str(Tx2).encode()), alex_prv)
    Tx2_mike_signature = sign(bytes(str(Tx2).encode()), mike_prv)

    alex_verified = verify(bytes(str(Tx2).encode()), Tx2_alex_signature, alex_pbc)
    mara_verified = verify(bytes(str(Tx2).encode()), Tx2_mara_signature, mara_pbc)

    if alex_verified and mara_verified:
        print('Success: An Invalid Transaction is not verified.')
    else:
        print('Fail: An Invalid Transaction is verified.')
