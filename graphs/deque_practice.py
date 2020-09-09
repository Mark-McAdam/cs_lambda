from collections import deque

dq = deque("abcdefg")

print("Deque:", dq)
print("Length - DQ", len(dq))
print("left side", dq[0])
print("right side", dq[-1])

dq.remove("c")
print("Deque: remove c", dq)


print()
print("populating")
# Add to the right
d1 = deque()
d1.extend("abcdefg")
print("extend    :", d1)
d1.append("h")
print("append    :", d1)

# Add to the left
d2 = deque()
d2.extendleft(range(6))
print("extendleft:", d2)
d2.appendleft(6)
print("appendleft:", d2)


print()
print("consuming")
print("From the right:")
d = deque("abcdefg")
while True:
    try:
        print(d.pop(), end="")
    except IndexError:
        break
print()

print("\nFrom the left:")
d = deque(range(6))
while True:
    try:
        print(d.popleft(), end="")
    except IndexError:
        break
print()
