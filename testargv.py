import sys

print(len(sys.argv))
print(sys.argv)

if "-h" in sys.argv:
    print("help is here!")
    
for s in sys.argv:
    print(s)