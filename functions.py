from fpdf import FPDF

FILEPATH = "todos.txt"


def get_todos(filepath=FILEPATH):
    """ Read a text file and return
    the list of to-do items.
    """

    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_arg, filepath=FILEPATH):
    """ Write the to-do items list
    in the text file """
    with open(filepath, 'w') as file:
        file.writelines(todos_arg)


def txt_to_pdf(filepath=FILEPATH):
    pdf_local = FPDF(orientation="P", unit="mm", format="A4")
    pdf_local.add_page()
    pdf_local.set_font(family="Times", style="B", size=12)

    with open(filepath, 'r') as file:
        todos_local = file.readlines()
        for i in todos_local:
            pdf_local.cell(w=0, h=12, txt=i, align='L', ln=1)
    return pdf_local


if __name__ == "__main__":
    print("Hello")
    print(get_todos())
