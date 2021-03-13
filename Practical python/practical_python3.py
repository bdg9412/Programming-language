#파이썬 시퀀스

#1) 모든 시퀀스는 순서가 유지되고, 정수로 인덱싱, 길이 유지
a='hello' #문자열
b=[1,3,5] #리스트
c=('good',100,490.1) #튜플

a[0] #'h'
b[-1] #'-'이면 뒤부터 시작!
c=[1] #100


#2) 시퀀스를 복제(s*n)
a="hi"
print(a*3) #hihihi가 된다.
b=[1,2,3]
print(b*2) # [1,2,3,1,2,3]이 된다

'''

응용으로 출력단을 구분하고 싶을 떄
'='*20 과 같이 사용할 수 있다.

'''

#3) 같은 타입의 시퀀스끼리 이어붙일 수 있다(s+t)
a=(1,2,3)
b=(4,5)
print(a+b) # (1,2,3,4,5)가 된다

#4) 슬라이싱
a=[0,1,2,3,4,5]

a[2:5] # [2,3,4]
a[-5:] # [5,4,3,2,1]
a=[:3] # 0,1,2

'''
슬라이싱에서는 start, end 인데스는 반드시 정수여야 한다
슬라이스할 때 end 위치는 포함하지 않는다.
슬라이싱에서 인덱스를 생락하면 리스트의 시작이나 끝을 기본값으로 사용
'''

#5) 슬라이싱 재할당
#리스트에서 슬라이스를 다시 할당하거나 삭제할 수 있다
a=[1,2,3,4,5]
a[0:1]=[0,0]
print(a) #결과는 [0,0,3,4,5]

del a[0:1] #결과는 [3,4,5]


#6) 시퀀스 축소하여 단일 값으로 줄이는 함수
s=[1,2,3,4]
sum(s) #10
min(s) #1
max(s) #4 --> 코딩테스트에서 최소, 최대값 찾을 때

t=['hello','world']
max(t) #world 출력

#7) 시퀀스에 대한 iteration
s=[1,2,3,5,6]
for i in s:
    print(i)
#1,2,3,5,6

#8)for문 중간에 break로 for문 탈출하거나 continue로 해당 iter 건너뛰기 가능
for i in s:
    print(i)
    if i==10:
        break
    elif i==0:
        continue

#정수에 대해 루핑
#카운트를 할 때 range()를 사용
for i in range(10):
    print(i) #0,1,2,3,4,.....9,10

for k in rnange(0,10,2):
    print(k) #0부터 8까지 2씩 증가(end 슬라이스는 포함 아님)


#9) enumrate() 함수 --> 이걸 사용하면 인덱스와 값을 동시에 받을 수 있다
names=['dong','keun','bak']
for i,name in enumrate(names):
    print('iter: ',i) #0,1,2
    print('value ', name) #dong, keun, bak

#10) for와 튜플
tuples_=[(1,2),(2,3)]
for x,y in tuples_:
    print(x,' ',y)
'''
출력결과
1   2                                                                                                                                         
2   3 

#11) zip()함수 --> 여러 시퀀스를 결합해 iterator 생성
columns = ['name', 'shares', 'price']
values = ['GOOG', 100, 490.1 ]
pairs = zip(columns, values)
print(pairs) # ('name','GOOG'), ('shares',100), ('price',490.1)