#스크립트

#1) 함수
'''
이 함수는 filename과 debug를 인자로 받는다.
그러나 아래와 같이 debug 인자를 선택으로 받을 수 있는데
debug를 입력 안할 시 False로 받는다. 
'''
def read_prices(filename,debug=False): 
    prices = {}
    with open(filename) as f:
        f_csv = csv.reader(f)
        for row in f_csv:
            prices[row[0]] = float(row[1])
    return prices
    #return prices*prices 

#반환 값은 return으로 표시한다

#2) 함수 여러 개의 반환 값
'''
한개의 값을 반환할 때와 다르게
여러개의 값을 반환할 경우 튜플에 여러 값을 담아 반환 하게 된다.
'''
def divide(a,b):
    q = a // b      # 몫, 이 값은 함수 내에서만 유효한 지역변수
    r = a % b       # 나머지
    return q, r     # 튜플을 반환

q_global,r_global=divide(10,5) #이 값은 전역에서 유효한 전역변수
result=divide(10,5) #튜플로 반환받는다.

'''
출력 결과
print(q,r) --> 2 0
print(result) --> (2, 0) 튜플 타입인 것을 확인할 수 있다.

'''
#3) 예외
#try-except을 이용하여 예외를 처리한다!
try:
    print("follow logic")
except RuntimeError as e: #빌트인 예외는 RuntimeError외에도 많은 것이 존재한다
    print("this is error: ",e)

#혹은 중간에 raise를 사용한다
def test():
    print("do logic")
    raise RuntimeError('yeap!')

'''
예외가 발생했는지 여부와 관계 없이 실행해야 할 코
lock = Lock()
...
lock.acquire()
try:
    ...
finally:
    lock.release()  # 이것은 항상 실행된다! 예외 발생 여부와 관계 없이
'''

#위 과정을 with으로 대체 할 수 있다
ob=object_test()
with ob:
    print(ob.do_work()): #do_work()는 헬로 출력
'''
위 코드는 헬로를 출력하고 객체를 반환한다.
즉 with을 사용한다면 객체의 라이프 사이클을 설계할 수 있는 것이다.
객체 생성, 사용, 소멸
'''
