import os

for i in range(100):
    print('Running %d' % i)
    os.system('python main.py > runs/run_%d.txt' % i)
