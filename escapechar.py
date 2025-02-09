# Split strings over several lines using \n
# ------------------------------------------------------

splitString = "This string has been\nsplit over\nseveral\nlines"

print(splitString)

# result
# ------------------------------------------------------

# This string has been
# split over
# several
# lines

# Tabbed strings over several lines using \t
# ------------------------------------------------------

tabbedString = "1\t2\t3\t4\t5"

print (tabbedString)

# result
# ------------------------------------------------------

# 1       2       3       4       5

# Escape with double and single quotes
# ------------------------------------------------------

print ('The pet shop owner said "No, no, \'e\'s uh,...he\'s resting".')

# result
# ------------------------------------------------------
# The pet shop owner said "No, no, 'e's uh,...he's resting".

#  or 

print ("The pet shop owner said 'No, no \'e\'s uh, ...he\'s resting'.")

# result
# ------------------------------------------------------
# The pet shop owner said 'No, no 'e's uh, ...he's resting'.


# Escape with tripple quotes
# ------------------------------------------------------

print ("""The pet shop owner said "No, no, 'e,'s uh, ...he's resting". """)

# result
# ------------------------------------------------------
# The pet shop owner said "No, no, 'e,'s uh, ...he's resting". 

# Escape with tripple quotes. they can split strings over several lines
# ------------------------------------------------------

anotherSplitString = """This string has been
split over
several
lines"""

print (anotherSplitString)

# result
# ------------------------------------------------------
# This string has been
# split over
# several
# lines


# Escape with tripple quotes. they can split strings over several lines using breaks. Takes away the line breaks
# ------------------------------------------------------

anotherSplitString2 = """This string has been \
split over \
several \
lines"""

print (anotherSplitString2)

# result
# ------------------------------------------------------
# This string has been split over several lines


# Quiz
# ------------------------------------------------------

print ("Number 1\tThe Larch")
print ("Number 2\tThe Horse Chestnut")
