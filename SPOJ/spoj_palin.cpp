/*
 * spoj_palin.cpp
 *
 *  Created on: 30-Jun-2014
 *      Author: brij
 */
#include <iostream>
#include <cstring>
#include <cstdio>
using namespace std;

char str[1001001];
int main() {
	int n, length, mid, odd, p, q, carry, a;
	bool ok = false;
	cin >> n;
	while (n--) {
		scanf("%s", str);
		length = strlen(str);
		mid = (length + 1) / 2;
		odd = (length & 1) ? 1 : 0;
		p = odd ? mid - 2 : mid - 1;
		q = mid;
		ok = false;
		while (p >= 0 && q < length) {
			if (str[p] > str[q]) {
				str[q] = str[p];
				ok = true;
			}
			else if (str[p] == str[q]){
				str[q] = str[p];
			} else {
				break;
			}
			p--; q++;
		}

		if (!ok) {
			p = mid - 1;
			q = odd ? mid - 1 : mid;
			carry = 1;
			while (p >= 0 || carry) {
				a = (p >= 0) ? (str[p] - '0') : 0;
				str[q] = (a + carry) % 10 + '0';
				carry = (a + carry) / 10;
				p--; q++;
			}
			str[q] = 0;
			p = 0; q--;
			while (p < q) {
				str[p] = str[q];
				p++; q--;
			}
		}
		printf("%s\n", str);
	}
	return 0;
}



