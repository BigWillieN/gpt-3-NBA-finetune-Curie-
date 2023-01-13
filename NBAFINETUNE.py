import openai
import tkinter as tk

# Set your OpenAI API key
openai.api_key = "your key here"

# Create the GUI window
root = tk.Tk()
root.title("ChatGPT NBA FineTune GUI")

# Create the input prompt field
prompt_label = tk.Label(root, text="Enter your prompt:")
prompt_label.pack()
prompt_field = tk.Entry(root)
prompt_field.pack()

# Create the result display area
result_label = tk.Label(root, text="Result:")
result_label.pack()
result_text = tk.Text(root)
result_text.pack()

# Define the function to handle the "Enter" button press
def on_enter():
    # Get the prompt text from the input field
    prompt = prompt_field.get()
    
    # Use the OpenAI API to generate a completion for the prompt
    response = openai.Completion.create(
        model="curie:ft-politecnico-di-torino-2023-01-13-19-04-16",
        prompt=prompt
    )
    
    # Get the generated text from the API response
    generated_text = response["choices"][0]["text"]
    
    # Insert the generated text into the result display area
    result_text.insert("1.0", generated_text)

# Create the "Enter" button
enter_button = tk.Button(root, text="Enter", command=on_enter)
enter_button.pack()

# Run the GUI
root.mainloop()
