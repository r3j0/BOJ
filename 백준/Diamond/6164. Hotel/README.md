# [Diamond V] Hotel - 6164 

[문제 링크](https://www.acmicpc.net/problem/6164) 

### 성능 요약

메모리: 6708 KB, 시간: 32 ms

### 분류

자료 구조, 느리게 갱신되는 세그먼트 트리, 세그먼트 트리

### 제출 일자

2025년 2월 1일 17:28:22

### 문제 설명

<p>The cows are journeying north to Thunder Bay in Canada to gain cultural enrichment and enjoy a vacation on the sunny shores of Lake Superior. Bessie, ever the competent travel agent, has named the Bullmoose Hotel on famed Cumberland Street as their vacation residence. This immense hotel has N (1 <= N <= 50,000) rooms all located on the same side of an extremely long hallway (all the better to see the lake, of course).</p>

<p>The cows and other visitors arrive in groups of size D_i (1 <= D_i <= N) and approach the front desk to check in. Each group i requests a set of D_i contiguous rooms from Canmuu, the moose staffing the counter.  He assigns them some set of consecutive room numbers r..r+D_i-1 if they are available or, if no contiguous set of rooms is available, politely suggests alternate lodging. Canmuu always chooses the value of r to be the smallest possible.</p>

<p>Visitors also depart the hotel from groups of contiguous rooms. Checkout i has the parameters X_i and D_i which specify the vacating of rooms X_i..X_i+D_i-1 (1 <= X_i <= N-D_i+1). Some (or all) of those rooms might be empty before the checkout.</p>

<p>Your job is to assist Canmuu by processing M (1 <= M < 50,000) checkin/checkout requests. The hotel is initially unoccupied.</p>

### 입력 

 <ul>
	<li>Line 1: Two space-separated integers: N and M</li>
	<li>Lines 2..M+1: Line i+1 contains request expressed as one of two possible formats: (a) Two space separated integers representing a check-in request: 1 and D_i (b) Three space-separated integers representing a check-out: 2, X_i, and D_i</li>
</ul>

<p> </p>

### 출력 

 <ul>
	<li>Lines 1.....: For each check-in request, output a single line with a single integer r, the first room in the contiguous sequence of rooms to be occupied. If the request cannot be satisfied, output 0.</li>
</ul>

<p> </p>

