def to_upper(text):
    return text.upper()

def to_lower(text):
    return text.lower()

def word_count(text):
    words = text.split()
    return len(words), len(text)

if __name__ == "__main__":
    sample = "Hello from GitHub CLI!"
    print("Uppercase:", to_upper(sample))
    print("Lowercase:", to_lower(sample))
    words, chars = word_count(sample)
    print(f"Words: {words}, Characters: {chars}")
