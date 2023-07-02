#include <stdio.h>
#include <stdlib.h>
#include <string.h>

int main(void) {
	int n; // 피연산자의 개수
	char str[202];
	int ope_value[26];

	double _operand[101] = {0,};
	int _operand_size = 0;

	scanf("%d", &n);
	scanf("%s", str);
	for (int i = 0; i < n; i++) {
		scanf("%d", &ope_value[i]);
	}

	for (int i = 0; i < strlen(str); i++) {
		if (str[i] == '+') {
			_operand[_operand_size - 2] = _operand[_operand_size - 2] + _operand[_operand_size - 1];
			_operand_size--;
		}
		else if (str[i] == '-') {
			_operand[_operand_size - 2] = _operand[_operand_size - 2] - _operand[_operand_size - 1];
			_operand_size--;
		}
		else if (str[i] == '*') {
			_operand[_operand_size - 2] = _operand[_operand_size - 2] * _operand[_operand_size - 1];
			_operand_size--;
		}
		else if (str[i] == '/') {
			_operand[_operand_size - 2] = (double)_operand[_operand_size - 2] / _operand[_operand_size - 1];
			_operand_size--;
		}
		else { // operand
			_operand[_operand_size] = ope_value[(int)str[i] - 65];
			_operand_size++;
		}
	}

	printf("%.2lf", _operand[0]);

	return 0;
}