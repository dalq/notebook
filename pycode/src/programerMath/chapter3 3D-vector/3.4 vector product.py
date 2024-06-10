from numpy import cross

if __name__ == '__main__':
    print('(0,0,1) x (1,2,3) = {}'.format(cross((0, 0, 1), (1, 2, 3))))
    print('(0,0,1) x (-1,-1,0) = {}'.format(cross((0, 0, 1), (-1, -1, 0))))
    print('(0,0,1) x (1,-1,5) = {}'.format(cross((0, 0, 1), (1, -1, 5))))
