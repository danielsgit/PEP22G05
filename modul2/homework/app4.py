a = "Ananas"
print(
"""
- A
  n
  a
  n
  a
  s
- Ana
  nas
- An:ana:s
- Ana_na_s
- nananananananana
""")

print('Versiunea 2:')
print('-',a[0], "\n",'',a[1],
      "\n",'',a[2],"\n",'',a[3],
      "\n",'',a[4],"\n",'',a[5],)
print('-', a[0:3], "\n",'',a[3:])
print('- ' + a[0:2],a[2:5],a[-1],sep=":")
print('- ' + a[0:3],a[3:5],a[-1],sep="_")
print('-', a[1:5]*4)

