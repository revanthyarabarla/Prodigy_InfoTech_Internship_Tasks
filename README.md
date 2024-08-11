# Prodigy_InfoTech_Internship_Tasks

Task 1:
Encrypt and Decrypt Text using the Caesar Cipher Algorithm
This Python script demonstrates a simple implementation of the Caesar Cipher, an ancient encryption technique. The script includes functions to both encrypt and decrypt text using a specified shift value.

How It Works
Encryption Function (encrypt):

Takes a text string and a shift value as inputs.
Iterates through each character in the text.
For alphabetic characters, it shifts their ASCII value by the specified shift, wrapping around the alphabet if necessary.
Non-alphabetic characters remain unchanged.
Returns the encrypted text.
Decryption Function (decrypt):

Utilizes the encrypt function with a negative shift to reverse the encryption.
Returns the decrypted text.
Main Function (main):

Prompts the user to input the text to be encrypted and the shift value.
Encrypts the input text using the specified shift value.
Decrypts the encrypted text to verify the process.
Prints the encrypted and decrypted texts.
Prerequisites
Basic understanding of Python programming.
Python installed on your system (Python 3.6+ is recommended).

===========================================================================

Task 2: Explanation

How It Works:-

*Encryption Function (encrypt_image):

1. Load Image: The function opens the image using PIL.Image.open.
2. Iterate through Pixels: It iterates through each pixel in the image.
3. Swap RGB Values: For each pixel, the RGB values are swapped (R becomes B, G becomes R, B becomes G).
4. Save Encrypted Image: The modified image is saved with _encrypted appended to the original file name.

*Decryption Function (decrypt_image):

1. Load Image: The function opens the encrypted image using PIL.Image.open.
2. Iterate through Pixels: It iterates through each pixel in the image.
3. Swap RGB Values: The RGB values are swapped back to their original positions (B becomes R, R becomes G, G becomes B).
4. Save Decrypted Image: The modified image is saved with _decrypted appended to the original file name.

*Main Function (main):

1. User Prompt: The user is prompted to choose between encryption and decryption.
2. Encrypt/Decrypt: Based on the user's choice, the respective function is called.
3. Repeat or Exit: The user can choose to continue with another image or exit.

How to Use:-

1. Ensure Prerequisites: Make sure you have Python and Pillow installed.
2. Run the Script: Execute the script in your Python environment.
3. Follow Prompts: Input the required information when prompted:
	- Choose to encrypt or decrypt.
	- Provide the image path.
	- The script will output the path to the encrypted/decrypted image.
4. Repeat or Exit: You can choose to process another image or exit the script.

===========================================================================

Task 3:
### Explanation

#### How It Works

**Password Strength Evaluation Function (`evaluate_password_strength`)**:
1. **Define Criteria for Password Strength**:
    - **Minimum Length**: At least 8 characters.
    - **Uppercase Letter**: At least one uppercase letter.
    - **Lowercase Letter**: At least one lowercase letter.
    - **Digit**: At least one digit.
    - **Special Character**: At least one special character from the set `!@#$%^&*(),.?":{}|<>`.

2. **Assess Password Strength**:
    - **Strong Password**: Meets all criteria, returns "Strong password! 👍".
    - **Weak Password**: Fails any criteria, returns feedback for improvement.

**Main Function (`main`)**:
1. **User Prompt**: Prompts the user to enter a password.
2. **Evaluate Password**: Uses 'evaluate_password_strength' to evaluate the input password.
3. **Print Results**: Prints whether the password is strong or provides feedback for improvement.

### How to Use

1. **Ensure Prerequisites**: Ensure Python is installed.
2. **Run the Script**: Execute the script in your Python environment.
3. **Follow Prompts**: Enter your password when prompted.
4. **Receive Feedback**: The script evaluates your password and provides feedback on its strength.

===========================================================================

Task 4:
### Explanation

#### How It Works

**Keystroke Capture Function (`on_press`)**:
1. **Logging Keystrokes**:
   - **Character Logging**: Captures each character typed by the user and adds it to a sentence string.
   - **Special Key Handling**: Handles special keys such as space and enter by converting them into spaces and newlines, respectively.
   - **Real-Time Logging**: Logs each captured character or special key action to the `keylog.txt` file.

2. **Key Release Handling (`on_release`)**:
   - **Exit Condition**: Monitors for the escape key (`esc`) press, which stops the keylogger and exits the script.

**Main Functionality**:
1. **Start Listening**: The keylogger starts listening for keyboard events and runs continuously.
2. **Sentence Construction**: As the user types, the current sentence is displayed in real-time in the console.

### How to Use

1. **Ensure Prerequisites**: Ensure Python is installed, and the `pynput` library is available.
2. **Run the Script**: Execute the script in your Python environment.
3. **Start Typing**: The script will automatically log every keystroke to the `keylog.txt` file.
4. **Exit the Script**: Press the escape key (`esc`) to stop the keylogger and exit the script.

===========================================================================

