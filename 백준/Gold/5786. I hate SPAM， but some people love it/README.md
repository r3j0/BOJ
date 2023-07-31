# [Gold V] I hate SPAM, but some people love it - 5786 

[문제 링크](https://www.acmicpc.net/problem/5786) 

### 성능 요약

메모리: 117232 KB, 시간: 180 ms

### 분류

너비 우선 탐색, 깊이 우선 탐색, 그래프 이론, 그래프 탐색

### 문제 설명

<p>Nowadays, unfortunately, SPAM messages are becoming more and more common. Some of them may have a multiplicative effect since they ask you to forward them to all your friends. Some SPAM messages wish good luck, others promise you will become rich, and others just remind you how important it is to tell your friends that you care for their friendship. Here is an example of a SPAM:</p>

<blockquote>
<p>From: Alice<br>
To: Bob, Mary, Julia, Paul</p>

<p>Hi, this is a good luck email. I wish you become a millionaire, but<br>
that is up to you. If you<br>
* send this email to 10 or more people you will be a millionaire<br>
* send this email to 5 or more people you will be rich<br>
* send this email to less than 5 people you will be poor<br>
As I said, it is up to you. Write your email and be rich! :-)</p>

<p>Alice</p>
</blockquote>

<p>People usually react in two different ways when they receive a SPAM:</p>

<ul>
	<li>They discard the message immediately without even reading it (they hate SPAM); </li>
	<li>They forward the message to everyone they know (they love SPAM).</li>
</ul>

<p>For this problem, we will assume everyone loves SPAM, but one never forwards the same message twice. Each SPAM message has a different effect based on the number of friends you forward the message to. For example: a SPAM message could tell that you will be poor if you send the message to 5 friends, but you will be the rich if you send to 10, and you will be the richest man in the world if you send it to 20 friends, and so on.</p>

<p>We will consider only SPAM messages similar to the example above. More specifically, a SPAM message will define two threshold values T<sub>1</sub> and T<sub>2</sub> and three attributes A<sub>1</sub>, A<sub>2</sub> and A<sub>3</sub>. A person acquires one of the three attributes depending on the number of messages forwarded for that specific SPAM. If a person forwards T messages and T < T<sub>1</sub> then her/his attribute is A<sub>1</sub>, if T<sub>1</sub> ≤ T < T<sub>2</sub> then her/his attribute is A<sub>2</sub>, otherwise her/his attribute is A<sub>3</sub>.</p>

<p>You will be given the names of a group of people, and for each person in the group, the set of friends she/he knows the email address. You will also be given a set of distinct SPAM messages, and for each SPAM message its threshold values and attributes, and the information about which person started it. You have to write a program that determines, for each person in the given group, which attributes she/ he acquired, based on all the SPAM they forward.</p>

<p>You may assume that the SPAM originator will have at least one friend (in other words, she/he will send at least one message), and a person will not send messages to herself.</p>

### 입력 

 <p>Your program should process several test cases. The first line of a test case contains an integer N indicating the number of persons in the group (2 ≤ N ≤ 20). In the input, a person is identified by an integer from 1 to N. The following N lines contain each a list of friends of each person (the i-th line contains the list of friends of person number i). The list of friends of person i describes the friends person i knows the email address, and consists of a list of integers F<sub>i</sub> (1 ≤ F<sub>i</sub> ≤ N, F<sub>i</sub> ≠ i) terminated by the value 0 (zero). Following the list of friends comes the description of the SPAM messages (there will be at most 100 messages). Each description appears in a different line. The description consists of an integer P identifying the person who is the SPAM originator (2 ≤ P ≤ N); two integers T<sub>1</sub> and T<sub>2</sub> representing the threshold values; and the three attributes A<sub>1</sub>, A<sub>2</sub> and A<sub>3</sub> (each attribute is a word of no more than 20 letters). The SPAM list ends with a line containing only the value 0 (zero). The following N lines contain each a name, which is single word with no more than 20 letters. The name in the i-th line is the name of person number i. The end of input is indicated by N = 0.</p>

### 출력 

 <p>For each test case your program should output a list of names followed by the attributes they acquired. Your program should write the persons names in the order they appear in the input, followed by ’:’ and by a space, followed by their attributes according to the SPAM they sent. Attributes should be written in the order they appear in the input; each attribute should be followed by a space.</p>

<p> </p>

