from struct import*
i=raw_input()
k=4-len(i)%4&3
i+='\0'*k
o=''
while i:
 b,=unpack('>I',i[-4:]);i=i[:-4]
 while b:o+=chr(b%85+33);b/=85
print'<~%s~>'%o[k:][::-1]
