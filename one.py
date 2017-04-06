import crypt
aaa = crypt.crypt("tt",crypt.mksalt(crypt.METHOD_MD5))
print(aaa)
