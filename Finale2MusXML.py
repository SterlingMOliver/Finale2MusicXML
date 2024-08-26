import os
import tkinter as tk
from tkinter import filedialog, messagebox

def generate_finale_script(source_folder, output_script_path):
    files = [f for f in os.listdir(source_folder) if f.endswith(('.mus', '.musx'))]
    with open(output_script_path, 'w') as f:
        for file in files:
            f.write(f'open "{os.path.join(source_folder, file)}"\n')
            f.write('export as MusicXML\n')
            f.write('close\n\n')
    return output_script_path

def select_folder(title):
    return filedialog.askdirectory(title=title)

def select_save_file(title, filetypes, initialfile):
    return filedialog.asksaveasfilename(title=title, defaultextension=".fsc", filetypes=filetypes, initialfile=initialfile)

def run_script():
    source_folder = select_folder("Select the folder containing Finale files")
    if not source_folder:
        return

    output_script_path = select_save_file(
        "Save the FinaleScript file",
        [("FinaleScript files", "*.fsc")],
        initialfile="FinaleBatchExport.fsc"
    )
    if not output_script_path:
        return

    script_path = generate_finale_script(source_folder, output_script_path)
    messagebox.showinfo("FinaleScript Generated", f"FinaleScript has been generated at:\n\n{script_path}\n\nPlease go to Finale and run the FinaleScript that was generated in 'Plug-Ins -> FinaleScript Palette' to batch process all your project files in the selected folder to MusicXML.\n\n Please reach out to @SterlingMOliver on Twitter or Instagram if something breaks. I am not a Finale user, just doing my best to help.")

root = tk.Tk()
root.title("Finale to MusicXML Batch Converter")

frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

label = tk.Label(frame, text="Finale to MusicXML Batch Converter", font=("Arial", 14))
label.pack(pady=10)

description = tk.Label(frame, text="Select the folder containing Finale files and where to save the FinaleScript:", wraplength=400, justify="left")
description.pack(pady=10)

run_button = tk.Button(frame, text="Generate FinaleScript", command=run_script)
run_button.pack(pady=10)

instructions = tk.Label(frame, text="After running, please go to the folder that the script was exported to and run that FinaleScript in Finale to batch process all your Finale files in the selected folder to MusicXML.", wraplength=400, justify="left", fg="red")
instructions.pack(pady=10)

instructions = tk.Label(frame, text="Please reach out to @SterlingMOliver on Twitter or Instagram if something breaks. I am not a Finale user, just doing my best to help.", wraplength=400, justify="left", fg="blue")
instructions.pack(pady=10)

root.mainloop()
