import subprocess
import sys
import os

# UI dosyalarÄ±nÄ±n listesi
ui_files = [
    "ui/frmMain.ui",
]

# Ã‡Ä±ktÄ± klasÃ¶rÃ¼ yoksa oluÅŸtur
os.makedirs("forms", exist_ok=True)

for ui_file in ui_files:
    file_name = os.path.basename(ui_file).replace(".ui", "")
    py_file = f"forms/Ui_{file_name}.py"

    # Raspberry Pi iÃ§in gÃ¼venli yÃ¶ntem (python -m ile)
    command = [sys.executable, "-m", "PyQt5.uic.pyuic", ui_file, "-o", py_file]

    try:
        subprocess.run(command, check=True)
        print(f"{ui_file} Dönüştürüldü.")
    except subprocess.CalledProcessError as e:
        print(f"{ui_file} Hata: {e}")




# resim dönüştürme  = pyrcc5 -o Resources_rc.py Resources.qrc
# demoya donuştürme = pyinstaller --onefile --icon=restorant.ico frmGiris.py
# demoya donuştürme = pyinstaller --onefile --icon=restorant.ico --noconsole frmGiris.py