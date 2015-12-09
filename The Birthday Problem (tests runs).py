import random
for numpeople in range(20,40):
        cnt = 0
        for tries in range(1000):
                l = [random.randrange(0, 366) for _ in range(numpeople)]
                if len(l) != len(set(l)): cnt += 1 # Duplicates
        print(str(numpeople) + " people: ~" + str(cnt/10) + "%")