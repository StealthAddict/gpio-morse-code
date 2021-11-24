import tkinter as tk
#from tkinter import ttk


class App(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title('MorseCode')
        self.geometry("300x80")

        self.codeInput = tk.StringVar()

        self.columnconfigure(0, weight=1)
        self.columnconfigure(1, weight=1)
        self.columnconfigure(2, weight=1)

        self.create_widgets()

    def create_widgets(self):

        padding = {'padx': 5, 'pady': 5}
        # label  TTK
        tk.Label(self, text='Input Code:').grid(column=0, row=0, **padding)

        # Code Entry TTK
        codeEntry = tk.Entry(self, textvariable=self.codeInput)
        codeEntry.grid(column=1, row=0, **padding)
        codeEntry.focus()

        # Submit Button  TTK
        submit_button = tk.Button(self, text='Submit', command=self.submit)
        submit_button.grid(column=2, row=0, **padding)

        # Output label      TTK
        self.output_label = tk.Label(self)
        self.output_label.grid(column=0, row=1, columnspan=3, **padding)

    def submit(self):
        
        MORSE_CODE_DICT = { 'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.', 'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..', 'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-','R':'.-.', 'S':'...', 'T':'-','U':'..-', 'V':'...-', 'W':'.--','X':'-..-', 'Y':'-.--', 'Z':'--..','1':'.----', '2':'..---', '3':'...--','4':'....-', '5':'.....', '6':'-....','7':'--...', '8':'---..', '9':'----.', '0':'-----', ', ':'--..--', '.':'.-.-.-', '?':'..--..', '/':'-..-.', '-':'-....-', '(':'-.--.', ')':'-.--.-', '':''}
        myCodeInput = self.codeInput.get()

        def decrypt(toDecrypt):
            toDecrypt += ' '
            decipher = ''
            citext = ''
            i = 0

            if toDecrypt[0] == ' ':
                toDecrypt[0:]

            for letter in toDecrypt:
                if letter != ' ':
                    i = 0
                    citext += letter

                else:
                    i += 1

                    if i == 2: 
                        decipher += ' '

                    else:
                        decipher += list(MORSE_CODE_DICT.keys())[list(MORSE_CODE_DICT
                .values()).index(citext)]
                        citext = ''

            return decipher

        result = decrypt(myCodeInput)
        
        self.output_label.config(text=result)


if __name__ == "__main__":
    app = App()
    app.mainloop()