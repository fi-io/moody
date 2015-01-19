/*
 * spoj_palin2.c
 *
 *  Created on: 30-Jun-2014
 *      Author: brij
 */

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

char digittable[10] = {'1','2','3','4','5','6','7','8','9','0'};

char *next_small(char *k) {
    int len = strlen(k);
    char *next;
    if(len == 1) {
        char d = digittable[k[0]-48];
        if(d == '0') {
            next = calloc(3, sizeof(char));
            next[0] = '1';
            next[1] = '1';
            return next;
        }
        else {
            next = calloc(2, sizeof(char));
            next[0] = d;
            return next;
        }
    }
    else {
        if(k[0] == k[1]) {
            if(k[0] == '9') {
                next = calloc(4, sizeof(char));
                next[0] = '1';
                next[1] = '0';
                next[2] = '1';
                return next;
            }
            else {
                next = calloc(3, sizeof(char));
                next[0] = k[0]+1;
                next[1] = k[1]+1;
                return next;
            }
        }
        else {
            if(k[0] < k[1]) {
                next = calloc(3, sizeof(char));
                next[0] = k[0]+1;
                next[1] = next[0];
                return next;
            }
            else {
                next = calloc(3, sizeof(char));
                next[0] = k[0];
                next[1] = k[0];
                return next;
            }
        }
    }
}

char *fix_zero(char *k) {
    int len = strlen(k);
    int i;
    for(i = 0; i < len; i++) {
        if(k[i] != '0')
            return k;
    }

    char *next = calloc(len+2, sizeof(char));
    strcpy(next+1, k);
    next[0] = '1';
    next[len] = '1';
    return next;
}

char *next_odd(char *k) {
    int len = strlen(k);
    int mid = len/2;
    bool inc_mid = true;
    char *next = calloc(len + 1, sizeof(char));
    strcpy(next, k);
    int i;
    for(i = 0; i < mid; i++) {
        if(k[len-i-1] < k[i])
            inc_mid = false;
        else if(k[len-i-1] > k[i])
            inc_mid = true;
        next[len-i-1] = k[i];
    }
    if(inc_mid) {
        char d = digittable[k[mid]-'0'];
        next[mid] = d;
        int j = 1;
        while(d == '0') {
            d = digittable[k[mid-j]-'0'];
            next[mid-j] = d;
            j++;
        }
        for(i = 0; i < mid; i++) {
            next[len-i-1] = next[i];
        }
    }
    return fix_zero(next);
}

char *next_even(char *k) {
    int len = strlen(k);
    int mid = len/2-1;
    bool inc_mid = true;
    char *next = calloc(len + 1, sizeof(char));
    strcpy(next, k);
    int i;
    for(i = 0; i < mid; i++) {
        if(k[len-i-1] < k[i])
            inc_mid = false;
        else if(k[len-i-1] > k[i])
            inc_mid = true;
        next[len-i-1] = k[i];
    }
    if(inc_mid) {
        if(next[mid] == next[mid+1]) {
            if(next[mid] == '9') {
                next[mid] = '0';
                next[mid+1] = '0';
            }
            else {
                next[mid]++;
                next[mid+1]++;
            }
        }
        else {
            if(next[mid] < next[mid+1]) {
                next[mid]++;
                next[mid+1] = next[mid];
            }
            else {
                next[mid+1] = next[mid];
            }
        }
        int j = 1;
        while(next[mid-j+1] == '0') {
            next[mid-j] = digittable[next[mid-j]-'0'];
            j++;
        }
        for(i = 0; i < mid; i++) {
            next[len-i-1] = next[i];
        }
    }
    return fix_zero(next);
}

int main() {
    int t;
    scanf("%d", &t);
    int i;
    for(i = 0; i < t; i++) {
        char k[1000000];
        scanf("%s", k);
        int len = strlen(k);
        if(len <= 2)
            printf("%s\n", next_small(k));
        else if(len % 2 == 0)
            printf("%s\n", next_even(k));
        else
            printf("%s\n", next_odd(k));
    }
    return 0;
}


