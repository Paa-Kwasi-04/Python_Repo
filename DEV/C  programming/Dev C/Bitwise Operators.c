#include <stdio.h>

int a, b, c, d, e, f, g, h, i, j, k;

int main() {
    printf("what is a: ");scanf("%d", &a);
    printf("what is b: ");scanf("%d", &b);

    c = a & b;
    d = a | b;
    e = a ^ b;
    f = a << 2;
    g = a >> 2;
    h = b << 2;
    i = b >> 2;
    j = ~a;
    k = ~b;
    printf("a&b is:%d\n", c);
    printf("a|b is:%d\n", d);
    printf("a^b is:%d\n", e);
    printf("a<<2 is:%d\n", f);
    printf("a>>2 is:%d\n", g);
    printf("b<<2 is:%d\n", h);
    printf("b>>2 is:%d\n", i);
    printf("~a is:%d\n", j);
    printf("~b is:%d", k);


    return 0;
}
