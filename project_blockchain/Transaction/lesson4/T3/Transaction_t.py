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
   
    listValidInput1 = []
    listValidOutput1 = []

    for a in range(len(Tx1.inputs)):
        Tx1_alex_signature = sign(bytes(str(Tx1.inputs[a]).encode()), alex_prv)
        verified = verify(bytes(str(Tx1.inputs[a]).encode()), Tx1_alex_signature, alex_pbc)
        listValidInput1.append(verified)

    for a in range(len(Tx1.inputs)):
        Tx1_alex_signature = sign(bytes(str(Tx1.inputs[a]).encode()), alex_prv)
        verified = verify(bytes(str(Tx1.inputs[a]).encode()), Tx1_alex_signature, alex_pbc)
        listValidOutput1.append(verified)

    verified1 = None
    for a in listValidInput1:
        for b in listValidOutput1:
            if a == False or b == False:
                verified1 = False
            else:
                verified1 = True

    if verified1:
        print('Success: Valid signature is verified.')
    else:
        print('Fail: Valid signature is not verified.')

    # if mike sign it to perform illegal transfer
    listValidInput2 = []
    listValidOutput2 = []

    for a in range(len(Tx1.inputs)):
        Tx1_mike_signature = sign(bytes(str(Tx1.inputs[a]).encode()), mike_prv)
        verified = verify(bytes(str(Tx1.inputs[a]).encode()), Tx1_mike_signature, alex_pbc)
        listValidInput2.append(verified)

    for a in range(len(Tx1.inputs)):
        Tx1_mike_signature = sign(bytes(str(Tx1.inputs[a]).encode()), mike_prv)
        verified = verify(bytes(str(Tx1.inputs[a]).encode()), Tx1_mike_signature, alex_pbc)
        listValidOutput2.append(verified)

    verified2 = None
    for a in listValidInput2:
        for b in listValidOutput2:
            if a == False or b == False:
                verified2 = False
            else:
                verified2 = True

    if verified2:
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


    Tx2_alex_signature =  None 

    listValidInput3 = []
    listValidOutput3 = []

    for a in range(len(Tx2.inputs)):
        Tx2_alex_signature = sign(bytes(str(Tx2.inputs[a]).encode()), alex_prv)
        verified = verify(bytes(str(Tx2.inputs[a]).encode()), Tx2_alex_signature, alex_pbc)
        listValidInput3.append(verified)

    for a in range(len(Tx2.inputs)):
        Tx2_alex_signature = sign(bytes(str(Tx2.inputs[a]).encode()), alex_prv)
        verified = verify(bytes(str(Tx2.inputs[a]).encode()), Tx2_alex_signature, alex_pbc)
        listValidOutput3.append(verified)

    verified3 = None
    for a in listValidInput3:
        for b in listValidOutput3:
            if a == False or b == False:
                verified3 = False
            else:
                verified3 = True

    Tx2_mara_signature = None 

    listValidInput4 = []
    listValidOutput4 = []

    for a in range(len(Tx2.inputs)):
        Tx2_mara_signature = sign(bytes(str(Tx2.inputs[a]).encode()), mara_prv)
        verified = verify(bytes(str(Tx2.inputs[a]).encode()), Tx2_mara_signature, mara_pbc)
        listValidInput4.append(verified)

    for a in range(len(Tx2.inputs)):
        Tx2_mara_signature = sign(bytes(str(Tx2.inputs[a]).encode()), mara_prv)
        verified = verify(bytes(str(Tx2.inputs[a]).encode()), Tx2_mara_signature, mara_pbc)
        listValidOutput4.append(verified)

    verified4 = None
    for a in listValidInput4:
        for b in listValidOutput4:
            if a == False or b == False:
                verified4 = False
            else:
                verified4 = True

    alex_verified = verified3
    mara_verified = verified4

    if alex_verified and alex_verified:
        print('Success: A valid Transaction is verified.')
    else:
        print('Fail: A Valid Transaction is not verified.')

    
    listValidInput5 = []
    listValidOutput5 = []

    for a in range(len(Tx2.inputs)):
        Tx2_mike_signature = sign(bytes(str(Tx2.inputs[a]).encode()), mike_prv)
        verified = verify(bytes(str(Tx2.inputs[a]).encode()), Tx2_mike_signature, mike_pbc)
        listValidInput5.append(verified)

    for a in range(len(Tx2.inputs)):
        Tx2_mike_signature = sign(bytes(str(Tx2.inputs[a]).encode()), mike_prv)
        verified = verify(bytes(str(Tx2.inputs[a]).encode()), Tx2_alex_signature, mike_pbc)
        listValidOutput5.append(verified)

    verified5 = None
    for a in listValidInput5:
        for b in listValidOutput5:
            if a == False or b == False:
                verified5 = False
            else:
                verified5 = True

    if verified4 and verified1:
        print('Success: An Invalid Transaction is not verified.')
    else:
        print('Fail: An Invalid Transaction is verified.')