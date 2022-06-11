def positive_or_negative(*args):
    positive_sum = 0
    negative_sum = 0
    for x in args:
        if int(x) > 0:
            positive_sum += int(x)
        else:
            negative_sum += int(x)
    print(f'''{negative_sum}
{positive_sum}''')
    if positive_sum > abs(negative_sum):
        return "The positives are stronger than the negatives"
    else:
        return "The negatives are stronger than the positives"


numbers = [int(x) for x in input().split()]

print(positive_or_negative(*numbers))
