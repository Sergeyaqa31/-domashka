def count_words(text):
    words = text.strip().split()
    return len(words)

print(count_words("  Hello, world! This is Python.  "))  # 5