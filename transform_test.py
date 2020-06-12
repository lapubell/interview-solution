from transform import formatName

expectations = {
    "mr jim jones": "Mr. Jim Jones",
    "James smith": "James Smith",
    "Ms Sally Smith": "Ms. Sally Smith",
    "MRS. KRISTIN BROWN": "Ms. Kristin Brown",
    "Mister Tom Jones": "Mr. Tom Jones"
}

for i, o in expectations.items():
    if formatName(i) != o:
        print ("problem parsing", i, "\n\nExpected:", o, "\n  Actual:", formatName(i))
    else:
        print ("PASS")
