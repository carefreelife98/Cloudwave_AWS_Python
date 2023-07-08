# 리스트 만들기
temps = [28, 31, 33, 35, 27, 26, 25] 

# 리스트 항목 접근하기
print(temps[3])
e = temps[3]

# 리스트 처리하기
temps = [28, 31, 33, 35, 27, 26, 25]

for i in range(len(temps)):
	if i != len(temps)-1:
		print(temps[i], end=', ')
	else:
		print(temps[i])

temps =[28, 31, 33, 35, 27, 26, 25]

# for~each 루프 사용하기
for element in temps:
	if element != temps[-1]:
		print(element, end=', ')
	else:
		print(element)


# 동시에 두 개 이상의 리스트를 반복하기 위해 zip() 함수 사용
questions =['name','quest','color']
answers =['Kim','파이썬','blue']
for q, a in zip(questions, answers):
	print(f"What is your {q}?  It is {a}")


heroes = [ ] 	# 공백 리스트를 생성한다.
heroes.append("아이언맨")		# 리스트에 ”아이언맨“을 추가한다. 
heroes.append("토르")			# 리스트에 ”토르“를 추가한다. 
print(heroes)


heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치", "헐크" ]
n = heroes.index("헐크")		# n은 2가 된다. 

if "헐크" in heroes:
    print(heroes.index("헐크"))

heroes = [ "아이언맨", "토르", "헐크", "스칼렛 위치", "헐크" ]
n = heroes.index("헐크", 3)		# n은 4가 된다. 


heroes = [ "아이언맨", "토르", "헐크" ]
heroes.remove("토르")

if "토르" in heroes:
	heroes.remove("토르")


values = [ 1, 2, 3, 4, 5, 6, 7, 8, 9, 10 ]
min(values)		# 1
max(values)		# 10

a = [ 3, 2, 1, 5, 4 ]
a.sort()			# [1, 2, 3, 4, 5]

heroes =['아이언맨','헐크','토르']
heroes.sort()
print(heroes)

a =[3,2,1,5,4 ]
# a.sort(reverse=True)
a.sort()
print(a)


# import time
# SIZE =50000

# start_time = time.time()
# mylist =[]
# for i in range(SIZE):
#     mylist = mylist +[i * i]
# print("수행시간=", time.time()- start_time)

# start_time = time.time()
# mylist =[]
# for i in range(SIZE):
#     mylist.append(i * i)
# print("수행시간=", time.time()- start_time)


# 리스트 함축
list1 = [10, 20, 30, 40, 50]

list2 = [sum(list1[0:x+1]) for x in range(0, len(list1))]

print("원래 리스트: ",list1)
print("새로운 리스트: ",list2)
numbers = [x for x in range(100) if x % 2 == 0 and x % 3 == 0]
print(numbers)


# 다차원 리스트
s = [ 	[ 1, 2, 3, 4, 5 ] ,
	[ 6, 7, 8, 9, 10 ], 
	[11, 12, 13, 14, 15 ] ]

# 행과 열의 개수를 구한다. 
rows = len(s)
cols = len(s[0])

for r in range(rows):
	for c in range(cols):
		print(s[r][c], end=",")
	print()


s = [ 	[ 1, 2, 3, 4, 5 ] ,
	[ 6, 7, 8, 9, 10 ], 
	[11, 12, 13, 14, 15 ] ]

# 행과 열의 개수를 구한다. 
rows = len(s)
cols = len(s[0])

i = 1
total = 0
for j in range(cols) :
 total = total + s[i][j] 	# 행 합계를 계산한다. 
print(total)



# 튜플(tuple)
# 리스트와 유사하지만 변경 불가능

single_tuple = ("apple",)    	# 쉼표가 끝에 있어야 한다. 
print(single_tuple)	
no_tuple = ("apple")    	# 쉼표가 없으면 튜플이 아니라 수식이 된다. 

fruits = ("apple", "banana", "grape")
print(fruits[1])		
# fruits[1] = "pear"		# 오류 발생!

fruits =("apple","banana","grape")
for f in fruits:
	print(f, end=" ")		# apple banana grape 출력 
	
myList = [1, 2, 3, 4] 
myTuple = tuple(myList)		# tuple()는 튜플을 생성하는 함수이다. 
print(myTuple)



# 딕셔너리(dictionary)
# key:value 형태로 저장되는 자료구조. 키(key)는 중복 불가능하지만 값(value)은 중복 가능.

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
print( capitals["Korea"])	

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
if "France" in capitals :
	print( "딕셔너리에 포함됨" )
else: 
	print( "딕셔너리에 포함되지 않음" )



capitals ={}
capitals["Korea"]="Seoul"
capitals["USA"]="Washington"
capitals["UK"]="London"
capitals["France"]="Paris"
print(capitals)


capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
capitals.update({"France":"Paris","Germany":"Berlin"})
print(capitals)


capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 

capitals.clear()
if len(capitals)==0 :
	print("딕셔너리에 항목이 있음")
else:
	print("딕셔너리가 비어 있음")


capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
        print( key, end=" ")
	

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key in capitals :
        print( key,":", capitals[key])
	

capitals ={"Korea":"Seoul","USA":"Washington","UK":"London"} 
for key, value in capitals.items():
        print( key,":", value )


# 세트(set)
# 고유한 값들을 저장하는 자료구조. 중복저장 불가능. 
# 리스트와 다르게 세트의 요소는 특정 순서로 저장되지 않으며 위치별로 액세스할 수 없음.

fruits = { "apple", "banana", "grape" }
if "apple" in fruits:
	print("집합 안에 apple이 있습니다.")
	

fruits ={"apple","banana","grape"}
for x in sorted(fruits):
	print(x, end=" ")
	


engineers =set(['Kim','Park','Lee'])
programmers =set(['Kim','Song','Choi'])
managers =set(['Chun','Seo','Oh'])

for group in [engineers, programmers, managers]: 
	group.discard('Kim') 		# 모든 그룹에서 “Kim"을 삭제한다.  
	print(group)
	


aList  =[1,2,3,4,5,1,2 ]
result ={ x for x in aList if x%2==0 }
print(result)


A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}

if A < B : 			# 또는 A.issubset(B) :
	print("A는 B의 부분 집합입니다.")
	


A ={"apple","banana","grape"}
B ={"apple","banana","grape","kiwi"}
if A == B :
	print("A와 B는 같습니다.")
else :
	print("A와 B는 같지 않습니다.")
	

list1 =[1,2,3,4,5 ]
list2 =[3,4,5,6,7 ]
print(set(list1)&set(list2))



# 문자열 : 파이썬에 문자열을 처리하는 방법은 다양함.

# 문자열 비교
a = input("문자열을 입력하시오: ")
b = input("문자열을 입력하시오: ")
if( a < b ):
	print(a, "가 앞에 있음")
else:
	print(b, "가 앞에 있음")


# f-문자열 이용하여 출력하기(버전 3.6 이상) 
x = 25
y = 98
prod = x * y
print(f"{x}과 {y}의 곱은 {prod}")

# 회문 검사

s = input("문자열을 입력하시오: ")

s1 = s[::-1]			# 문자열을 거꾸로 만든다. 

if( s == s1 ):
        print("회문입니다.")
else:
        print("회문이 아닙니다.")
	


# 문자열 찾기: startswith(s), endswith(s), find(s) 등

s = input("파이썬 소스 파일 이름을 입력하시오: ")
if s.endswith(".py"):
	print("올바른 파일 이름입니다")
else :
	print("올바른 파일 이름이 아닙니다.")

# 그 외 다양하게 문자를 처리할 수 있는 함수들이 있음.


# sample 함수 이용하여 문자열에서 random하게 값 읽기
import random
  
s = "0123456789"		# 대상 문자열
passlen = 6			# 패스워드 길이


p =  "".join(random.sample(s, passlen ))
print(p)

# 문자열 단어수 세기
t = "Python is very easy and powerful!"

length = len(t.split(" "))
print(length)