# [Gold IV] Sierpinski 삼각형 - 3158 

[문제 링크](https://www.acmicpc.net/problem/3158) 

### 성능 요약

메모리: 108080 KB, 시간: 108 ms

### 분류

애드 혹, 구현

### 제출 일자

2024년 1월 2일 16:09:58

### 문제 설명

<p><a href="https://en.wikipedia.org/wiki/Wac%C5%82aw_Sierpi%C5%84ski">Wacław Sierpiński</a>는 폴란드 수학자이다. 어느 날 그는 아래와 같은 방법으로 삼각형을 그리기로 했다.</p>

<ul>
	<li>정삼각형 T를 그린다.</li>
	<li>삼각형 변의 중점을 서로 연결한다. 새롭게 생긴 정삼각형을 T1, T2, T3, T4라고 한다. 아래 그림 중 왼쪽 그림이 해당한다.</li>
	<li>위의 단계를 삼각형 T1, T2, T3에 대해서 반복한다. 새로운 삼각형은 T11, T12, T13, T14, T21, T22, T23, T24, T31, T32, T33, T34가 된다.</li>
	<li>1, 2, 3으로 끝나는 모든 삼각형에 대해서 이 방법을 반복한다. 이렇게 생긴 프랙탈을 <a href="https://en.wikipedia.org/wiki/Sierpinski_triangle">Sierpinski 삼각형</a>이라고 한다.</li>
</ul>

<p style="text-align: center;"><img alt="" src="https://upload.acmicpc.net/d80a2cee-5de9-4c38-87ee-b01e39765eb8/-/preview/" style="width: 437px; height: 173px;"></p>

<p>삼각형 B가 삼각형 A를 포함하지 않고, A의 한 변 전체가 B의 한 변의 일부일 때, A는 B에 기대고 있다고 한다. 예를 들어, 삼각형 T23은 T24와 T4에 기대고 있지만, T2와 T32에는 기대고 있지 않다. (A가 B에 기대고 있다는 말은 B가 A에 기대고 있다는 말을 포함하지 않는다)</p>

<p>Sierpinski 삼각형의 일부 삼각형 A가 주어진다. 이때, A가 기대고 있는 모든 삼각형 B를 찾는 프로그램을 작성하시오.</p>

### 입력 

 <p>첫째 줄에 삼각형 A가 주어진다. 삼각형 A의 이름은 2글자보다 크거나 같고, 50글자보다 작거나 같다. </p>

### 출력 

 <p>삼각형 A가 기대고 있는 모든 삼각형을 한 줄에 하나씩 출력한다. 출력하는 순서는 아무 순서나 상관없다.</p>

