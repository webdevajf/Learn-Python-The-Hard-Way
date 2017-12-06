print('1 ', 4 < 6) #True
print('2 ', 8 > 1) #True
print('3 ', 2 == 4) #False
print('4 ', 5 != 5) #False
print('5 ', (not True and 5 > 4)) #False
print('5a ', ((not True) and 5 > 4)) #False
print('5b ', (not False and 5 > 4)) #True
print('5c ', ((not False) and 5 > 4)) #True
print('6 ', 8 == 8 and 7 <= 12) #True
print('7 ', 12 >= 19 or not False) #True
print('8 ', 8 != 9 and not(6 < 7 or 10 < 12)) #False
print('9 ', 32 > 14 and not(12 == 3 or not(9 > 10))) #False
