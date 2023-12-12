# Given probabilities
p_virus = 0.15
p_positive_given_virus = 0.95
p_positive_given_no_virus = 0.02

p_positive = p_virus * p_positive_given_virus + (1 - p_virus) * p_positive_given_no_virus

p_virus_given_positive = (p_virus * p_positive_given_virus) / p_positive

p_no_virus_given_positive = ((1 - p_virus) * p_positive_given_no_virus) / p_positive

p_negative_given_virus = 1 - p_positive_given_virus
p_negative_given_no_virus = 1 - p_positive_given_no_virus

p_virus_given_negative = (p_virus * p_negative_given_virus) / (1 - p_positive)

p_no_virus_given_negative = ((1 - p_virus) * p_negative_given_no_virus) / (1 - p_positive)

print("If the test is positive:")
print("(i) Probability that the patient has the virus:", p_virus_given_positive)
print("(ii) Probability that the patient doesn't have the virus:", p_no_virus_given_positive)
print("\nIf the test is negative:")
print("(i) Probability that the patient has the virus:", p_virus_given_negative)
print("(ii) Probability that the patient doesn't have the virus:", p_no_virus_given_negative)
