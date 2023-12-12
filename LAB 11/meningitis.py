p_meningitis = 1 / 50000
p_stiff_neck_given_meningitis = 0.7
p_stiff_neck = 0.01

p_meningitis_given_stiff_neck = (p_stiff_neck_given_meningitis * p_meningitis) / p_stiff_neck

print("Probability of meningitis given a stiff neck:", p_meningitis_given_stiff_neck)
