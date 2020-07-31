from additive_string import isAdditiveNumber

expectations = {
    "235813": True,
    "199100199": True,
    "12345678": False
}

for i, o in expectations.items():
    if isAdditiveNumber(i) != o:
        print ("problem parsing", i, "\n\nExpected:", o, "\n  Actual:", isAdditiveNumber(i))
    else:
        print ("PASS")
