#include <stdio.h>
#include <stdlib.h>
#include <math.h>

#define ll long long

ll init(ll* arr, ll* tree, ll node, ll start, ll end){
    if (start == end)
        return tree[node] = arr[start];

    ll mid = (start + end) / 2;

    return tree[node] = init(arr, tree, node * 2, start, mid) + init(arr, tree, node * 2 + 1, mid + 1, end);
}

void update(ll* tree, ll node, ll start, ll end, ll index, ll diff){
    if (index < start || index > end) return;

    tree[node] += diff;

    if (start != end) {
        ll mid = (start + end) / 2;
        update(tree, node * 2, start, mid, index, diff);
        update(tree, node * 2 + 1, mid + 1, end, index, diff);
    }
}

ll sum(ll* tree, ll node, ll start, ll end, ll left, ll right){
    if (left > end || right < start)
        return 0;

    if (left <= start && end <= right)
        return tree[node];

    ll mid = (start + end) / 2;

    return sum(tree, node * 2, start, mid, left, right) + sum(tree, node * 2 + 1, mid + 1, end, left, right);
}

int main() {
    ll n, m, k;
    scanf("%lld %lld %lld", &n, &m, &k);
    ll* arr = (ll*)malloc(sizeof(ll) * (n + 1));
    for(ll i=1; i<=n; i++){
        scanf("%lld", &arr[i]);
    }
    ll h = (ll)ceil(log2(n));
    ll tree_size = (1 << (h + 1));
    ll* tree = (ll*)malloc(sizeof(ll) * tree_size);
    init(arr, tree, 1, 1, n);
    m += k;
    while(m--){
        ll a, b, c;
        scanf("%lld %lld %lld", &a, &b, &c);
        if(a == 1){
            ll diff = c - arr[b];
            arr[b] = c;
            update(tree, 1, 1, n, b, diff);
        }
        else{
            printf("%lld\n", sum(tree, 1, 1, n, b, c));
        }
    }
    return 0;
}
