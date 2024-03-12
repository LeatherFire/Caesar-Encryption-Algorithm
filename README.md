# Encryption and Decryption Tool

This Python script provides functionality for encrypting and decrypting text using various methods. It supports both single-key and multi-key encryption techniques, along with brute-force decryption option.

## Features

- **Single-Key Encryption**: Encrypt text using a single key (shift value).
- **Multi-Key Encryption**: Encrypt text using multiple keys (shift values).
- **Decryption**: Decrypt encrypted text using the appropriate key(s).
- **Brute-Force Decryption**: Attempt to decrypt encrypted text using brute-force method, trying all possible keys.

## Usage

1. **Encryption**: To encrypt text, follow these steps:
   - Choose the encryption option from the menu.
   - Select either single-key or multi-key encryption.
   - Enter the text to be encrypted and the key(s) when prompted.
   - Encrypted text will be displayed.

2. **Decryption**: To decrypt text, follow these steps:
   - Choose the decryption option from the menu.
   - Select either single-key or multi-key decryption.
   - Enter the encrypted text and the corresponding key(s) when prompted.
   - Decrypted text will be displayed.

3. **Brute-Force Decryption**: To decrypt text using brute-force method, follow these steps:
   - Choose the brute-force decryption option from the menu.
   - Enter the encrypted text to be decrypted.
   - The script will attempt to decrypt the text using all possible keys and display the decrypted results.

## Language and Text

- The script is designed to work with English text only. Other languages are not supported.

## Technical Details

- **Alphabet Mapping**: Each letter of the English alphabet is mapped to a numeric value, with 'A' being 1, 'B' being 2, and so on, up to 'Z' being 26.
- **Encryption Algorithm**: For encryption, the script utilizes a shift cipher algorithm, where each letter is shifted by a certain number of positions according to the key provided.
- **Decryption Algorithm**: Decryption is performed by reversing the encryption process, shifting each letter back by the corresponding key value.
- **Brute-Force Decryption**: Brute-force decryption involves trying all possible key values to decrypt the text. It iterates through each key value and attempts decryption until the original text is recovered or all keys are exhausted.

## Developer Information

- This Python script is developed and maintained by LeatherFire.
- For inquiries, bug reports, or contributions, please contact sadacan1907@gmail.com.

## License

This project is licensed under the MIT license. See the [LICENSE](LICENSE) file for details.
