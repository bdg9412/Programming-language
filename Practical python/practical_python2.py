#1) 문자열 포매팅

'''

      Name      Shares        Price

----------  ----------  -----------

        AA         100        32.20

       IBM          50        91.10

       CAT         150        83.44

      MSFT         200        51.23

        GE          95        40.37

      MSFT          50        65.10

       IBM         100        70.44

       

위 처럼 구조화된 출력을 생성하고자 하는 경우가 생기는데 이럴 경우

f 문자열을 사용하여 문자열 포매팅을 수행할 수 있다.

{표현식: 포맷}, print(f'{name:10s} {Shares:10d} {price:10.2f}')

 

d: 정수

f: 부동소수점수

s: 문자열

c: 문자

 

:>10d 정수를 10자리 필드에 오른쪽 정렬, :<10d 정수를 10자리 필드에 왼쪽 정렬 

:^10d 정수를 10자리 필드에 가운데 정렬, :0.2f 부동소수점수를 두 자리 정밀도로 나타낸다

'''

 

s = {

    'name': 'IBM',

    'shares': 100,

    'price': 91.1

}

 

#2) format_map() 메서드를 사용해 값들의 딕셔너리에 문자열 포매팅을 적용할 수 있다.

print('{name:>10s} {shares:10d} {price:10.2f}'.format_map(s)) #       IBM        100      91.10: 출력예