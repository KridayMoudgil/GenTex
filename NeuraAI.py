from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
import customtkinter
import tkinter as tk
import pyttsx3

root = customtkinter.CTk()
root.geometry("900x600")
root.resizable(False, False)
root.title("Neura.AI")

customtkinter.set_appearance_mode("Dark")
customtkinter.set_default_color_theme("blue")

engine = pyttsx3.init()

template = """
Answer the question below.
Here is the conversation history: {context}
Question : {question}
Answer : """

model = OllamaLLM(model="llama3.2")
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    user_input = entry_1.get()
    response_label.configure(state="normal")
    response_label.insert(tk.END, "Generating...\n\n")
    response_label.yview(tk.END)
    root.update()
    if user_input.lower() == "who is kriday moudgil?":
        response_label.configure(state="normal")
        response_label.insert(tk.END, f"Neura: \n\n Kriday Moudgil is an Indo-American multi-billionaire,"
                                      "philantrophist and the CEO of Microsoft AI. \n\n")
        response_label.configure(state="disabled")
        response_label.yview(tk.END)
    else:

        result = chain.invoke({"context": context, "question": user_input})
        response = str(result)
        response_label.configure(state="normal")
        response_label.insert(tk.END, f"Neura: \n\n{response}\n\n")
        response_label.configure(state="disabled")
        response_label.yview(tk.END)
        context += f"\nUser: {user_input}\nAI: {result}"


def say_response():
    context = ""
    user_input = entry_1.get()
    result = chain.invoke({"context": context, "question": user_input})
    response = str(result)
    engine.say(response)
    engine.runAndWait()


label_1 = customtkinter.CTkLabel(root, text="Neura AI", font=("Roboto", 40, "bold"))
label_1.pack(padx=5, pady=10)

entry_1 = customtkinter.CTkEntry(root, placeholder_text="Prompt: ", height=45, width=800)
entry_1.pack(padx=50, pady=10)

button_1 = customtkinter.CTkButton(root, text="Generate Response", height=30, width=155, command=handle_conversation)
button_1.pack(padx=60, pady=10)

button_2 = customtkinter.CTkButton(root, text="Say Response", height=30, width=155, command=say_response)
button_2.pack(padx=70, pady=10)

# Scrollable frame for responses
frame = customtkinter.CTkFrame(root, bg_color="#000")
frame.pack(padx=20, pady=10, fill=tk.BOTH, expand=True)

scrollbar = customtkinter.CTkScrollbar(frame)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

response_label = customtkinter.CTkTextbox(frame, wrap=tk.WORD, height=20, font=("Helvetica", 15), state="normal",
                                          yscrollcommand=scrollbar.set)
response_label.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar.configure(command=response_label.yview)





root.mainloop()
