import statistics

list_n = [2,4,6,8,10]

print("AVERAGE")
print(statistics.mean(list_n))
print("MIDDLE")
print(statistics.median(list_n))
print("MOST FREQUENT NUMBER")

try:
    print(statistics.mode(list_n))

except statistics.StatisticsError:
    print("FAILED TO FIND A MOD")


print(statistics.variance(list_n))
print(statistics.stdev(list_n))

if __name__ == '__main__':
    pass