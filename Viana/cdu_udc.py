while True:
	print("Digite um número")
	N = int(input())
	print(str(int(N%100 + 99*(N%10) + (N - N%100)/100)))
