import subprocess
import sys
import time
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler


class Reiniciador(FileSystemEventHandler):

    def __init__(self):
        self.processo = None
        self.iniciar_programa()

    def iniciar_programa(self):
        if self.processo:
            self.processo.terminate()

        self.processo = subprocess.Popen(
            [sys.executable, "main.py"]
        )

    def on_modified(self, event):
        if event.src_path.endswith(".py"):
            print(f"\nArquivo alterado: {event.src_path}")
            print("Reiniciando Quizem...\n")

            time.sleep(0.2)
            self.iniciar_programa()


handler = Reiniciador()

observer = Observer()
observer.schedule(handler, ".", recursive=True)
observer.start()

print("👀 Auto-reload ativado!")
print("Salve um arquivo .py para reiniciar o Quizem.\n")

try:
    while True:
        time.sleep(1)

except KeyboardInterrupt:
    observer.stop()

observer.join()