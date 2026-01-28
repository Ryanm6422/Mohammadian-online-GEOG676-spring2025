part1 = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]

sum1 = 1
for val in part1:
    sum1 *= val

part2 = [-1, 23, 483, 8573, -13847, -381569, 1652337, 718522177]

sum2 = 0
for val in part2:
    sum2 += val


part3 = [146, 875, 911, 83, 81, 439, 44, 5, 46, 76, 61, 68, 1, 14, 38, 26, 21]

sum3 = 0
for val in part3:
    if val % 2 == 0:
        sum3 += val

print('Part 1 Result: ', sum1)
print('Part 2 Result: ', sum2)
print('Part 3 Result: ', sum3)