import subprocess
import hashlib

def executar_ping(ip_usuario):
    # VULNERABILIDADE 1: Command Injection (Severidade: Alta)
    # O uso de shell=True concatenando input externo permite que 
    # um invasor execute comandos arbitrários no sistema operacional.
    comando = f"ping -c 1 {ip_usuario}"
    subprocess.run(comando, shell=True)

def gerar_hash_senha(senha):
    # VULNERABILIDADE 2: Criptografia Fraca (Severidade: Média/Alta)
    # O algoritmo MD5 é obsoleto e considerado inseguro para proteger dados sensíveis.
    hash_inseguro = hashlib.md5(senha.encode()).hexdigest()
    return hash_inseguro