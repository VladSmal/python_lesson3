age = int(input())

if 1799 < age < 1_000_000:
    if age % 400 ==0:
        print (age, "Рік є високосним")
    elif age % 100 == 0:
        print(age, "Рік не є високосним")
    elif age %4 == 0:
        print(age, "Рік є високосним")
    else:
       print(age, "Рік не є високосним")
else:
    print("Рік не відповідає умовам, діапазон від 1799 до 1_000_000")
