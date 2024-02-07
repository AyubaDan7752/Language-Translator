import tkinter as tk
from tkinter import ttk
from googletrans import Translator, LANGUAGES

class LanguageTranslator:
    def __init__(self, root):
        self.root = root
        self.root.title("Language Translator")

        # Create and set up widgets
        self.create_widgets()

    def create_widgets(self):
        # Label
        label = ttk.Label(self.root, text="Enter Text:")
        label.grid(row=0, column=0, padx=10, pady=10, sticky="w")

        # Entry for input text
        self.input_text = ttk.Entry(self.root, width=40)
        self.input_text.grid(row=0, column=1, padx=10, pady=10, columnspan=2)

        # Label for selected language
        self.language_label = ttk.Label(self.root, text="Select Language:")
        self.language_label.grid(row=1, column=0, padx=10, pady=10, sticky="w")

        # Combobox for selecting language
        self.languages = ttk.Combobox(self.root, values=list(LANGUAGES.values()))
        self.languages.grid(row=1, column=1, padx=10, pady=10, columnspan=2)
        self.languages.set("English")  # Default language is English

        # Button to translate
        translate_button = ttk.Button(self.root, text="Translate", command=self.translate_text)
        translate_button.grid(row=2, column=0, padx=10, pady=10, columnspan=3)

        # Output text
        self.output_text = tk.Text(self.root, height=5, width=40, wrap="word")
        self.output_text.grid(row=3, column=0, padx=10, pady=10, columnspan=3)

    def translate_text(self):
        # Get input text and selected language
        text_to_translate = self.input_text.get()
        target_language = self.languages.get()

        # Print statements for debugging
        print(f"Input Text: {text_to_translate}")
        print(f"Target Language: {target_language}")

        try:
            # Perform translation
            translator = Translator()
            translation = translator.translate(text_to_translate, dest=target_language.lower())

            # Print statements for debugging
            print(f"Translated Text ({translation.dest}): {translation.text}")

            # Display translated text
            self.output_text.delete(1.0, tk.END)  # Clear previous text
            self.output_text.insert(tk.END, f"Translated Text ({translation.dest}): {translation.text}")

        except Exception as e:
            # Print statements for debugging in case of an exception
            print(f"Error during translation: {e}")

if __name__ == "__main__":
    root = tk.Tk()
    app = LanguageTranslator(root)
    root.mainloop()



