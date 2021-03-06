package JTJD1;
import java.io.*;
public class JTJ1 {
	public static void main(String[] args) {
		System.out.println("Hello World");
		/*
		 #1
		 public: 메소드의 접근 제어자이다. public은 누구나 이 메소드에 접근할 수 있다는 의미
		 static: 메소드에 static이 지정되어 있다면 이 메소드는 인스턴스 생성없이 실행 할 수 있음을 의미
		 --> 그러니까 c++기준으로 생성자인데 인자를 주지 않아도 생성자 호출이 가능하다는 것으로 이해
		 void: 메소드의 리턴값 없음
		 String: 문자열을 나타내는 자바의 자료형
		 args[]: String 자료형에 대한 변수명으로 args 뒤에 []가 있으므로 한 개가 아닌 여러개의 값으로 이루어진 배열임을 의미
		 System.out.println: 표준 출력으로 데이터를 보내는 자바의 내장 메소드로 println 메소드로 들어오는 문자열 값을 화면에 출력한다.
		 
		 #2
		 cmd에서 java 명령어로 실행시
		 C:\Users\12152\eclipse-workspace\JTJ1\bin으로 이동하여
		 'java 패키지명.클래스이름'과 같이 입력하면 실행가능!
		 
		 #3
		 ++,--는 c++과 동일하다
		 ++i의 경우 1이 증가하여 작동
		 i++의 경우 동작 후 1이 증가
		 
		 #4
		 boolean은 참 혹은 거짓
		 boolean isSuccess= true; 참
		 boolean isTest = false 거짓
		 if (isTest){
		 	System.out.println("이 부분은 실행이 안됩니다.")
		 	//왜냐면 isTest가 false이므로
		 }
		 
		 #5
		 char a1 = 'a' 문자값
		 char a2 = 97 아스키코드값
		 char a3 = '\u0061' 유니코드값
		 
		 #6
		 문자열이란 문장을 의미
		 String a ="happy java"; --> 문자형 char와 다르게 "" 쌍따옴표 사용
		 String a = new String("happy java"); -->위의 예와 동일하나 new를 사용하여 객체로 생성할 수 있다.
		 
		 #7
		 String 자료형의 메소드
		*/
	}
}
