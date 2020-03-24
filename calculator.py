import re

def add(str):
    str_list = []
    neg_str = []

    if len(str) == 0: return 0

       
    for each_letter in re.findall(r"-?\d+", str):
        try:
            if int(each_letter) >= 1000:
                each_letter = 0
            if int(each_letter) < 0:
                neg_str.append(each_letter)
            str_list.append(int(each_letter))
        except:
            continue
            
    if len(neg_str) > 0:
        raise Exception('negatives not allowed: {}'.format(neg_str))

    return sum(str_list)
