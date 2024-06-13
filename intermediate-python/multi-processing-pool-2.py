from multiprocessing import Pool

def f(x):
    return x*x

if __name__ == '__main__':
    with Pool(1) as p:
        print(p.map(f, [1, 2, 3, 3, 4, 2, 5, 6, 7, 8]))

