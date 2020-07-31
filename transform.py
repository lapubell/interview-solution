# Translate these names from the string on the left to the string on the right
# of the ->

# mr jim jones       -> Mr. Jim Jones
# James smith        -> James Smith
# Ms Sally Smith     -> Ms. Sally Smith
# MRS. KRISTIN BROWN -> Ms. Kristin Brown
# Mister Tom Jones   -> Mr. Tom Jones
# doctor jane doe    -> Dr. Jane Doe
# Tom Marvelo Riddle -> Tom Marvelo Riddle

def formatName(name):
    parts = name.split()
    parts[0] = checkPrefix(parts[0]) # <- formatting for prefix
    return " ".join(parts).title()

def checkPrefix(word):
    word = word.lower().replace('.', '') # <- data sanitation
    maleTransforms = ['mister', 'mr']
    femaleTransforms = ['miss', 'mrs', 'ms']
    professionalTransforms = ['doctor']
    if any(word in s for s in maleTransforms):
        return 'Mr.'
    if any(word in s for s in femaleTransforms):
        return 'Ms.'
    if any(word in s for s in professionalTransforms):
        return 'Dr.'
    return word

if __name__ == '__main__':
    print(formatName("mr jim jones"))
    print(formatName("James smith"))
    print(formatName("Ms Sally Smith"))
    print(formatName("MRS. KRISTIN BROWN"))
    print(formatName("Mister Tom Jones"))
    print(formatName("doctor jane doe"))
    print(formatName("Tom Marvelo Riddle"))
