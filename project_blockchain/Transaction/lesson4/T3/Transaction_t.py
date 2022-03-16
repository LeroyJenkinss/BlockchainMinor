from Signature import *
from Transaction import *


def print_transaction(tx_name, tx):
    pass


if __name__ == '__main__':
    
    keys_list =[]

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', alex_prv, alex_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', alex_prv, alex_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', alex_prv, alex_pbc))

    Tx1 = Tx()
    Tx1.add_input(alex_pbc, 0.9)
    Tx1.add_output(mike_pbc, 0.8)
    print(f'hier is het :{Tx1}')
    print_transaction('Tx1', Tx1)
    for a in Tx1.inputs:
        print(f'hier is inputs :{a}')

    Tx1_alex_signature = sign(Tx1, alex_prv)
    
    verified = verify(Tx1, Tx1_alex_signature, alex_pbc)

    if verified:
        print('Success: Valid signature is verified.')
    else:
        print('Fail: Valid signature is not verified.')

    # # if mike sign it to perform illegal transfer
    # Tx1_mike_signature = None # Modify this -- to sign it with Mike's Signature
    # verified = None # Modify this -- to verify it with Alex's Signature
    # if verified:
    #     print('Fail: Invalid signature is accepted.')
    # else:
    #     print('Success: Invalid signature is not verified.')


    # Tx2 = Tx()
    # Tx2.add_input(alex_pbc, 2.1)
    # Tx2.add_output(mike_pbc, 0.9)
    # Tx2.add_output(rose_pbc, 1.0)
    # Tx2.add_input(mara_pbc, 0.7)
    # Tx2.add_input(mara_pbc, 1.1)
    # Tx2.add_input(mara_pbc, 1.5)
    # Tx2.add_output(mike_pbc, 1.9)
    # Tx2.add_output(rose_pbc, 0.2)
    # print_transaction('Tx2', Tx2)

    # Tx2_alex_signature = None # Modify this -- to sign it with Alex's Signature
    # Tx2_mara_signature = None # Modify this -- to sign it with Mara's Signature

    # alex_verified = None # Modify this -- to verify it with Alex's Signature
    # mara_verified = None # Modify this -- to verify it with Mara's Signature 

    # if alex_verified and alex_verified:
    #     print('Success: A valid Transaction is verified.')
    # else:
    #     print('Fail: A Valid Transaction is not verified.')


    # Tx2_alex_signature = None # Modify this -- to sign it with Alex's Signature
    # Tx2_mike_signature = None # Modify this -- to sign it with Mike's Signature

    # alex_verified = None # Modify this -- to verify it with Alex's Signature
    # mara_verified = None # Modify this -- to verify it with Mara's Signature 

    # if alex_verified and alex_verified:
    #     print('Success: An Invalid Transaction is not verified.')
    # else:
    #     print('Fail: An Invalid Transaction is verified.')