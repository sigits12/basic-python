punctuation_marks = [".", "?", "!", ":", ";", "-", "—", "(", ")", "[", "]", "...", "’", "“ ”", "/", ",", " "]


def remove_marks(text):
    for i in punctuation_marks:
        text = text.replace(i, '')
    return text.lower()


def reverse(text):
    text = remove_marks(text)
    return text[::-1]


def is_palindrome(text):
    text1 = remove_marks(text)
    return text1 == reverse(text)


something = input("Enter text: ")
if is_palindrome(something):
    print("Yes. it is a palindrome")
else:
    print("No, it is not a palindrome")
