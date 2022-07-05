import random
lower = "abcdefghijklmnopqrstuvwxyz"
upper = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
number = "0123456789"
symbol = "!@#$%^&*.;:"
aln = lower + upper + number + symbol
length = 12
password = "".join(random.sample(aln,length))
print(" The Password You generated is :",password)




