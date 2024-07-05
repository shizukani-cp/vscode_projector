import PySimpleGUI as sg

sg.set_options(font=(None, 24))

file_types = (("VS codeプロジェクトファイル", ".vscodeprj"), ("すべてのファイル", "*"))
layout = [
    [sg.Text("プロジェクトファイルのパス:"), sg.Input(k="path"), sg.FileBrowse("参照", file_types=file_types)],
    [sg.Button("開く", k="open")],
    [sg.Button("保存", k="save")],
    [sg.Button("閉じる", k="close", button_color="red")]
]

win = sg.Window("VS code projector", layout)

while True:
    e, v = win.read()
    if e in (None, "close"): break
win.close()