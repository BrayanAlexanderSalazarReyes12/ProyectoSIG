
# This file was generated by the Tkinter Designer by Parth Jadhav
# https://github.com/ParthJadhav/Tkinter-Designer


from pathlib import Path

# from tkinter import *
# Explicit imports to satisfy Flake8
from tkinter import *
from textToSpech import run_tests_and_additional_code
import textToSpech 

OUTPUT_PATH = Path(__file__).parent
ASSETS_PATH = OUTPUT_PATH / "assets/frame0"


def relative_to_assets(path: str) -> Path:
    return ASSETS_PATH / Path(path)


window = Tk()

window.geometry("800x600")
window.configure(bg = "#FFFFFF")
window.title("Software OVA Fonducar")
window.iconbitmap("icon.ico")

canvas = Canvas(
    window,
    bg = "#FFFFFF",
    height = 600,
    width = 800,
    bd = 0,
    highlightthickness = 0,
    relief = "ridge"
)

canvas.place(x = 0, y = 0)
image_image_1 = PhotoImage(
    file=relative_to_assets("image_1.png"))
image_1 = canvas.create_image(
    400.0,
    300.0,
    image=image_image_1
)

image_image_2 = PhotoImage(
    file=relative_to_assets("image_2.png"))
image_2 = canvas.create_image(
    125.0,
    300.0,
    image=image_image_2
)

image_image_3 = PhotoImage(
    file=relative_to_assets("image_3.png"))
image_3 = canvas.create_image(
    128.0,
    572.0,
    image=image_image_3
)

# Define a function to handle clicks on the image
def on_image_click(event: Event):
    titulo = entry_1.get("1.0", "end-1c")
    mensaje = entry_2.get("1.0", "end-1c")
    print(f"{titulo}.mp4")
    textToSpech.mensaje1 = mensaje
    textToSpech.titulo = titulo
    run_tests_and_additional_code()
    entry_1.delete("1.0", "end")
    entry_2.delete("1.0", "end")


# Bind the click event to the image
canvas.tag_bind(image_3, "<Button-1>", on_image_click)

canvas.create_text(
    273.0,
    34.0,
    anchor="nw",
    text="Título:",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

canvas.create_text(
    501.0,
    140.0,
    anchor="nw",
    text="Contenido",
    fill="#000000",
    font=("Inter Bold", 20 * -1)
)

entry_image_1 = PhotoImage(
    file=relative_to_assets("entry_1.png"))
entry_bg_1 = canvas.create_image(
    557.0,
    47.5,
    image=entry_image_1
)
entry_1 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    highlightthickness=0
)
entry_1.place(
    x=350.0,
    y=35.0,
    width=400.0,
    height=25.0
)

entry_image_2 = PhotoImage(
    file=relative_to_assets("entry_2.png"))
entry_bg_2 = canvas.create_image(
    526.5,
    310.5,
    image=entry_image_2
)
entry_2 = Text(
    bd=0,
    bg="#D9D9D9",
    fg="#000716",
    wrap=WORD,
    highlightthickness=0
)
entry_2.place(
    x=310.0,
    y=182.0,
    width=440.0,
    height=259.0
)

image_image_4 = PhotoImage(
    file=relative_to_assets("image_4.png"))
image_4 = canvas.create_image(
    735.0,
    536.0,
    image=image_image_4
)

canvas.create_rectangle(
    -2.0,
    50.0,
    250.0,
    52.0,
    fill="#FFFFFF",
    outline="")

image_image_5 = PhotoImage(
    file=relative_to_assets("image_5.png"))
image_5 = canvas.create_image(
    124.0,
    306.0,
    image=image_image_5
)
window.resizable(False, False)
window.mainloop()
