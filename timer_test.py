import timeit

start = timeit.default_timer()

while(True):
    now = timeit.default_timer()
    score = now-start
    print(score)

    # ~15secs
    if(score == 15):
        break

print(score)