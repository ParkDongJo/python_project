import matplotlib.pyplot as plt

# data_x1 = [2,3,5,7,9]
# data_y1 = [5,3,9,2,8]
# data_x2 = [2,4,6,8,10]
# data_y2 = [8,7,2,11,4]
#
# plt.bar(data_x1, data_y1, label='Set 1', color='b')
# plt.bar(data_x2, data_y2, label='Set 2', color='g')
# plt.legend()
# plt.title('Bar Chart')
#
# print(plt.show())


def print_bar():

    data_x = ['1그룹','2그룹','3그룹','4그룹','5그룹']
    data_y = [5,3,9,2,8]
    data_y = [5,3,9,2,8]
    data_y = [5,3,9,2,8]
    data_y = [5,3,9,2,8]

    plt.bar(data_x, data_y2, label='Set 1', color='b')
    plt.bar(data_x, data_y2, label='Set 2', color='g')
    plt.bar(data_x, data_y2, label='Set 3', color='r')
    plt.bar(data_x, data_y2, label='Set 4', color='y')
    plt.bar(data_x, data_y2, label='Set 5', color='g')
    plt.legend()
    plt.title('Bar Chart')

    print(plt.show())