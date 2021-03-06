package JTJD1;

public class JTJ3 {
	//#1 배열: 자료형 종류가 아닌 자료형 집합
	//	 배열은 자료형 앞에 []을 붙여서 나타낸다.
	int[] odds = {1,3,5,7,9}; //int형 배열
	String[] weeks = {"월","화","수","목","금"}; //문자열 배열
	
	//#2 배열은 위 처럼 값을 할당하여 선언하는 방식과 배열의 길이만 미리 설정하여 변수를 생성한 후 값을 대입하는 방식이 있다.
	String[] weeks_after= new String[7];
	
	//#3 배열의 값에 접근하는 방식은 파이썬 리스트와 마찬가지
	System.out.println(weeks[0]);

	//#4 배열의 길이
	String weeks_len = {"월","화"};
	System.out.println(weeks_len.length); //2
}
