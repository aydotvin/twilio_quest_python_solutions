import sys


for i in range(len(sys.argv)):
    string_to_print = f"{i}. {sys.argv[i]}"
    print(string_to_print)
