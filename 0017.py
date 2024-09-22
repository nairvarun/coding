one_to_nine = 36
eleven_to_nineteen = 67
ten = 3
twenty = 6
thirty = 6
forty = 5
fifty = 5
sixty = 5
seventy = 7
eighty = 6
ninety = 6
hundred = 7
onethousand = 11
and_ = 3

one_to_ninetynine = 9*one_to_nine + ten + eleven_to_nineteen + 10*(twenty + thirty + forty + fifty + sixty + seventy + eighty + ninety)

one_to_thousand = (10 * one_to_ninetynine) + (100 * one_to_nine) + (900 * hundred) + (9 * 99 * and_) + onethousand
print(one_to_thousand)
