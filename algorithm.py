import time
alphabet_dict = {
    'A': 1, 'B': 2, 'C': 3, 'D': 4, 'E': 5,
    'F': 6, 'G': 7, 'H': 8, 'I': 9, 'J': 10,
    'K': 11, 'L': 12, 'M': 13, 'N': 14, 'O': 15,
    'P': 16, 'Q': 17, 'R': 18, 'S': 19, 'T': 20,
    'U': 21, 'V': 22, 'W': 23, 'X': 24, 'Y': 25, 'Z': 26
}

def main():
    while True:
        print("1. Encrypt")
        print("2. Decrypt")
        print("3. Decrypt(Brute-Force)")
        print("4. Exit")
        choice = input("Choose an option: ")
        if choice == "1":
            while True:
                language = "EN"
                if language in ["EN", "E", "en", "e", "English", "english","ENGLISH","En","eN"]:
                    encrypt("EN")
                    break
            break
        elif choice == "2":
            while True:
                language = "EN"
                if language in ["EN", "E", "en", "e"]:
                    decrypt("EN")
                    break
            break
        elif choice == "3":
            while True:
                language = "EN"
                if language in ["EN", "E", "en", "e"]:
                    decrypt_brute("EN")
                    break
            break
        elif choice == "4":
            break
        else:
            print("Invalid choice. Please try again.")

def decrypt_brute(language):
    while True:
        nosecrettext = input("Enter text to decrypt with Brute-Force: ")
        if not nosecrettext:
            print("Invalid input. Please try again.")
        elif any(char.isdigit() or not char.isascii() or char in "!@#$%^&*()-_=+[]{};:'\"\\|<>,./?`~" for char in nosecrettext):
            print("Invalid input. Please enter only English letters and spaces.")
        else:
            freewords=nosecrettext.split()
            encrypted_word = ""
            for j in range(26):
                for word in freewords:
                    for letter in word:
                        for i in range((j+1)):
                            encrypted_index = (alphabet_dict[letter.upper()] - i - 1) % 26
                            if (encrypted_index==0):
                                encrypted_letter = 'Z'
                            else:
                                encrypted_letter = chr(encrypted_index + ord('A') - 1)
                            print(encrypted_letter, end='\r', flush=True)  # Her harf yazdırılır, ancak satır değiştirilmez
                            time.sleep(0.01)  # 0.5 saniyelik gecikme ekleyin
                        encrypted_word += encrypted_letter  # Her harf şifrelenmiş kelimeye eklenir
                        print(encrypted_word,end='\r', flush=True)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                    print("Decrypted: " + word, "with key: " + str(j+1) + " result ==> " + encrypted_word)
                    #print(encrypted_word)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                    #print("")
                    encrypted_word = ""  # Şifrelenmiş kelime sıfırlanır, bir sonraki kelime için hazır hale getirilir
                print("")
                #print("Decrypted: " + encrypted_word, "with key: " + str(j+1))
            print("Decrypting is done !!!")

def encrypt(language):
    while True:
        nosecrettext = input("Enter text to encrypt: ")
        if not nosecrettext:
            print("Invalid input. Please try again.")
        elif any(char.isdigit() or not char.isascii() or char in "!@#$%^&*()-_=+[]{};:'\"\\|<>,./?`~" for char in nosecrettext):
            print("Invalid input. Please enter only English letters and spaces.")
        else:
            freewords=nosecrettext.split()
            if(language=="EN"):
                print("Multi-Key (MK) or Single-Key (SK)?")
                keyoption = input("Please choose Multi-Key or Single-Key: ")
                while True:
                    if keyoption in ["MK", "mk", "Multi-Key", "multi-key"]:
                        while True:
                            keys_input = input("Enter the keys (separated by space): ")
                            if keys_input == "":
                                print("Empty input. Please try again.")
                            else:
                                keys = keys_input.split()
                                if len(keys) < 2 or not all(key.isdigit() and float(key) == int(key) and 1 <= int(key) <= 26 for key in keys):
                                    print("Invalid input. Please enter at least two valid integers between 1 and 26.")
                                else:
                                    encrypted2(keys, freewords, "en")
                                    break
                        break

                    elif keyoption in ["SK", "sk", "Single-Key", "single-key"]:
                        while True:
                            key = input("Enter the key: ")
                            if key.isdigit() and float(key) == int(key) and 1 <= int(key) <= 26 and (len(key)==1 or len(key)==2):
                                encrypted2(key, freewords, "en")
                                break
                            else:
                                print("Invalid input. Please enter a valid integer between 1 and 26.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
                        break
            else:
                print("you choose another language")

            break
    print("Encrypting...")

def decrypt(language):
    while True:
        nosecrettext = input("Enter text to decrypt: ")
        if not nosecrettext:
            print("Invalid input. Please try again.")
        elif any(char.isdigit() or not char.isascii() or char in "!@#$%^&*()-_=+[]{};:'\"\\|<>,./?`~" for char in nosecrettext):
            print("Invalid input. Please enter only English letters and spaces.")
        else:
            freewords=nosecrettext.split()
            if(language=="EN"):
                print("Multi-Key (MK) or Single-Key (SK)?")
                keyoption = input("Please choose Multi-Key or Single-Key: ")
                while True:
                    if keyoption in ["MK", "mk", "Multi-Key", "multi-key"]:
                        while True:
                            keys_input = input("Enter the keys (separated by space): ")
                            if keys_input == "":
                                print("Empty input. Please try again.")
                            else:
                                keys = keys_input.split()
                                if len(keys) < 2 or not all(key.isdigit() and float(key) == int(key) and 1 <= int(key) <= 26 for key in keys):
                                    print("Invalid input. Please enter at least two valid integers between 1 and 26.")
                                else:
                                    decrypted2(keys, freewords, "en")
                                    break
                        break

                    elif keyoption in ["SK", "sk", "Single-Key", "single-key"]:
                        while True:
                            key = input("Enter the key: ")
                            if key.isdigit() and float(key) == int(key) and 1 <= int(key) <= 26 and (len(key)==1 or len(key)==2):
                                decrypted2(key, freewords, "en")
                                break
                            else:
                                print("Invalid input. Please enter a valid integer between 1 and 26.")
                        break
                    else:
                        print("Invalid choice. Please try again.")
                        break
            else:
                print("you choose another language")

            break
    print("Decrypting...")

def encrypted2(keys, freewords, language):
    if language.upper() == "EN":
        if (type(keys) is str):
            encrypted_word = ""
            for word in freewords:
                for letter in word:
                    for i in range(int(keys)):
                        encrypted_index = (alphabet_dict[letter.upper()] + i + 1) % 26
                        if (encrypted_index==0):
                            encrypted_letter = 'Z'
                        else:
                            encrypted_letter = chr(encrypted_index + ord('A') - 1)
                        print(encrypted_letter, end='\r', flush=True)  # Her harf yazdırılır, ancak satır değiştirilmez
                        time.sleep(0.1)  # 0.5 saniyelik gecikme ekleyin
                    encrypted_word += encrypted_letter  # Her harf şifrelenmiş kelimeye eklenir
                    print(encrypted_word,end='\r', flush=True)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                print(encrypted_word)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                encrypted_word = ""  # Şifrelenmiş kelime sıfırlanır, bir sonraki kelime için hazır hale getirilir


        else:
            anc=-1
            encrypted_word = ""
            lenwords=len(freewords)
            lenkeys=len(keys)
            bnc=-1
            keylist=[]
            for i in range(lenwords):
                bnc+=1
                keylist.append((bnc%lenkeys))
            for j in keylist:
                if(len(freewords)!=anc):
                    anc+=1
                word=freewords[anc]
                for letter in word:
                    for i in range(int(keys[j])):
                        encrypted_index = (alphabet_dict[letter.upper()] + i + 1) % 26
                        if (encrypted_index==0):
                            encrypted_letter = 'Z'
                        else:
                            encrypted_letter = chr(encrypted_index + ord('A') - 1)
                        print(encrypted_letter, end='\r', flush=True)  # Her harf yazdırılır, ancak satır değiştirilmez
                        time.sleep(0.1)  # 0.5 saniyelik gecikme ekleyin
                    encrypted_word += encrypted_letter  # Her harf şifrelenmiş kelimeye eklenir
                    print(encrypted_word,end='\r', flush=True)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                print(encrypted_word)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                encrypted_word = ""  # Şifrelenmiş kelime sıfırlanır, bir sonraki kelime için hazır hale getirilir
    else:
        print("you choose another language")
    print("Encrypting...", keys, freewords)

def decrypted2(keys, freewords, language):
    if language.upper() == "EN":
        if (type(keys) is str):
            encrypted_word = ""
            for word in freewords:
                for letter in word:
                    for i in range(int(keys)):
                        encrypted_index = (alphabet_dict[letter.upper()] - i - 1) % 26
                        if (encrypted_index==0):
                            encrypted_letter = 'Z'
                        else:
                            encrypted_letter = chr(encrypted_index + ord('A') - 1)
                        print(encrypted_letter, end='\r', flush=True)  # Her harf yazdırılır, ancak satır değiştirilmez
                        time.sleep(0.1)  # 0.5 saniyelik gecikme ekleyin
                    encrypted_word += encrypted_letter  # Her harf şifrelenmiş kelimeye eklenir
                    print(encrypted_word,end='\r', flush=True)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                print(encrypted_word)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                encrypted_word = ""  # Şifrelenmiş kelime sıfırlanır, bir sonraki kelime için hazır hale getirilir


        else:
            anc=-1
            encrypted_word = ""
            lenwords=len(freewords)
            lenkeys=len(keys)
            bnc=-1
            keylist=[]
            for i in range(lenwords):
                bnc+=1
                keylist.append((bnc%lenkeys))
            for j in keylist:
                if(len(freewords)!=anc):
                    anc+=1
                word=freewords[anc]
                for letter in word:
                    for i in range(int(keys[j])):
                        encrypted_index = (alphabet_dict[letter.upper()] - i - 1) % 26
                        if (encrypted_index==0):
                            encrypted_letter = 'Z'
                        else:
                            encrypted_letter = chr(encrypted_index + ord('A') - 1)
                        print(encrypted_letter, end='\r', flush=True)  # Her harf yazdırılır, ancak satır değiştirilmez
                        time.sleep(0.1)  # 0.5 saniyelik gecikme ekleyin
                    encrypted_word += encrypted_letter  # Her harf şifrelenmiş kelimeye eklenir
                    print(encrypted_word,end='\r', flush=True)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                print(encrypted_word)  # Tüm kelime şifrelendiğinde, şifrelenmiş kelime yazdırılır
                encrypted_word = ""  # Şifrelenmiş kelime sıfırlanır, bir sonraki kelime için hazır hale getirilir
    else:
        print("you choose another language")
    print("Decrypting...", keys, freewords)


if __name__ == "__main__":
    main()
