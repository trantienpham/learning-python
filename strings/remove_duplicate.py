def remove_duplicates(sentences: str) -> str:
    sen_list = sentences.split(" ")
    check = set()
    
    for a_word in sen_list:
        check.add(a_word)
    
    return " ".join(sorted(check))

if __name__ == "__main__":
    print(remove_duplicates("Python is great and Java is also great"))