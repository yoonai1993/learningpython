# 如果语句很长，我们可以使用反斜杠(\)来实现多行语句
item_one, item_two, item_three = 2, 3, 4
total = item_one + \
        item_two + \
        item_three
print(total)

# 在 [], {}, 或 () 中的多行语句，不需要使用反斜杠(\)，例如：
total = ['item_one', 'item_two', 'item_three',
        'item_four', 'item_five']