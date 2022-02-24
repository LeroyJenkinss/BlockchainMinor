
import Asym

# Read the encrypted message from "message_test.enc"
# Read Keys file from "sample_test.keys"   File format is similar to the previous tutorial
# Check and print who is the receiver of this message

if __name__ == '__main__':
    print('This message is for .... ')

    from Asym import *

if __name__ == '__main__':
    
    keys_list = []

    alex_prv, alex_pbc = generate_keys()
    keys_list.append(('alex', alex_prv, alex_pbc))

    mike_prv, mike_pbc = generate_keys()
    keys_list.append(('mike', mike_prv, mike_pbc))

    rose_prv, rose_pbc = generate_keys()
    keys_list.append(('rose', rose_prv, rose_pbc))

    mara_prv, mara_pbc = generate_keys()
    keys_list.append(('mara', mara_prv, mara_pbc))

    john_prv, john_pbc = generate_keys()
    keys_list.append(('john', john_prv, john_pbc))

    lily_prv, lily_pbc = generate_keys()
    keys_list.append(('lily', lily_prv, lily_pbc))

    keys_file_name = 'samples.keys'
    save_keys(keys_file_name, keys_list)
    loaded_keys = load_keys(keys_file_name)

    plain_message = b'This is a test message!'
    recieved_message = load_message(message_title_name)
    for item in loaded_keys:
        key_name, prv_key, pbc_key = item
        decrypted_message = decrypt(recievedMessage, pbc_key)
        if decrypted_message == plain_message:
            print(f'Success: The message is correctly encrypted and decrypted by {key_name}')
        else:
            print(f'Fail: The message could not be decrypted by {key_name}')
    
