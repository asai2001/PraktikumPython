import multiprocessing
def function_square(data):
    result = data*data
    return result
if __name__ == '__main__':
    inputs = list(range(0,19533119))
    pool = multiprocessing.Pool(processes=4)
    pool_outputs = pool.map(function_square, inputs)
    pool.close()
    pool.join()
    print ('Pool :', pool_outputs)
