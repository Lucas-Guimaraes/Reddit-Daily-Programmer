#https://www.reddit.com/r/dailyprogrammer/comments/yj2zq/8202012_challenge_89_easy_simple_statistical/
#'89easytest.txt' is a supplementary file
#modes available: mean, variance, and sd (standard deviation)

#Checks the mode
def simple_statistics(file, mode):
    f = open(file, 'r')
    data = []
    for line in f:
        data.append(float(line))
    
    if mode == 'mean':
        return mean(data)
    elif mode == 'variance':
        return variance(data)
    elif mode == 'sd':
        return standard_deviation(data)

#Mode #1. Returns the mean.
def mean(data):
    return round(sum(data) / len(data), 4)
    
#Mode #2. Returns the Variance.
def variance(data):
    mean_for_v = mean(data)
    total_variance = []
    for i in range(0,len(data)):
        total_variance.append((data[i] - mean_for_v) ** 2)
    var = round((1.0/len(data)*sum(total_variance)),4)
    return var

#Mode #3. Returns the Standard Deviation.
def standard_deviation(data):
    standard_d = round(variance(data) ** 0.5, 4)
    return standard_d
    
file_name = '89easytest.txt'
print(simple_statistics(file_name, 'mean'))
print(simple_statistics(file_name, 'variance'))
print(simple_statistics(file_name, 'sd'))
raw_input()