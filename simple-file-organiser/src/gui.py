from PySimpleGUI import Text, Input, FolderBrowse, Multiline, Button, Window, Text, WIN_CLOSED
from simple_file_organiser import SimpleFileOrganiser

def run():
    layout = [
        [Text("Directory"), Input(key="directory", default_text=os.getcwd()), FolderBrowse()],
        [Multiline("Enter keywords (one per line)", key="keywords", size=(None, 5))],
        [Text("Unsorted Folder"), Input(key="unsorted_folder", default_text="Unsorted")],
        [Text("Invalid Folder"), Input(key="invalid_folder", default_text="Invalid")],
        [Text("Valid Extensions (comma-separated)"), Input(key='extensions', default_text="pdf")],
        [Button("Run"), Text("", key="status")]
    ]

    window = Window("File Organiser", layout)

    while True:
        event, values = window.read()
        if event == WIN_CLOSED or event == "Run":
            if event == "Run":
                SimpleFileOrganiser(
                    values["directory"],
                    values["keywords"].split("\n"),
                    values["unsorted_folder"],
                    values["invalid_folder"],
                    values["extensions"].split(",")
                ).run()
                window["status"].update("Complete!") 
            break
    window.close()
