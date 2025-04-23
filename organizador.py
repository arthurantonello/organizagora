from categorias import CATEGORIAS
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler
from pathlib import Path
from datetime import datetime
import shutil, time

# Mapeia extensão para categoria
ext2cat = {ext: cat for cat, exts in CATEGORIAS.items() for ext in exts}

# Pasta a ser organizada
pasta = Path.home() / "Downloads"

LOG_FILE = Path(__file__).parent / "organizador_log.txt"

class OrganizadorHandler(FileSystemEventHandler):
    def on_created(self, event):
        if not event.is_directory:
            organizar_arquivo(Path(event.src_path))

def log(msg, tipo = 'INFO'):
    agora = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    mensagem = f"[{tipo} - {agora}] {msg}"
    print(mensagem)

    try:
        with open(LOG_FILE, "a", encoding="utf-8") as f:
            f.write(mensagem + "\n")
    except Exception as e:
        # Se der erro ao gravar, pelo menos mostramos no console
        print(f"[ERRO - {agora}] não conseguiu escrever no log: {e}")

def organizar_arquivo(arquivo: Path):
    ext = arquivo.suffix.lower().lstrip('.')
    categoria = ext2cat.get(ext, 'Outros') # Se não houver uma categoria, aloca em 'Outros'
    destino = pasta / categoria
    destino.mkdir(exist_ok= True)

    try:
        mover_com_renome(arquivo, destino)
    except Exception as e:
        log(f"Erro ao mover {arquivo.name}: {e}", tipo="ERRO")

def mover_com_renome(arquivo: Path, destino: Path):
    # cria pasta de destino se não existir
    destino.mkdir(exist_ok= True, parents= True)
    destino_arquivo = destino / arquivo.name

    if destino_arquivo.exists():
        log(f"Conflito: '{destino_arquivo.name}' já existe em {destino}", tipo="ALERTA")
        stem = arquivo.stem
        suffix = arquivo.suffix
        i = 1

        while True:
            novo_nome = f"{stem}_{i}{suffix}"
            candidato = destino / novo_nome

            if not candidato.exists():
                destino_arquivo = candidato
                log(f"Renomeando para '{novo_nome}'", tipo="ALERTA")
                break
            i += 1  
    try:
        shutil.move(str(arquivo), str(destino_arquivo))
        log(f"Movido: {arquivo.name} → {destino.name}", tipo="SUCESSO")
    except Exception as e:
        log(f"Erro ao mover {arquivo.name}: {e}", tipo="ERRO")


if __name__ == '__main__':
    # Caso não queira organizar os arquivos já existentes, apenas remova esse loop
    log("Organizando arquivos existentes...")
    for arquivo in pasta.iterdir():
        if arquivo.is_file():
            organizar_arquivo(arquivo)
    ##
    observer = Observer()
    observer.schedule(OrganizadorHandler(), str(pasta), recursive = False)
    observer.start()

    log(f'Monitorando a pasta {pasta}')
    try:
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()
    log("Monitoramento encerrado.")