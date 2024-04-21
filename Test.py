import tkinter as tk
import sqlite3

# Database connection and table creation
conn = sqlite3.connect('flashcards.db')
c = conn.cursor()

c.execute('''CREATE TABLE IF NOT EXISTS flashcards
             (id INTEGER PRIMARY KEY, question TEXT, answer TEXT)''')

conn.commit()
conn.close()

root = tk.Tk()
root.title("Flashcard App")
root.geometry("500x400")

main_frame = tk.Frame(root, bg="lightblue", padx=20, pady=20)
main_frame.pack(fill=tk.BOTH, expand=True)

question_label = tk.Label(main_frame, text="Question:", font=("Arial", 16, "bold"), bg="lightblue")
question_label.pack(pady=10)

question_text_label = tk.Label(main_frame, text="", font=("Arial", 14), wraplength=400, bg="lightblue")
question_text_label.pack()

show_answer = tk.Button(main_frame, text="Show Answer", font=("Arial", 12), bg="lightgreen", activebackground="green")
show_answer.pack(pady=15)

next_button = tk.Button(main_frame, text="Next Card", font=("Arial", 12), bg="lightyellow", activebackground="yellow")
next_button.pack(pady=5)

answer_label = tk.Label(main_frame, text="", font=("Arial", 14), fg="gray", bg="lightblue")
answer_label.pack()

current_card_index = 0
num_cards = 0
def add_flashcard():
    question = new_question_entry.get()
    answer = new_answer_entry.get()

    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    c.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

    # Update the GUI to show the entered question and answer near the Next Card button
    new_question_label.config(text="New Question: " + question)
    new_answer_label.config(text="New Answer: " + answer)

    flashcards = fetch_flashcards()
    num_cards = len(flashcards)
    current_card_index = 0
    show_next_card()


def fetch_flashcards():
    global num_cards
    flashcards = [
        {"question": "What is the capital of France?", "answer": "Paris"},
        {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"}
    ]
    num_cards = len(flashcards)
    return flashcards

def show_next_card():
    global current_card_index, flashcards, question_text_label, answer_label

    if num_cards == 0:
        question_text_label.config(text="No flashcards found in the database.")
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

flashcards = fetch_flashcards()
show_next_card()

show_answer.config(command=reveal_answer)
next_button.config(command=show_next_card)

def add_flashcard():
    question = new_question_entry.get()
    answer = new_answer_entry.get()

    # Update the GUI to show the entered question and answer near the Next Card button
    new_question_label.config(text="New Question: " + question)
    new_answer_label.config(text="New Answer: " + answer)

    conn = sqlite3.connect('flashcards.db')
    c = conn.cursor()
    c.execute("INSERT INTO flashcards (question, answer) VALUES (?, ?)", (question, answer))
    conn.commit()
    conn.close()

    flashcards = fetch_flashcards()
    num_cards = len(flashcards)
    current_card_index = 0
    show_next_card()

add_flashcard_frame = tk.Frame(root, bg="lightblue", padx=20, pady=10)
add_flashcard_frame.pack(fill=tk.BOTH)

new_question_label = tk.Label(add_flashcard_frame, text="New Question:", font=("Arial", 12), bg="lightblue")
new_question_label.grid(row=0, column=0)
new_question_entry = tk.Entry(add_flashcard_frame, font=("Arial", 12))
new_question_entry.grid(row=0, column=1)

new_answer_label = tk.Label(add_flashcard_frame, text="New Answer:", font=("Arial", 12), bg="lightblue")
new_answer_label.grid(row=1, column=0)
new_answer_entry = tk.Entry(add_flashcard_frame, font=("Arial", 12))
new_answer_entry.grid(row=1, column=1)

add_flashcard_button = tk.Button(add_flashcard_frame, text="Add Flashcard", font=("Arial", 12), bg="lightblue", command=add_flashcard)
add_flashcard_button.grid(row=2, columnspan=2, pady=10)

root.mainloop()
