sens = {}
N = int(input())
for i in range(N):
    name, num = map(str, input().split())
    if name not in sens:
        sens[name] = []
    sens[name].append(int(num))
for i in sens.values():
    i.sort()
M = int(input())
for i in range(M):
    name = input()
    if name not in sens:
        print("no data")
    else:
        leng = len(sens[name])
        if leng%2 == 0:
            print(sens[name][leng//2 - 1])
        else:
            print(sens[name][leng//2])