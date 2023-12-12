possible_outcomes = [1, 2, 3, 4, 5, 6]

even_outcomes = [outcome for outcome in possible_outcomes if outcome % 2 == 0]
odd_outcomes = [outcome for outcome in possible_outcomes if outcome % 2 != 0]

print("Possible Outcomes:", possible_outcomes)

for outcome in possible_outcomes:
    probability = possible_outcomes.count(outcome) / len(possible_outcomes)
    print(f"Probability of {outcome}: {probability:.2f}")

print("Probability of Even Outcomes:", len(even_outcomes) / len(possible_outcomes))
print("Probability of Odd Outcomes:", len(odd_outcomes) / len(possible_outcomes))
