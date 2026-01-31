import time
string = "无人扶我青云志，我自踏雪之山巅"
print("-------------")
for char in string:
    print(char, flush=True, end='')
    time.sleep(0.5)
print()
