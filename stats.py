
def word_counter(text):
    words = text.split()
    return len(words)

def characters_counter(text):
    char_count={}

    for char in text:
        if not char.isalpha():  # skip non-alphabetical characters
            continue
        if char.lower() in char_count:
            char_count[char.lower()]+=1
        else:
            char_count[char.lower()] = 1
    return char_count

def sort_on(item):
    
    return item[1]

def sorted_report(char_count):
    listed = list(char_count.items())
    listed.sort(key=sort_on, reverse=True)
    return listed

    

 

