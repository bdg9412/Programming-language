package JTJD1;

public class JTJ2 {

     public static void main(String []args){

        System.out.println("Hello World");

        //String 메소드

        //1) equals: 두 개의 문자열이 동일한 값을 가지고 있는지를 비교하여 결과값을 리턴

        String a ="hello";

        String b = "java";

        System.out.println(a.equals(b)); //문자열 비교 수행 a와 b의 문장이 서로 다르므로 false

        

        String c =new String("hello");

        System.out.println(a.equals(c)); //문자열 비교 수행 a와 c의 문장이 서로 같으므로 true

        System.out.println(a == c); //==는 두개의 자료형이 동일한 객체인지를 판별한다. 허나 여기서 두개는 서로 다른 객체임으로 false 출력

        //2)indexOf: 문자열에서 특정 문자가 시작되는 인덱스를 리턴

        String a1 = "hello java";

        System.out.println(a1.indexOf("java")); //6출력

        

        //3)replaceAll: 문자열 중 특정 문자를 다른 문자로 바꾸고 싶을 때 사용

        String a2 = "hello hello2";

        System.out.println(a2.replaceAll("hello2","java")); //hello java 출력

        

        //substring: 문자열 중 특정 부분을 뽑아낼 경우에 사용

        String a3 = "hello java";

        System.out.println(a3.substring(0,4)); //hell 출력

        

        //toUpperCase: 문자열을 대문자로 변경

        String a4 = "Hello Java";

        System.out.println(a4.toUpperCase()); //HELLO JAVA 출력

        

        

        //StringBuffer

        //StringBuffer는 문자열을 추가하거나 변경할 때 주로 사용하는 자료형

        //파이썬의 리스트인데 string형의 리스트인 것 같다.

        StringBuffer sb = new StringBuffer();

        sb.append("hello");

        sb.append(" ");

        sb.append("jump to java");

        sb.insert(0,"everyone "); //삽입 위치, 삽임 대상 선택 

        //substring의 경우 String과 사용법 동일

        System.out.println(sb.toString()); //everyone hello jump to java 출력

        

        /*

        위 과정은 아래와 같다.

        String temp = "";

        temp += "hello";

        temp += " ";

        temp += "jump to java";

        System.out.println(temp);

        

        두가지 경우 모두 동일한 결과를 도출하지만 내부적으로 객체가 생성되고 메모리가 사용되는 과정이 다르다.

        첫번째 예의 경우 StringBuffer 객체는 단 한번만 생성된다. 반면에 두번째 예의 경우에는 String 자료형에 + 연산이 있을 때마다 새로운 String 객체가 생성된다.

        그러나 StringBuffer 객체는 String보다 훨씬 무겁다. 자신의 개발 과정에 따라 String과 StringBuffer를 선택하면 될 것 같다.

        

        */
        
        

     }

}
