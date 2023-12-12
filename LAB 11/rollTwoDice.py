import random

def roll_dice():
    die1 = random.randint(1, 6)
    die2 = random.randint(1, 6)
    return die1, die2

def make_2d_array(dice_rolls):
    array = [[0 for _ in range(6)] for _ in range(6)]

    for die1, die2 in dice_rolls:
        total = die1 + die2
        array[die1 - 1][die2 - 1] = total

    return array

def print_2d_array(array):
    for row in array:
        print(row)

def print_distinct_sums(array):
    distinct_sums = sorted(set(val for row in array for val in row))
    frequencies = [sum(row.count(sum_value) for row in array) for sum_value in distinct_sums]
    relative_frequencies = [freq / 36 for freq in frequencies]

    print("Sum:", distinct_sums)
    print("Frequency:", frequencies)
    print("Relative Frequency:", relative_frequencies)

    index_of_six = distinct_sums.index(6)
    classical_probability_of_six = relative_frequencies[index_of_six]
    print(f"\nClassical Probability of Sum 6: {classical_probability_of_six:.4f}")

if __name__ == '__main__':
    dice_rolls = [roll_dice() for _ in range(10000)]
    array = make_2d_array(dice_rolls)
    
    print_2d_array(array)
    
    print_distinct_sums(array)
