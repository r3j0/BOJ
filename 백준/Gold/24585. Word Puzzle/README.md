# [Gold II] Word Puzzle - 24585 

[문제 링크](https://www.acmicpc.net/problem/24585) 

### 성능 요약

메모리: 41064 KB, 시간: 1444 ms

### 분류

다이나믹 프로그래밍, 문자열

### 문제 설명

<p>Young Anna recently indulges in a word puzzle app on her phone. A word puzzle is a single English word with several blanks. Each blank represents a letter to be filled. For example, the word “programming” may appear as a puzzle <code>p_o_rammin_</code>. When solving a puzzle, Anna first clicks on a blank and then begins typing letters. The app automatically advances to the next blank once Anna types a letter. When there are no more blanks to the right of the filled letter, the app jumps back to the beginning of the word and advances from there. Anna keeps typing until all blanks are filled. To solve the puzzle <code>p_o_rammin_</code>, Anna may click on the first blank and type <code>rgg</code>. Alternatively, she may click on the second blank and then type <code>ggr</code>.</p>

<p>One day Anna shows you a puzzle that she solved along with the sequence of letters she typed. Could you tell how many different puzzles can be the one that Anna solved? Two puzzles are different if they have blanks at different positions, e.g. if the puzzle word is <code>programming</code> and Anna typed <code>rgg</code>, there can be two possible puzzles: <code>p_o_rammin_</code> and <code>pro__ammin_</code>. As the answer can be large, output the answer modulo 1,000,000,007.</p>

### 입력 

 <p>The first line of input has a single string p giving the puzzle word (1 ≤ |p| ≤ 10<sup>5</sup>). The second line has a single string s giving the letter sequence that Anna typed (1 ≤ |s| ≤ min(50, |p|)). Both strings contain only lowercase English letters.</p>

### 출력 

 <p>Output the number of different puzzles that can be the one solved by Anna, modulo 1,000,000,007. If Anna can not have typed s to solve the puzzle, output zero.</p>

