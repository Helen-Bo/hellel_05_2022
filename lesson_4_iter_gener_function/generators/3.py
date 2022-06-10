import sys

sourse_list = [item for item in range(10_000_000)]
sourse_gen = (item for item in range(10_000_000))

print("list: ", len(sourse_list), sep=": ")
print(sys.getsizeof(sourse_list))

print("generator: ", sourse_gen, sep=": ")
print(sys.getsizeof(sourse_gen))
