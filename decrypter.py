# Shift Value Validation

def shift_validation():
    while True:
        try:
            shift = int(input("Enter the Shift Value (1-25): "))
            if shift < 1 or shift > 25:
                print("Shift Value must be between 1 and 25\n")
            else:
                return shift
        except ValueError:
            print("Enter a Valid Integer")
            continue


def decrypt(ciphertext,shift):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
                if char.isupper():
                    plaintext += chr((ord(char)-ord('A') - shift) % 26 + ord('A'))
                elif char.islower():
                    plaintext += chr((ord(char) - ord('a') - shift) % 26 + ord('a'))
                else:
                    plaintext += char
        else:
            plaintext +=char
    return plaintext



if __name__ == "__main__":
    file_location = input("Enter the File Location: ")
    shift = shift_validation()
    with open(file_location,'r') as file:
        file_data = file.read()
    plaintext = decrypt(file_data,shift)
    with open(file_location,'w') as f_write:
        f_write.write(plaintext)
    
    