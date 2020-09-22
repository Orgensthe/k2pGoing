def find_maximum_card(card):

    maximum_number = 0
    for idx in range(len(card)):
        minimum_number = min(card[idx])
        if maximum_number < minimum_number:
            maximum_number = minimum_number

    return maximum_number


n = 2
m = 4

card = [[7, 3, 1, 8], [3, 3, 3, 4]]
maximum_number = find_maximum_card(card)
print(maximum_number)
