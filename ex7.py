# ex7.py

# Learn Python the Hard way

formatter = "%r %r %r %r"
# why does Python allow this to be a string and a string formatter / piper
# I hate this; Haskell's implementation of strings with read/show makes more sense to me

print formatter % (1,2,3,4)
print formatter % ("one", "two", "three", "four")
print formatter % (True, False, False, True)
print formatter % (formatter, formatter, formatter, formatter)
print formatter % (
    "I had this thing.",
    "That you could type up right.",
    "But it didn't sing.",
    "So I said goodnight.")
