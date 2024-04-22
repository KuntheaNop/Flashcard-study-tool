import tkinter as tk
import sqlite3

def fetch_flashcards():
    global num_cards
    conn = sqlite3.connect("flashcards.db")
    c = conn.cursor()
    c.execute("SELECT * FROM flashcards")
    flashcards = c.fetchall()
    num_cards = len(flashcards)
    conn.close()
    return flashcards

def show_next_card():
    global current_card_index, flashcards, question_text_label, answer_label

    if num_cards == 0:
        question_text_label.config(text="No flashcards found.")
        show_answer.config(state=tk.DISABLED)
        next_button.config(state=tk.DISABLED)
        return

    answer_label.config(text="", fg="gray")

    if current_card_index == num_cards - 1:
        current_card_index = 0
    else:
        current_card_index += 1

    question_text_label.config(text=flashcards[current_card_index]["question"])
    show_answer.config(state=tk.NORMAL)
    next_button.config(state=tk.NORMAL)

def reveal_answer():
    answer_label.config(text="Answer: " + flashcards[current_card_index]["answer"], fg="black")

def add_flashcard():
    question = new_question_entry.get()
    answer = new_answer_entry.get()
    if question and answer:
        flashcards.append({"question": question, "answer": answer})
        new_question_entry.delete(0, tk.END)
        new_answer_entry.delete(0, tk.END)
        global num_cards
        num_cards += 1

        if num_cards == 1:
            show_next_card()  # Display the first flashcard when added

def save_user_info():
    global user_name, user_major
    user_name = name_entry.get()
    user_major = major_entry.get()
    name_entry.delete(0, tk.END)
    major_entry.delete(0, tk.END)
    user_info_label.config(text=f"Name: {user_name}\nMajor: {user_major}")

root = tk.Tk()
root.title("Flashcard App")
root.geometry("500x500")

main_frame = tk.Frame(root, bg="lightblue", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

# User Information Section
user_info_frame = tk.Frame(main_frame, bg="lightblue")
user_info_frame.pack(pady=10)

name_label = tk.Label(user_info_frame, text="Name:", font=("Arial", 12, "bold"), bg="lightblue")
name_label.grid(row=0, column=0, padx=5, pady=5)

name_entry = tk.Entry(user_info_frame, font=("Arial", 12))
name_entry.grid(row=0, column=1, padx=5, pady=5)

major_label = tk.Label(user_info_frame, text="Major:", font=("Arial", 12, "bold"), bg="lightblue")
major_label.grid(row=1, column=0, padx=5, pady=5)

major_entry = tk.Entry(user_info_frame, font=("Arial", 12))
major_entry.grid(row=1, column=1, padx=5, pady=5)

save_info_button = tk.Button(user_info_frame, text="Save Info", font=("Arial", 12), bg="lightblue", command=save_user_info)
save_info_button.grid(row=2, columnspan=2, pady=10)

user_info_label = tk.Label(user_info_frame, text="", font=("Arial", 12), bg="lightblue")
user_info_label.grid(row=3, columnspan=2, pady=5)

# Flashcard Display Section
flashcard_display_frame = tk.Frame(main_frame, bg="lightblue")
flashcard_display_frame.pack(pady=10)

question_label = tk.Label(flashcard_display_frame, text="Question:", font=("Arial", 16, "bold"), bg="lightblue")
question_label.pack()

question_text_label = tk.Label(flashcard_display_frame, text="", font=("Arial", 14), wraplength=400, bg="lightblue")
question_text_label.pack()

answer_label = tk.Label(flashcard_display_frame, text="", font=("Arial", 14), fg="gray", bg="lightblue")
answer_label.pack()

# Flashcard Controls Section
flashcard_controls_frame = tk.Frame(main_frame, bg="lightblue")
flashcard_controls_frame.pack(pady=10)

show_answer = tk.Button(flashcard_controls_frame, text="Show Answer", font=("Arial", 12), bg="lightgreen", activebackground="green", command=reveal_answer)
show_answer.pack(side=tk.LEFT, padx=10)

next_button = tk.Button(flashcard_controls_frame, text="Next Card", font=("Arial", 12), bg="lightyellow", activebackground="yellow", command=show_next_card)
next_button.pack(side=tk.LEFT, padx=10)

# Add New Flashcard Section
add_flashcard_frame = tk.Frame(main_frame, bg="lightblue")
add_flashcard_frame.pack(pady=10)

new_question_label = tk.Label(add_flashcard_frame, text="New Question:", font=("Arial", 12), bg="lightblue")
new_question_label.grid(row=0, column=0, padx=5, pady=5)

new_question_entry = tk.Entry(add_flashcard_frame, font=("Arial", 12))
new_question_entry.grid(row=0, column=1, padx=5, pady=5)

new_answer_label = tk.Label(add_flashcard_frame, text="New Answer:", font=("Arial", 12), bg="lightblue")
new_answer_label.grid(row=1, column=0, padx=5, pady=5)

new_answer_entry = tk.Entry(add_flashcard_frame, font=("Arial", 12))
new_answer_entry.grid(row=1, column=1, padx=5, pady=5)

add_flashcard_button = tk.Button(add_flashcard_frame, text="Add Flashcard", font=("Arial", 12), bg="lightblue", activebackground="blue", command=add_flashcard)
add_flashcard_button.grid(row=2, columnspan=2, pady=10)

# Provided Questions and Answers
provided_flashcards = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "Who created Python?", "answer": "Guido van Rossum"},
    {"question": "what is 100*2", "answer": "200"},
    {"question": "When python was created?", "answer": "1991"}
]

flashcards = provided_flashcards
num_cards = len(flashcards)
current_card_index = 0
question_text_label.config(text=flashcards[current_card_index]["question"])

root.mainloop()
