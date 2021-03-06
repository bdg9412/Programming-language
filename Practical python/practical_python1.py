d = {

        'name' : 'AA',

        'shares' : 100,

        'price'  : 32.2

    }

    

for k in d:

    print(k) #key를 출력하게 된다.

 

cost = d['shares'] * d['price']

print(cost) #튜플에서는 위 계산을 리스트 처럼 변수명[index]로 수행하였으나 딕셔너리 변수에 key값을 할당하여 value를 사용한다.

 

d['shares'] = 75 

print(d['shares']) #튜플에서는 t[1] = 75이 안되지만 딕셔너리에서는 값의 변경이 가능하다. 즉 튜플은 값의 변화가 없을 때 사용하도록

 

for k in d:

    print(k, '=', d[k]) #이렇게 key와 value를 출력할 수 있다.

 

d['account'] = 12345 #이렇게 딕셔너리에 새로운 어트리뷰트를 추가할 수 있다.

 

del d['account'] #혹은 이렇게 딕셔너리에서 어트리뷰트를 삭제할 수 있다.

 

#딕셔너리에 items()메소드를 사용하여 (key,value) 튜플을 얻을 수 있다.

'''

>>> items = d.items()

>>> items

dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])

>>> for k, v in d.items():

        print(k, '=', v)

 

name = AA

shares = 75

price = 32.2

date = (6, 11, 2007)

>>>

'''

#형태가 맞는 items같은 튜플이 있다면 dict()함수를 사용해 딕셔너리를 생성할 수 있다.

'''

>>> items

dict_items([('name', 'AA'), ('shares', 75), ('price', 32.2), ('date', (6, 11, 2007))])

>>> d = dict(items)

>>> d

{'name': 'AA', 'shares': 75, 'price':32.2, 'date': (6, 11, 2007)}

>>>

'''

 

#컨테이너로서의 리스트

#데이터의 순서가 중요할 때는 리스트를 사용하자! 왜냐면 리스트는 어떤 유형의 객체든 담을 수 있다.

contain_list=[('dongkeun',94),"bak"] #리스트에 튜플과 문자열을 담았다!

print(contain_list[0],"  ",contain_list[1])

 

#복습용도, 빈 리스트 생성 및 append

records = []  # 빈 리스트로 초기화

records.append("1")

records.append("2")

 

#컨테이너로서의 딕딕셔너리를

#딕셔너리는 빠른 임의조회(key값으로 검색)에 유용

prices = {

   'GOOG': 513.25,

   'CAT': 87.22,

   'IBM': 93.37,

   'MSFT': 44.12

}

print(prices['CAT'])

 

#복습용도, 빈 딕셔너리 생성 및 할당

prices = {} # 빈 딕셔너리로 초기화

prices['dongkeun']=94

 

#딕셔너리의 키는 어떤 값도 가능하다

'''

holidays = {

  (1, 1) : 'New Years',

  (3, 14) : 'Pi day',

  (9, 13) : "Programmer's day",

}

'''

 

#세트

#세트는 고유 항모그이 모음이면서 순서를 유지하지 않는다.

names = ['IBM', 'AAPL', 'GOOG', 'IBM', 'GOOG', 'YHOO']

 

unique = set(names)

# unique = set(['IBM', 'AAPL','GOOG','YHOO'])

# 이같은 방식은 주로 코딩테스트할 때 중복제거하고 무언가를 찾을때!

'''

names.add('CAT')        # 항목을 추가

names.remove('YHOO')    # 항목을 제거

 

s1 | s2                 # 합집합

s1 & s2                 # 교집합

s1 - s2                 # 차집합
'''