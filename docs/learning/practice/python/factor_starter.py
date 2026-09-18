"""A small, offline Python 3 starter. No third-party packages or network access.

只填写 count_factors；main 已负责运行示例。
Fill in count_factors only; main runs the examples for you.
"""


def count_factors(n):
    """Count positive divisors of integer n >= 2, excluding 1 and n itself.

    例如 12 的候选人是 2 到 11；能整除 12 才算入选。
    For 12, candidates run from 2 to 11; count only those dividing 12.
    不要把 2、4、12 的答案直接写死。/ Do not hard-code sample answers.
    """
    # TODO: start a counter, try candidates with for/if, then return the count.
    # TODO：先设计数器，再用 for/if 检查候选数，最后 return 计数。
    raise NotImplementedError


def main():
    print("Python ready / Python 已启动。")
    try:
        results = [(n, count_factors(n), expected)
                   for n, expected in [(2, 0), (4, 1), (12, 4)]]
    except NotImplementedError:
        print("Starter ready; fill in count_factors and run again.")
        print("骨架运行正常；请填写 count_factors 后再运行。")
        return
    for n, actual, expected in results:
        print(f"n={n}: got / 得到 {actual}; expected / 预期 {expected}")
    if any(actual != expected for _, actual, expected in results):
        print("Recheck candidates, the remainder test and return indentation.")
        print("先检查候选范围、余数判断，以及 return 的缩进。")
        return
    # This summarizes YOUR function, not a supplied implementation of it.
    counts = [count_factors(n) for n in range(2, 101)]
    if any(type(value) is not int or value < 0 for value in counts):
        print("Return a nonnegative integer for every input / 每个输入都应返回非负整数。")
        return
    frequencies = {value: counts.count(value) for value in sorted(set(counts))}
    print("Outputs / 输出个数:", len(counts))
    print("Count -> frequency / 因数个数 -> 出现频数:", frequencies)
    print("Frequency sum / 频数之和:", sum(frequencies.values()))
    print("99 outputs alone do not prove every count is correct.")
    print("99 个输出只是范围检查；请另用 7 和 100 手算核对，再画两种图。")


if __name__ == "__main__":
    main()
