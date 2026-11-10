certainty_factor_patient_has_cancer = 0.9
false_positive_rate = 0.20

result = certainty_factor_patient_has_cancer * (1 - false_positive_rate)

print("Cancer Diagnosis Analysis")
print("-------------------------")
print("Doctor's Certainty:", certainty_factor_patient_has_cancer)
print("False Positive Rate:", false_positive_rate)
print("Final Certainty:", result)
print("Percentage:", result * 100, "%")
