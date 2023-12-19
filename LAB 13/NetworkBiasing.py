# Given probabilities
P_S = 0.3
P_D = 0.4
P_H_given_S_and_D = 0.8
P_H_given_not_S_and_D = 0.5
P_H_given_S_and_not_D = 0.4
P_H_given_not_S_and_not_D = 0.1
P_B_given_H = 0.7
P_B_given_not_H = 0.1
P_E_given_H = 0.8
P_E_given_not_H = 0.1

# Calculate probabilities using Bayes' theorem and given probabilities
P_H = P_S * P_D * P_H_given_S_and_D + (1 - P_S) * P_D * P_H_given_not_S_and_D + P_S * (1 - P_D) * P_H_given_S_and_not_D + (1 - P_S) * (1 - P_D) * P_H_given_not_S_and_not_D
P_not_H = 1 - P_H

P_B = P_H * P_B_given_H + P_not_H * P_B_given_not_H

P_E = P_H * P_E_given_H + P_not_H * P_E_given_not_H

# Output the calculated probabilities
print("Probability of heart disease, P(H):", P_H)
print("Probability of not heart disease, P(not(H)):", P_not_H)
print("Probability of blood pressure, P(B):", P_B)
print("Probability of abnormal electrocardiogram, P(E):", P_E)
