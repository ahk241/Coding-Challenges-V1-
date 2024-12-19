import tkinter as tk
import string
import secrets

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("New Password Generator")
        self.root.geometry("400x300")
        self.root.config(bg="#333")  
        
        
        self.title_label = tk.Label(root, text="New Password Generator", font=("Arial", 16), fg="white", bg="#333")
        self.title_label.pack(pady=15)
        
        # Password length slider for GUI 
        self.length_label = tk.Label(root, text="New Password Length:", font=("Arial", 12), fg="white", bg="#333")
        self.length_label.pack()

        self.length_slider = tk.Scale(root, from_=8, to_=32, orient="horizontal", font=("Arial", 12), bg="#333", fg="white")
        self.length_slider.set(12)
        self.length_slider.pack(pady=10)
        
     # code to show the password
        self.password_display = tk.Entry(root, font=("Arial", 14), width=30, fg="black", bg="white", bd=0, justify="center")
        self.password_display.pack(pady=15)
        
        # the button to generate the password
        self.generate_button = tk.Button(root, text="Generate Password", font=("Arial", 12), bg="#4CAF50", fg="white", command=self.generate_password)
        self.generate_button.pack(pady=10)
        
        # the button to copy the password
        self.copy_button = tk.Button(root, text="Copy", font=("Arial", 12), bg="#2196F3", fg="white", command=self.copy_password)
        self.copy_button.pack(pady=5)

    def generate_password(self):
        # reading the slider input
        length = self.length_slider.get()
        
         
        characters = string.ascii_letters + string.digits + string.punctuation
        
        # Generate a random password
        password = ''.join(secrets.choice(characters) for _ in range(length))
        
        # Show the generated password
        self.password_display.delete(0, tk.END)
        self.password_display.insert(tk.END, password)

    def copy_password(self):
    
        self.root.clipboard_clear()
        self.root.clipboard_append(self.password_display.get())
        self.root.update()

# Running the app on tinker
def main():
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()

if __name__ == "__main__":
    main()
