# for i in range(10):
#     print(i)
# 123
names = ["Dima", "Sasha", "Vania", "Tania"]

print("Out sourse names:")
for name in names:
    print(name)
print("\n\n")

data = iter(names)
print("Out iter names")
# next(data)
# data.__next__()
# for d in data:
#     print(d)
# print('\n\n')
while True:
    try:
        print(data.__next__())
    except StopIteration:
        break
