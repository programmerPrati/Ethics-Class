import tkinter as tk
import random

def caesar_cipher(text, shifts):
    result = ""
    for i, char in enumerate(text):
        shift = shifts[i]
        if char.isalpha():
            shift_base = ord('A') if char.isupper() else ord('a')
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        elif char.isspace():
            result += " "  # Keep spaces unchanged
        else:
            result += char
    return result

def generate_shifts(length):
    random.seed(42)  # Fixed seed for consistency
    return [random.randint(-26, 26) for _ in range(length)]

def encrypt_text():
    input_text = text_input.get()
    shifts = generate_shifts(len(input_text))
    encrypted_text = caesar_cipher(input_text, shifts)
    output_label.config(text=f"Encrypted: {encrypted_text}")

def decrypt_text():
    input_text = text_input.get()
    shifts = generate_shifts(len(input_text))
    reversed_shifts = [-s for s in shifts]
    decrypted_text = caesar_cipher(input_text, reversed_shifts)
    output_label.config(text=f"Decrypted: {decrypted_text}")

def on_click(event):
    if event.widget != text_input:
        root.focus_set()  # Deselect text box when clicking outside

# UI Setup
root = tk.Tk()
root.title("Caesar Cipher UI")
root.geometry("400x200")

tk.Label(root, text="Enter Text:").pack()
text_input = tk.Entry(root, width=40)
text_input.pack()

tk.Button(root, text="Encrypt", command=encrypt_text).pack()
tk.Button(root, text="Decrypt", command=decrypt_text).pack()

output_label = tk.Label(root, text="", fg="blue")
output_label.pack()

root.bind("<Button-1>", on_click)  # Bind click event to deselect text box

root.mainloop()
