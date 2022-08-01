age = int(input())
if age % 4 == 0 and 1799 < age < 1_000_001:
    print("Рік високосний")
elif age % 100 != 0 and 1799 < age < 1_000_001:
    print("Рік не високосний")
elif age % 400 == 0 and 1799 < age < 1_000_001:
    print("Рік високосний")
else:
    print("Рік не відповідає умовам")
