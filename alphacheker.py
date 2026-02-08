def is_alphabet_only(text):
    return text.isalpha()

# Test
user_input = input("Enter text: ")
if is_alphabet_only(user_input):
    print("✅ Only alphabets!")
else:
    print("❌ Contains non-alphabet characters.")