def mean(data):
    mean = sum(data) / len(data)
    return mean

def median(data):
    x = data.sort()
    if len(data) % 2 !=0:
        pos_median = (len(data) + 1) / 2
        pos_median = int(pos_median)
        median = data[pos_median-1]
    else:
        pos_median = len(data) / 2
        pos_median = int(pos_median)
        median = (data[pos_median-1] + data[pos_median]) / 2
    return median

def mode(data, freq=False):
    counter = 0
    num = data[0]
    
    for item in data:
        count_item = data.count(item)
        if (count_item > counter):
            counter = count_item
            num = item
    if freq == True:
        return num, counter
    else :
        return num

def var(data):
    n_data_squared = []
    for item in data:
        squared = item * item
        n_data_squared.append(squared)

    sum_n_data_squared = sum(n_data_squared)
    avg_sum_data_squared = (sum(data) * sum(data)) / len(data)
    data_size = len(data) - 1
    var = (sum_n_data_squared-avg_sum_data_squared) / data_size
    return var

def stdev(data):
    n_data_squared = []
    for item in data:
        squared = item * item
        n_data_squared.append(squared)

    sum_n_data_squared = sum(n_data_squared)
    avg_sum_data_squared = (sum(data) * sum(data)) / len(data)
    data_size = len(data) - 1
    var = (sum_n_data_squared-avg_sum_data_squared) / data_size
    stdev = var**(1/2)
    return stdev

def describe(data):
    print('\n-----Data Description-----\n')

    desc_mean = mean(data)
    desc_median = median(data)
    desc_mode = mode(data)
    desc_var = var(data)
    desc_stdev = stdev(data)

    print('Min                 :', min(data))
    print('Max                 :', max(data))
    print('Mean                :', desc_mean)
    print('Median              :', desc_median)
    print('Mode                :', desc_mode)
    print('Variance            :', desc_var)
    print('Standar Deviation   :', desc_stdev)

    print('\n---------------------------')