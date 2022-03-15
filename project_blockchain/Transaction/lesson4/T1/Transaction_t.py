from Signature import *

if __name__ == '__main__':
    
    alex_prv, alex_pbc = generate_keys()
    mike_prv, mike_pbc = generate_keys()

    data = [
        'Alex pays 2 coin to mike', 
        'Alex pays 1.2 coins to Mara', 
        'Mike pays 0.6 coin to Alex'
        ]

# sign data using alex signature and then verify it using the same signature
singedMessage = ''
signedArray = []
for a in data:
    signedMessage = sign(a.encode('UTF-8'),alex_prv)
    output = verify(a.encode(), signedMessage, alex_pbc)
    
    print(output)


# sign data using alex signature and then verify it using mike signature
for a in data:
    signedMessage = sign(a.encode('UTF-8'),alex_prv)
    output = verify(a.encode(), signedMessage, mike_pbc)
    print(output)