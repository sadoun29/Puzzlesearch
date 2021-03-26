# Tp2 : Résolution d’un search puzzle avec SHA
#  	Sadoun Habib
#	M1 RESYS 2020/2021	

import hashlib

def find_crypt(algo,ID,Y):
    i=0
    while True:
        
        if   algo=='sha1':
             sha=hashlib.sha1()
        elif algo=='sha256':
             sha=hashlib.sha256()
    
        sha.update(bytearray(ID,'UTF-8'))
        sha.update(bytearray(chr(i),'UTF-8'))
        H= sha.hexdigest()
        if H<=Y:
            print('Y     : ',Y)
            print('ID    : ',ID)
            print('X     : ',chr(i))
            print('ID||X : ',ID+chr(i))
            
            print('compt : ',i)
            print('H     : ',H)
            break
        else:
            i+=1
            continue

   
def PuzzleSha1(ID,Y):
    print('Hashage SHA1')
    print('--------------')
    find_crypt('sha1',ID,Y)    
        

def PuzzleSha256(ID,Y):
    print('Hashage SHA256')
    print('--------------')
    find_crypt('sha256',ID,Y)


#main

    

PuzzleSha1("SADOUN HABIB" , '03b1663dda6549a0939ffdd712a852e0d4234e6b')
print('\n\n')
PuzzleSha256("SADOUN HABIB" , '00005d10cc11e27bd8d4d1ce91bc725665ddbaa6ca2498ef38a88a58ad48cdb4')
