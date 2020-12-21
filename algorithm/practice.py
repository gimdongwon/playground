def strSlice():
	a = 'Boy'
	for item in range(len(a)):
		print(a[item])

# def sliceNum():
# 	data = input()
# 	for i in range(len(data)):
#     print([int(data[i]) * 10**(4-i)])

def covertNumber():
	data = input()
	print("{0:o}".format(int(data, 16)))
	# 'f'(16진수) => '17'(8진수)



# 합,차,곱,몫,나머지,나눈값
def counter():
	a,b = input().split()
	a = int(a)
	b = int(b)

	print(a+b)
	print(a-b)
	print(a*b)
	print(a//b)
	print(a%b)
	print("%.2f" % round(a/b,2))

def minusPlus():
	data = input()

	print("plus" if int(data)>=0 else "minus")
	print("even" if int(data)%2==0 else "odd")

def stopZero():
	data = '7 4 2 3 0 1 5'
	data = data.split()
	for i in range(len(data)):
		print(data[i])
		if data[i] == '0':
			break

def test30():
	from string import ascii_lowercase
	a = input()
	print(" ".join(ascii_lowercase[:ascii_lowercase.index(a)+1]))

def test35():
	data = input().split()

	for item in data:
		print(item)
		if item =='q':
			break

def cobination():
	a,b = input().split()

	for i in range(1,int(a)+1):
		for j in range(1,int(b)+1):
			print(i,j)

def xChange():
	data = int(input(), 16)
	for i in range(1,16):
		print("{0:X}".format(data,16)+"*"+"{0:X}".format(i,16)+"="+"{0:X}".format(i*data, 16))
	 
def threeSixNineChallenge():
	import re
	data = int(input())

	result = ''

	for i in range(1,data+1):
		result += str(i) + " "

	# print(result)
	print(re.sub('[3]|[6]|[9]', 'X', result))

# 다수의 최대 공약수
def GCDbyDW(a,b,c):
	arr = [a,b,c]
	def GCDofTwoNumbers(a,b):
		while b !=0:
			a,b = b, a%b
		return a
	GCDarr = arr[0]
	for i in range(len(arr)):
		GCDarr = GCDofTwoNumbers(GCDarr, arr[i])
		print("GCDarr = ", GCDarr)
	return GCDarr

# def LCMbyDW():
# 	arr = [3,7,9]
# 	def GCDofTwoNumbers(a, b): #GCDofTwoNumbers라는 이름의 함수와 매개변수 a, b 정의하기
# 		while b != 0 : #b가 0이 아닌 동안 반복
# 			a, b = b, a%b #a에 b를, b에 a와 b를 나눈 나머지를 교환하여 저장(스왑)
# 		return a #반환되는 a가 두 수의 최대공약수

# 	GCDarr = arr[0] #arr 리스트의 첫 번째 항목(0번 방)을 GCDarr에 저장
# 	LCMarr = arr[0] #arr 리스트의 첫 번째 항목(0번 방)을 LCMarr에 저장

# 	for i in range(len(arr)): #i가 0부터 리스트 arr의 길이만큼 반복
# 		GCDarr = GCDofTwoNumbers(LCMarr, arr[i]) # GCDarr에 LCMarr과 arr[i]의 최대공약수를 저장
# 		LCMarr = LCMarr * arr[i] // GCDarr #LCMarr에 LCMarr과 arr[i]의 최소공배수를 저장
#     	print(LCMarr)

# def lcm():
# 	import math

# 	data = list(map(int, input().split()))

# 	_lcm = data[0]
# 	for n in data[1:]:
# 		_lcm = int(_lcm*n/math.gcd(_lcm, n))
# 	print(_lcm)

def secondCall():
	a = int(input())
	b = list(map(int, input().split()))

	for i in range(1,24):
		c = b.count(i)
		print(c, end=' ')

def secondCall2():
	a = int(input())
	b = list(map(int, input().split()))

	for i in b:
		print(b[a-1], end=' ')
		a -= 1

#---------------------------------
# 결과 출력

secondCall()
# lcm()
# LCMbyDW()
# print(GCDbyDW())
# threeSixNineChallenge()
# xChange()
# stopZero()
#minusPlus()
# strSlice()
# sliceNum()