title = input("Enter a title :")
if len(title) > 100:
    print("The title is too long (", len(title), " characters )")
else:
    print("Title length is: ", len(title))
