SSN = input("enter SSN (ddd-dd-dddd):")

chunks = SSN.split('-')

valid=False

if len(chunks) ==3: 
   
   if len(chunks[0])==3 and len(chunks[1])==2 and len(chunks[2])==4:

       valid=True

print (valid)

