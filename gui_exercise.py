import tkinter as tk

def local_llm_query(user_input):
    # Mock LLM response for illustration
    return f"Response to '{user_input}' from Local LLM."

def query_llm():
    user_input = input_text.get("1.0", "end-1c")
    response = local_llm_query(user_input)  # Assuming local_llm_query is a function that queries your Local LLM
    output_text.delete("1.0", tk.END)
    output_text.insert(tk.END, response)

# Setting up the Tkinter window
window = tk.Tk()
window.title("OSINT Query Interface")

input_text = tk.Text(window, height=5, width=50)
input_text.pack()

query_button = tk.Button(window, text="Query", command=query_llm)
query_button.pack()

output_text = tk.Text(window, height=10, width=50)
output_text.pack()

window.mainloop()
