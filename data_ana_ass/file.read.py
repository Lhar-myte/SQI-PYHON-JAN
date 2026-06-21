# with open("reviews.txt", "r") as f:
#         lines = f.readlines()
#         print(lines)



import re

def extract_emails_and_phones(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()
    
    # Regular expressions for email and phone number extraction
    email_pattern = r'[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}'
    phone_pattern = r'\+234\s?\d{3}\s?\d{3}\s?\d{4}'
    
    emails = re.findall(email_pattern, content)
    phone_numbers = re.findall(phone_pattern, content)
    
    return emails, phone_numbers

def save_to_file(data, filename):
    with open(filename, 'w', encoding='utf-8') as file:
        for item in data:
            file.write(item + '\n')

def main():
    input_file = 'reviews.txt'
    emails, phone_numbers = extract_emails_and_phones(input_file)
    
    save_to_file(emails, 'emails.txt')
    save_to_file(phone_numbers, 'phone_numbers.txt')
    
    print("Extraction completed. Check emails.txt and phone_numbers.txt for results.")

if __name__ == "__main__":
    main()
        