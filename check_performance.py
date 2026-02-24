import sys

with open('r2 score.txt', 'r') as file:
        r2 = file.read()
        
if float(r2) < 0.65:
    print('Error: Performance Dropped Below 65%')
    sys.exit(1)
else:
    print('Performance Maintained')
    sys.exit(0)