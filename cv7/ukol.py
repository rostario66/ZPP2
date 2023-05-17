def mocnina(zaklad, exponent):
   vysledek = 1
    
   try:
      for i in range(exponent):
         vysledek *= zaklad
    
   except Exception as e:
      return e, "musite zadat jenom cele cislo"
    
   else: 
      return vysledek


print(mocnina(2, -4))


print()


def desitkove(number):
   vysledek = ''
  
   try: 
    
       while number > 0:
            vysledek = str(number%2) + vysledek
            number = number // 2 
   
   except TypeError:
      return "musite zadat jenom cele cislo"
    
   return vysledek
   
print(desitkove("10"))
    

print()


def factorial_konc(n, result=1):
   try:
      
      assert n > 0
   
   except AssertionError:
     return "factorial zapornych cisel neexistuje"

   if n == 0:
      return result
   else:
      return factorial_konc(n-1, result*n)

print(factorial_konc(-1))


print()


def porovnany(seznam1, seznam2):  
  try:
    
      for i in seznam1:
         if i not in seznam2:
            return False
      for j in seznam2:
         if j not in seznam1:
            return False
      return True
  
  except TypeError:
     return "muzete pouzit jenom seznam"


print(porovnany([1,2,3,1],"1"))


print()


def recursive(zaklad, exponent):
    try: 
        
        assert exponent < 998
    
    except AssertionError:
     return "exponent musi byt mensi za 998"


    if exponent == 0:
        return 1
    else:
        return zaklad * recursive(zaklad, exponent - 1)
    
print(recursive(2,998))


print()


def matice(n):
   try:
      if n == 0: 
         raise Exception
   except Exception:
      print("zadane cislo nemuze byt nulou")

   try:
      seznam = []
      for i in range(n):
         row = []
         for j in range(n):
              row.append(0)
         seznam.append(row)

      for i in range(n):
          seznam[i][n-1-i] = 1

      for vysledek in seznam:
           print(vysledek)
   except TypeError:
      print("muzete zadat jenom cele cislo")

matice(0)