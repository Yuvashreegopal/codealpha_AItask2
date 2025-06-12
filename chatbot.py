import tkinter as tk

# WhatsApp FAQ database
faq_data = {
    "How do I reset my WhatsApp password?":
        "Go to WhatsApp > Settings > Account > Two-step verification > Enable. Use 'Forgot PIN' if needed.",
    "How do I delete my WhatsApp account?":
        "Go to Settings > Account > Delete my account. Enter your number and follow the steps.",
    "How do I back up my chats?":
        "Go to Settings > Chats > Chat backup > Tap 'Back Up'. Choose Google Drive/iCloud if needed.",
    "How can I recover deleted messages?":
        "Restore from a recent backup during app reinstallation. Backup must have been enabled before deletion.",
    "How do I use WhatsApp on PC?":
        "Visit web.whatsapp.com > Scan the QR code using WhatsApp on your phone (Linked Devices).",
    "How can I block a contact?":
        "Open the chat > Tap on contact's name > Scroll down and select 'Block Contact'.",
    "How do I mute a group chat?":
        "Open group chat > Tap group name > Tap Mute notifications > Choose duration.",
    "Why am I banned from WhatsApp?":
        "You may have violated WhatsApp’s terms. Contact support via the app if you believe it was a mistake.",
    "How do I change my profile picture?":
        "Go to Settings > Tap your profile photo > Tap camera icon to update.",
    "How can I hide my last seen status?":
        "Go to Settings > Privacy > Last Seen & Online > Set to 'Nobody' or customize."
}

# GUI setup
root = tk.Tk()
root.title("📱 WhatsApp FAQ Chatbot")
root.geometry("620x480")
root.config(bg="#d9fdd3")  # Light green background

# Title label
title_label = tk.Label(
    root, text="📱 WhatsApp FAQ Chatbot", font=("Segoe UI", 18, "bold"),
    bg="#d9fdd3", fg="#1b5e20"
)
title_label.pack(pady=15)

# Dropdown menu
question_var = tk.StringVar(root)
question_var.set("Select a question")

def show_dropdown_answer(*args):
    selected = question_var.get()
    if selected in faq_data:
        response_label.config(text="Bot: " + faq_data[selected])
    else:
        response_label.config(text="")

dropdown = tk.OptionMenu(root, question_var, *faq_data.keys())
dropdown.config(width=60, font=("Segoe UI", 11), bg="white", fg="#1b5e20", relief="groove")
dropdown.pack(pady=10)
question_var.trace("w", show_dropdown_answer)

# Response display area in LabelFrame
response_frame = tk.LabelFrame(root, text="Bot's Response", font=("Segoe UI", 12, "bold"), bg="#d9fdd3", fg="#1b5e20", padx=10, pady=10)
response_frame.pack(pady=10)

response_label = tk.Label(
    response_frame, text="", wraplength=550, justify="left",
    font=("Segoe UI", 12), fg="#1b5e20", bg="#d9fdd3"
)
response_label.pack()

# Manual input
entry_label = tk.Label(root, text="Or ask your own question below:", font=("Segoe UI", 12), bg="#d9fdd3", fg="#1b5e20")
entry_label.pack(pady=5)

manual_entry = tk.Entry(root, font=("Segoe UI", 12), width=60, bd=2, relief="groove", fg="#1b5e20")
manual_entry.pack(pady=5)

# Ask button
def answer_manual_question():
    user_question = manual_entry.get().strip().lower()
    found = False
    for q, a in faq_data.items():
        if user_question in q.lower():
            response_label.config(text="Bot: " + a)
            found = True
            break
    if not found:
        response_label.config(text="Bot: Sorry, I don't have an answer for that.")

ask_btn = tk.Button(
    root, text="Ask", command=answer_manual_question,
    font=("Segoe UI", 12, "bold"), bg="#34af23", fg="white",
    activebackground="#2e7d32", relief="raised", padx=15, pady=5
)
ask_btn.pack(pady=15)

root.mainloop()
