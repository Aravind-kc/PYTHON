def count_words(text):
    tmp=text.count(" ")
    return tmp+1
def count_char(text):
    tmp=text.count("")
    return tmp-1
def reverse_char(text):
    return text[::-1]
def capitalize_words(text):
    return text.capitalize()