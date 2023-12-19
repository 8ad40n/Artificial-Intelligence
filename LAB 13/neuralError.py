import math

input_data = [0.05, 0.10]
target_output = [0.01, 0.99]

weights_input_hidden = [[0.15, 0.25], [0.20, 0.30]]
bias_hidden = [0.35, 0.35]

weights_hidden_output = [[0.40, 0.50], [0.45, 0.55]]
bias_output = [0.60, 0.60]

def sigmoid(x):
    return 1 / (1 + math.exp(-x))


h1_input = sum(w * x for w, x in zip(weights_input_hidden[0], input_data)) + bias_hidden[0]
h1_output = sigmoid(h1_input)

output_hidden = [h1_output, sigmoid(sum(w * x for w, x in zip(weights_input_hidden[1], input_data)) + bias_hidden[1])]
output = sigmoid(sum(w * x for w, x in zip(weights_hidden_output[0], output_hidden)) + bias_output[0]), \
         sigmoid(sum(w * x for w, x in zip(weights_hidden_output[1], output_hidden)) + bias_output[1])

error_o1 = 0.5 * (target_output[0] - output[0]) ** 2
error_o2 = 0.5 * (target_output[1] - output[1]) ** 2

total_error = error_o1 + error_o2

print("Output from node h1:", h1_output)
print("Output from nodes o1 and o2:", output)
print("Error at node o1:", error_o1)
print("Error at node o2:", error_o2)
print("Total Error:", total_error)
