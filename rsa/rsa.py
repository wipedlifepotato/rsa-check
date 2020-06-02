
import random
DEBUG=False
class RSA:
 def is_prime(self, num):
    a=num-1
    while a > 1:
        #print("num(%d)/a(%d) = %d" % (num,a, num/a)) 
        if (num%a) == 0: return False
        a = a -1
    return True

 def get_primenum(self, from_,o='+'):
    a=from_
    while not self.is_prime(a):
        if o == '+':
         a=a+1
        elif o=='-': a=a-1
        else: return False 
    return a
 def getKeysExternalInfo(self):
     return {
                'p':self.p,
                'q':self.q,
                'phi':self.phi
             }
 #return e,d,n where e-encryption key, d - decryption key, n - N whose publicQ
 def get_ed( self, frm=8, to=10, plus=1 ):

    #while not is_prime(n): 
    p,q=(random.randint(2**frm , 2**to),random.randint(2**frm , 2**to) )
    p,q=(self.get_primenum(p+plus),self.get_primenum(q+plus))
    n = p*q    
    phi=(p-1)*(q-1)

    self.p=p
    self.q=q
    self.phi=phi

    d=p+plus
    d=self.get_primenum(d)

    e=random.randint(2**frm,2**to)
    if DEBUG: print("public key generation.")
    while e*d % phi != 1:
        e=e+plus
        if e > phi: 
            print("WARNING: e>phi")
            e=d+1
    
    if DEBUG: print ( "DEBUG: e=%d;d=%d;n=%d;" % (e,d,n) )
    return e,d,n
 def getKeysPair(self):
  return { 'public': (self.encryptionKey,self.n), 'private': (self.decryptionKey,self.n) }
 def __init__(self, e=0,d=0,n=0):
     if e!=0 and d!=0 and n!=0:
      self.init_self_key(e,d,n)
     else:
      e,d,n = self.get_ed()
      self.init_self_key(e,d,n)
 def init_self_key(self,e,d,n):
     self.encryptionKey=e
     self.decryptionKey=d
     self.n=n
 def crypt_message(self, msg, encryptionKey=-1, n=-1):
     if encryptionKey == -1 or n==-1:
         if self.encryptionKey == 0 or self.n==-1: return False
         encryptionKey=self.encryptionKey
         if n==-1: n = self.n
     encryptList=[]
     for c in msg:
      encryptList.append(   ord(c)**encryptionKey % n )

     return encryptList
 def decrypt_message(self, msg,decryptionKey=-1,n=-1):
     if decryptionKey == -1 or n==-1:
      if self.decryptionKey == 0 or self.n==-1: return False
      decryptionKey=self.decryptionKey
      if n==-1: n = self.n
     decryptChars=[]
     for c in msg:
         decryptChars.append( chr(c**decryptionKey % n) )
     return decryptChars


             



