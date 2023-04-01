# Q1
def my_func(x1, x2, x3):
    num_list = [x1, x2, x3]
    for check in num_list:
        if type(check) == int:
            return 'Error: parameters should be float'
        if type(check) == str:
            return None
    sum_tot = x1 + x2 + x3
    if sum_tot == 0:
        return 'Not a number – denominator equals zero'
    num = (sum_tot * (x2 + x3) * x3) / sum_tot
    num = float(num)
    return num

#Exmple
print(my_func(-5.0, 2.0, 3.0))


# Q2
def revword(word):
    word = word[::-1].lower()
    return word


#Example
print(revword('RemoT'))


def countword():
    text_file = open("C:\\Users\\97250\\Desktop\\תואר הנדסה\\שנה ג' סמסטר ב\\data mining\\Tasks\\1\\text.txt", 'r')
    words_dict = dict()
    words_dict['word'] = text_file.readline().rstrip()
    for line in text_file:
        words = line.rstrip().split()
        for i in words:
            rev = revword(i)
            words_dict[rev] = words_dict.get(rev, 0) + 1
    return words_dict[words_dict['word']] + 1


print(countword())

