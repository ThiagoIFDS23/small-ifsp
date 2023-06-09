N = int(input())
fatorial = 1

for i in range(1, N):
    fatorial *= i

if (fatorial + 1) % N == 0 and N != 0 and N!= 1:
    print("O número é primo.")
else:
    print("O número não é primo.")
