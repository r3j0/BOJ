# [Platinum IV] Nawiasy - 8441 

[문제 링크](https://www.acmicpc.net/problem/8441) 

### 성능 요약

메모리: 6292 KB, 시간: 408 ms

### 분류

자료 구조, 세그먼트 트리

### 문제 설명

<p><em>Słowem nawiasowym</em> będziemy nazywali słowo złożone z dwóch rodzajów znaków: nawiasów otwierających, czyli "(", oraz nawiasów zamykających, czyli ")". Wśród wszystkich słów nawiasowych będziemy wyróżniać <em>poprawne wyrażenia nawiasowe</em>. Są to takie słowa nawiasowe, w których występujące nawiasy można połączyć w pary w taki sposób, że:</p>

<ul>
	<li>każda para składa się z nawiasu otwierającego oraz (występującego dalej w słowie nawiasowym) nawiasu zamykającego,</li>
	<li>dla każdej pary fragment słowa nawiasowego zawarty między nawiasami tej pary zawiera tyle samo nawiasów otwierających co zamykających.</li>
</ul>

<p>Na słowie nawiasowym można wykonywać operacje:</p>

<ul>
	<li><em>zamiany</em>, która zamienia <em>i</em>-ty nawias w słowie na przeciwny,</li>
	<li><em>sprawdzenia</em>, która sprawdza, czy słowo nawiasowe jest poprawnym wyrażeniem nawiasowym.</li>
</ul>

<p>Na pewnym słowie nawiasowym wykonywane są kolejno operacje zamiany lub sprawdzenia.</p>

<p>Napisz program, który:</p>

<ul>
	<li>wczyta ze standardowego wejścia słowo nawiasowe oraz ciąg operacji kolejno wykonywanych na tym słowie,</li>
	<li>dla każdej operacji sprawdzenia (występującej we wczytanym ciągu operacji) stwierdzi, czy bieżące słowo nawiasowe jest poprawnym wyrażeniem nawiasowym,</li>
	<li>wypisze wynik na standardowe wyjście.</li>
</ul>

### 입력 

 <p>W pierwszym wierszu wejścia znajduje się jedna liczba całkowita <em>n</em> (1 ≤ <em>n</em> ≤ 30000) oznaczająca długość słowa nawiasowego. W drugim wierszu znajduje się n nawiasów bez znaków odstępu między nimi. W trzecim wierszu znajduje się jedna liczba całkowita m (1 ≤ <em>m</em> ≤ 1000000) oznaczająca liczbę operacji wykonywanych na słowie nawiasowym. W każdym z kolejnych m wierszy znajduje się jedna liczba całkowita. Jeśli w (<em>k</em> + 3)-wierszu (dla 1 ≤ <em>k</em> ≤ <em>m</em>) występuje liczba 0, to znaczy, że k-tą z kolei operacją wykonywaną na słowie nawiasowym jest operacja sprawdzenia. Jeśli zaś jest to liczba całkowita p spełniająca 1 ≤ <em>p</em> ≤ <em>n</em>, to znaczy, że operacją tą jest operacja zamiany p-tego nawiasu na przeciwny.</p>

### 출력 

 <p>Twój program powinien wypisać w kolejnych wierszach (standardowego wyjścia) wyniki kolejnych operacji sprawdzenia. Jeśli bieżące słowo nawiasowe jest poprawnym wyrażeniem nawiasowym, to należy wypisać słowo <code>TAK</code>, w przeciwnym przypadku słowo <code>NIE</code>. (Na wyjściu powinno pojawić się tyle wierszy, ile operacji sprawdzenia zadano na wejściu.)</p>

