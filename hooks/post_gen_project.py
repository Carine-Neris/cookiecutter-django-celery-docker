#!/usr/bin/env python3
"""
Hook pós-geração do Cookiecutter para configuração automática do projeto Django.
Este script é executado automaticamente após a criação do projeto.
"""

import os
import sys
import secrets
import subprocess
import shutil
from pathlib import Path

# Cores para output
class Colors:
    RED = '\033[0;31m'
    GREEN = '\033[0;32m'
    YELLOW = '\033[1;33m'
    BLUE = '\033[0;34m'
    PURPLE = '\033[0;35m'
    CYAN = '\033[0;36m'
    WHITE = '\033[1;37m'
    NC = '\033[0m'  # No Color

def print_colored(message, color=Colors.NC):
    """Imprime mensagem colorida"""
    print(f"{color}{message}{Colors.NC}")

def print_status(message):
    print_colored(f"[INFO] {message}", Colors.BLUE)

def print_success(message):
    print_colored(f"[SUCCESS] {message}", Colors.GREEN)

def print_warning(message):
    print_colored(f"[WARNING] {message}", Colors.YELLOW)

def print_error(message):
    print_colored(f"[ERROR] {message}", Colors.RED)

def check_python():
    """Verifica se Python está disponível"""
    python_cmd = None
    
    # Tentar python3 primeiro
    if shutil.which('python3'):
        python_cmd = 'python3'
    elif shutil.which('python'):
        python_cmd = 'python'
    
    if not python_cmd:
        print_error("Python não encontrado! Instale Python antes de continuar.")
        return None
    
    print_status(f"Python encontrado: {python_cmd}")
    return python_cmd

def generate_secret_key():
    """Gera uma SECRET_KEY segura"""
    try:
        chars = 'abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)'
        secret_key = ''.join(secrets.choice(chars) for i in range(50))
        return secret_key
    except Exception as e:
        print_error(f"Erro ao gerar SECRET_KEY: {e}")
        return None

def setup_env_file():
    """Copia .env.template para .env e insere SECRET_KEY"""
    env_template = Path('.env.template')
    env_file = Path('.env')
    
    if not env_template.exists():
        print_error("Arquivo .env.template não encontrado!")
        return False
    
    try:
        # Copiar template para .env
        shutil.copy2(env_template, env_file)
        print_success("Arquivo .env criado!")
        
        # Gerar SECRET_KEY
        secret_key = generate_secret_key()
        if not secret_key:
            return False
        
        # Ler conteúdo do .env
        with open(env_file, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Substituir SECRET_KEY vazia pela gerada
        content = content.replace('SECRET_KEY=', f'SECRET_KEY={secret_key}')
        
        # Escrever conteúdo atualizado
        with open(env_file, 'w', encoding='utf-8') as f:
            f.write(content)
        
        print_success(f"SECRET_KEY gerada e inserida: {secret_key[:10]}...")
        return True
        
    except Exception as e:
        print_error(f"Erro ao configurar arquivo .env: {e}")
        return False

def create_virtual_env():
    """Cria ambiente virtual Python"""
    python_cmd = check_python()
    if not python_cmd:
        return False
    
    try:
        print_status("Criando ambiente virtual...")
        subprocess.run([python_cmd, '-m', 'venv', 'venv'], check=True)
        print_success("Ambiente virtual criado!")
        return True
    except subprocess.CalledProcessError as e:
        print_error(f"Erro ao criar ambiente virtual: {e}")
        return False
    except Exception as e:
        print_error(f"Erro inesperado: {e}")
        return False


def check_docker():
    """Verifica se Docker está disponível"""
    has_docker = shutil.which('docker') is not None
    has_compose = shutil.which('docker-compose') is not None or shutil.which('docker') is not None
    
    if has_docker and has_compose:
        print_success("Docker detectado!")
        return True
    else:
        print_warning("Docker não detectado. Instale Docker para usar containers.")
        return False

def print_next_steps():
    """Mostra próximos passos para o usuário"""
    project_name = "{{ cookiecutter.project_name }}"
    
    print_colored("\n🎉 Configuração concluída com sucesso!", Colors.GREEN)
    print_colored("\n📋 Próximos passos:", Colors.WHITE)
    
    # Comandos específicos por SO
    if os.name == 'nt':  # Windows
        activate_cmd = "venv\\Scripts\\activate"
    else:  # Unix/Linux/MacOS
        activate_cmd = "source venv/bin/activate"
    
    print(f"1. Ativar ambiente virtual: {Colors.GREEN}{activate_cmd}{Colors.NC}")
    print(f"2. Editar arquivo .env com suas configurações específicas")
    
    if check_docker():
        print(f"3. Rodar com Docker: {Colors.GREEN}docker-compose up --build{Colors.NC}")
    
    print_colored(f"\n📁 Projeto criado em: {os.getcwd()}", Colors.CYAN)
    print_colored("📖 Consulte o README.md para mais informações!", Colors.PURPLE)

def main():
    """Função principal do hook pós-geração"""
    print_colored("🚀 Iniciando configuração automática do projeto...", Colors.WHITE)
    
    success_count = 0
    total_steps = 3
    
    # 1. Configurar arquivo .env
    if setup_env_file():
        success_count += 1
    
    # 2. Criar ambiente virtual
    if create_virtual_env():
        success_count += 1
    
    
    # Mostrar resultado
    if success_count == total_steps:
        print_success(f"Todas as {total_steps} etapas concluídas com sucesso!")
    else:
        print_warning(f"{success_count}/{total_steps} etapas concluídas.")
    
    # Mostrar próximos passos
    print_next_steps()

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print_error("\nOperação cancelada pelo usuário.")
        sys.exit(1)
    except Exception as e:
        print_error(f"Erro inesperado: {e}")
        sys.exit(1)
