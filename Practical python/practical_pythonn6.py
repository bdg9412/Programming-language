#객체

#1) main
'''
파이썬에는 c++의 int main()과 같은 메인 함수가 없다.
그 대신 메인 모듈이 있다. 이는 처음 실행하는 소스 파일이다.
import 되었을 경우는 메인프로그램이 아니고
python3 이름.py와 같이 메인으로서 실행된다면 메인 프로그램이 된다.
'''
if __name__ =="__main__":
    #메인 프로그램으로서 실행

#2) 클래스
class Player:
    def __init__(self, x, y): #c++의 생성자와 같다. 객체 선언시 초기값!
        #self가 의미하는 것은 각 인스턴스에 저장된 값이다! 
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy

    def damage(self, pts):
        self.health -= pts

p= Player(2,3) #클래스를 함수로서 호출하여 인스턴스 생성. 여기서 p는 인스턴스
p_other=Player(10,29) #p와 p_other의 클래스는 전혀 다른 로컬 값을 갖고있다.

print(p.x) #p의 __init__을 통하여 p 인스턴스의 x에 2가 저장되었으므로 2를 출력
print(p_other.x) #p_other의 __init__을 통하여 p_other 인스턴스의 x에 10가 저장되었으므로 10를 출력

print(p.move(2,3)) #p 인스턴스의 x는 2였는데 move함수를 통하여 2를 더해주게 되었으므로 4를 출력
# 위 함수 호출은 다음과 같이 이루어진다.
# `p`를 `self`와 매치
# `2`을 `dx`와 매치
# `3`를 `dy`와 매치

#3) 클래스 상속
class Parent:
    #do some logic

class Child(Parent):
    #this is subclass

#예시 --> 앞서 구현한 Player 클래스를 상속
    
class Player:
    def __init__(self, x, y): #c++의 생성자와 같다. 객체 선언시 초기값!
        #self가 의미하는 것은 각 인스턴스에 저장된 값이다! 
        self.x = x
        self.y = y
        self.health = 100

    def move(self, dx, dy):
        self.x += dx
        self.y += dy
        return self.x, self.y
    def damage(self, pts):
        self.health -= pts

#예시 --> 앞서 구현한 Player 클래스를 상속
class Stock(Player):
    def calculate(self):
        self.move(self.x,self.y)
        return self.x, self.y

sub=Stock(2,3)
print(sub.move(2,3)) #(4, 6)
print(sub.calculate()) #(8, 12) self.x가 4가 self.y가 6이므로 이를 두배 한 값!

#4) __init__와 상속
#__init__를 재정의하려면 부모를 초기화해야 한다.
class Stock:
    def __init__(self, name, shares, price):
        self.name = name
        self.shares = shares
        self.price = price

class MyStock(Stock):
    def __init__(self, name, shares, price, factor):
        # `super`와 `__init__`에 대한 호출을 확인
        super().__init__(name, shares, price)#super()는 부모 호출로 생각!
        self.factor = factor

    def cost(self):
        return self.factor * super().cost()

'''
한개의 부모를 여러 개의 자식이 상속받을 수 있고
아래와 같이 한개의 자식이 여러 클래스로부터 상속받을 수 있다.
class Mother:
    ...

class Father:
    ...

class Child(Mother, Father):
    ...
'''
