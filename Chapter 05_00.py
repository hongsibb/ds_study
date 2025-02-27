# Chapter 05-00
# 함수란?

#함수
# 프로그래머가 이름을 통해서 정의 후 필요할 때 마다 호출
# 반복되는 코드를 한 번 구현 후 재사용 가능한 코드의 집합
# 함수 구현 -> 재사용 (프로시져, 서브루틴)

#종류
#1. 매개변수가 필요한 함수
#2. 매개변수가 필요하지 않은 함수
#3. 결과값을 반환하는 함수 (return)
#4. 결과값을 반환하지 않는 함수수

#예제 1: 매개 변수가 필요하지 않은 함수, 리턴값 없음

def function1(): #매개변수 필요 x
    print('예제 1 호출')

# 실행
function1()

#예제 2: 매개변수 (agruement)가 필요한 함수
def function2(a, b):
    print('예제 2 호출', a, b)



# 예제3: 결과값 반환 x
def function3(x,y):
    print('예제 3 호출', x, y)

    
# 예제4: 결과값 반환O
def function4(x, y):
    return x + y



function1() # 호출
function2(10,20) # 호출 시 매개변수값 입력
function3(100, 200)
function4(100, 200) # 함수 안에 print가 없어서 아무값도 출력되지 않음.

r = function4(50, 50)

print('예제 4 호출', r)

# return = 필요할 때마다 쓸 수 있는 도구 / return x = 만든 함수 바로 실행하기
# return이 있으면 함수가 작업한 결과를 호출한 쪽으로 보내준다.

#return
def add(x, y):
    return x + y  # 계산만 하고 반환 (호출한 곳에서 값을 가지고 있음)

result = add(10, 20)  # retun이 없다면 none이고 함수 내 return이 있으므로 30을 가짐 / result = 30
print(result)  # 출력: 30 / return이 없으면 none이 출력됨.