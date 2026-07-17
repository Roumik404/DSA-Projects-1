import string

def clean_text(s):
    # Lowercase and remove spaces/punctuation
    return ''.join(ch.lower() for ch in s if ch.isalnum())

def is_palindrome(s):
    s = clean_text(s)
    return s == s[::-1]

def is_anagram(s1, s2):
    return sorted(clean_text(s1)) == sorted(clean_text(s2))

def almost_anagram(s1, s2):
    # Check if they differ by at most one character
    s1, s2 = clean_text(s1), clean_text(s2)
    if abs(len(s1) - len(s2)) > 1:
        return False
    # Count differences
    diffs = sum(1 for a, b in zip(sorted(s1), sorted(s2)) if a != b)
    return diffs <= 1

def batch_palindrome(words):
    for w in words:
        print(f"{w}: {'Palindrome' if is_palindrome(w) else 'Not palindrome'}")

def main():
    while True:
        print("\n--- Palindrome & Anagram Checker ---")
        print("1. Check Palindrome")
        print("2. Check Anagram")
        print("3. Check Almost Anagram")
        print("4. Batch Palindrome Check")
        print("5. Exit")
        choice = input("Choose (1-5): ")

        if choice == "1":
            s = input("Enter string: ")
            print("Palindrome!" if is_palindrome(s) else "Not a palindrome.")
        elif choice == "2":
            s1 = input("Enter first string: ")
            s2 = input("Enter second string: ")
            print("Anagram!" if is_anagram(s1, s2) else "Not an anagram.")
        elif choice == "3":
            s1 = input("Enter first string: ")
            s2 = input("Enter second string: ")
            print("Almost anagram!" if almost_anagram(s1, s2) else "Not close enough.")
        elif choice == "4":
            words = input("Enter words separated by commas: ").split(",")
            batch_palindrome([w.strip() for w in words])
        elif choice == "5":
            print("Closing checker. Bye!")
            break
        else:
            print("Invalid choice.")

if __name__ == "__main__":
    main()
