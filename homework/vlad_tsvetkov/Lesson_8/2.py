def fibonacci_gen(limit=100001):
    prev_num, num = 0, 1
    cnt = 1
    while True:
        yield num
        prev_num, num = num, prev_num + num
        cnt += 1


for cnt, num in enumerate(fibonacci_gen(), start=1):
    if cnt in (5, 200, 1000, 100000):
        print(num)
    if cnt > 100001:
        break
