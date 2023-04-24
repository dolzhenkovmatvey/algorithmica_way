def make_prefix_sum(a: list[int]) -> list[int]:
    n = len(a)
    prefix_sum = [0 for _ in range(n + 1)]
    for i in range(0, n):
        prefix_sum[i + 1] = a[i] + prefix_sum[i]
    return prefix_sum


def has_target_segment(a: list[int], target: int) -> (int, int):
    prefix_sum = make_prefix_sum(a)
    hash_map = {}
    n = len(prefix_sum)
    for i in range(n):
        if prefix_sum[i] in hash_map:
            l, r = i, hash_map[prefix_sum[i]]
            if l > r:
                l, r = r, l
            return l+1, r
        else:
            hash_map[target + prefix_sum[i]] = i
    return -1, -1


def main():
    a = list(map(int, input().split()))
    target = int(input())
    print(has_target_segment(a, target))


if __name__ == '__main__':
    main()
