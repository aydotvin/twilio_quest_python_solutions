import sys

try:
    name = sys.argv[1]
except:
    name = "john"

def hail_friend(n = "john"):
    print(f"Hail, friend! {n}")

hail_friend(name)


def add_numbers(n1, n2):
    return n1+n2

print(add_numbers(4, 3))