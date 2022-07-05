words = ["hello", "python", "world"]

for w in words:
	print(w)
print("end")

for w in words:
	for r in range(2):
		print(w)

for i, w in enumerate(words):
	print("Item", i, "is", w)