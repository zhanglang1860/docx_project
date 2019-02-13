import numpy as np

inputchannel = 4
cal_np = np.array([i for i in range(0, inputchannel)])
print(cal_np)


def cal_num_args(numbers, inputchannel):
    if numbers != 1:
        print("asdad")
        for i in range(0, inputchannel):
            pass
            print("numbers" + str(numbers),i)
            return cal_num_args((numbers - 1), inputchannel)
    if numbers == 1:
        return True


cal_num_args(3, 4)

#
# function Recursion(depth) {
#     console.log('抱着');
#     if (!depth) {
#         console.log('我的小鲤鱼')
#     } else {
#         Recursion(--depth);  // 递归调用
#     }
#     console.log('的我');
# }
#
# console.log('吓得我抱起了');
# Recursion(2)

#
# value = int(pow(inputchannel, 1 / numbers)) + 1
# cal_np = np.array([i for i in range(value - numbers * 2, value + numbers * 2)])
#
# # cal_np_number=np.concatenate((cal_np, cal_np), axis=0)
# # number = 2
# # while number < numbers:
# #     cal_np_number = np.concatenate((cal_np_number, cal_np), axis=0)
# #     number = number + 1
# #
# # # print(cal_np_number)
# find = False
# while find != True:
#     cal_np_number = np.random.choice(cal_np, numbers)
#     result = cal_np_number[0]
#     print(cal_np_number)
#     for i in range(0, numbers - 1):
#
#         if cal_np_number[i] < cal_np_number[i + 1]:
#             result = result * cal_np_number[i + 1]
#             if result == inputchannel:
#                 print("this is %s" % (cal_np_number))
#                 find = True


cal_num_args(3, 1024)
