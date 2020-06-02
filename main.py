#!/bin/python3

from rsa.rsa import RSA as rsa
import sys
def main():
  if len(sys.argv) < 2:
      print("%s msg" % sys.argv[0])
      return False

  r = rsa()
  crypted=r.crypt_message(sys.argv[1])
  print("Crypted")
  print(crypted)
  decrypted=r.decrypt_message(crypted)
  print("Decrypted")
  print(decrypted)
  print( r.getKeysPair() )
  print( r.getKeysExternalInfo() )
  #print( r.getKeyPairFor(3,11) )

main()

