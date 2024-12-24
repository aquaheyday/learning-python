#1. 기본 입력과 출력
#2. 여러 개의 입력 처리
#3. 입력 값을 변환
#4. 출력 형식 지정
#5. 빠른 입력

기본 입력: input()
기본 출력: print()

# 사용자의 입력을 받아 그대로 출력
a = input()
print(a)
# 입력 예시: hello
# 출력 예시: hello


# 두 줄의 입력을 받아 각각 변수에 저장하고 출력
a = input()
b = input()
print(a, b)
# 입력 예시: hello
# world
# 출력 예시: hello world


# 입력 받은 값을 출력하고 데이터 타입 확인
a = input()
print(a)
print(type(a))
# 입력 예시: hello
# 출력 예시: hello
# <class 'str'>

# 숫자를 입력 받아 출력하고 데이터 타입 확인
a = input()
print(a)
print(type(a))
# 입력 예시: 1234

# 입력 받은 값을 정수로 변환하여 출력하고 데이터 타입 확인
a = input()
a = int(a)
print(a)
print(type(a))
# 입력 예시: 1234
# 출력 예시: 1234
# <class 'int'>


input() 함수는 항상 문자열로 반환
다른 타입으로 저장이 필요한 경우 변환 필요
# 입력 받은 값을 정수로 바로 변환하여 출력하고 데이터 타입 확인
a = int(input())
print(a)
print(type(a))
# 입력 예시: 1234
# 출력 예시: 1234
# <class 'int'>

# 한 줄에 두 개의 입력을 받아 각 변수에 저장하고 출력
a, b = input().split()
print(a, b)
print(a)
print(b)
# 입력 예시: hello world
# 출력 예시: hello world
# hello
# world

# 두 개의 입력을 받아 정수로 변환하고 합을 출력
a, b = input().split()
a = int(a)
b = int(b)
print(a + b)
# 입력 예시: 12 3
# 출력 예시: 15

# 두 개의 입력을 받아 정수로 변환하지 않고 + 연산하여 결과를 출력
a, b = input().split()
print(a + b)
# 입력 예시: 12 3
# 출력 예시: 123


# map 함수를 사용하여 입력 받은 값을 정수로 변환하고 합을 출력
a, b = map(int, input().split())
print(a + b)
# 입력 예시: 12 3
# 출력 예시: 15


참고: map 함수 설명
map 함수는 여러 개의 입력값을 동시에 처리할 때 유용합니다.
일반적인 형태는 map(함수, 입력값들) 입니다.
map(int, input().split()) 는 input().split() 으로 나누어진 입력값들을
int 함수로 변환하여 리스트로 반환합니다.
예를 들어, input() 에서 "12 3" 을 입력받으면 split() 을 통해 ['12',
'3'] 리스트가 됩니다.
map(int, ['12', '3']) 는 각 요소를 int 로 변환하여 [12, 3] 리스트로
반환합니다.

# 여러 개의 입력을 리스트로 받아 출력하고 각 요소의 데이터 타입 확인
a = input().split()
print(a)
print(type(a))
print(type(a[0]))
# 입력 예시: hello python world
# 출력 예시: ['hello', 'python', 'world']
# <class 'list'>
# <class 'str'>


# map 함수를 사용하여 여러 개의 정수 입력을 리스트로 변환하여 출력하고 각 요소의 데이
a = list(map(int, input().split()))
print(a)
print(type(a))
print(type(a[0]))
# 입력 예시: 1 23 456
# 출력 예시: [1, 23, 456]
# <class 'list'>
# <class 'int'>


출력 형식 지정
print() 함수의 sep 와 end 파라미터를 사용하여 출력 형식을 지정

sep 파라미터
sep 는 출력할 값들 사이에 넣을 문자열을 지정
기본값은 공백
# sep 예제
print('apple', 'banana', 'cherry')
print('apple', 'banana', 'cherry', sep = ', ')
# 출력:
# apple banana cherry
# apple, banana, cherry


end 파라미터
end 는 출력의 끝에 넣을 문자열을 지정
기본값은 줄 바꿈( '\n' )

# end 예제
print('Hello', end = ' ')
print('World')
# 출력:
# Hello World

참고: 몫과 나머지 구하기
두 수를 입력받아 몫과 나머지를 구하는 문제
# 두 개의 입력을 받아 정수로 변환하고 몫과 나머지를 출력
a, b = map(int, input().split())
print(a // b, a % b)


빠른 입력: \ import sys \ input = sys.stdin.readline
참고 : sys.stdin.readline 이 input 에 비해 더 빠른 이유
input() 함수는 사용자 입력을 받고 개행 문자를 제거한 후 문자열로 반환합니다.
이 과정에서 표준 입력 스트림을 사용해 데이터를 읽고, 이를 다시 처리하는 과정이
포함되어 있어 다소 시간이 걸릴 수 있습니다.
반면에 sys.stdin.readline() 함수는 표준 입력 스트림에서 한 줄을 그대로 읽
어옵니다. 개행 문자를 포함한 입력 문자열을 반환하므로, 후처리가 필요 없는 경우
입력 처리 속도가 더 빠릅니다.
대량의 데이터를 처리할 때 input() 보다 sys.stdin.readline() 이 빠른 이유
는 다음과 같습니다:
sys.stdin.readline() 은 한 번에 입력을 받아들여서 처리 속도가 빠릅니다.
input() 은 내부적으로 많은 작업을 처리하므로, 반복문에서 자주 호출될 때
성능 저하가 발생할 수 있습니다.
예를 들어, 반복문을 통해 여러 줄의 입력을 받아야 하는 경우
sys.stdin.readline() 을 사용하면 성능이 향상됩니다.

# sys.stdin.readline을 사용한 빠른 입력 예제
import sys
input = sys.stdin.readline
t = int(input())