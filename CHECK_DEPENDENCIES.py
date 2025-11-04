#!/usr/bin/env python3
"""
Script de verificación de dependencias para Monitor de Red - Pruebas Avanzadas
Ejecutar con: python CHECK_DEPENDENCIES.py
"""

import subprocess
import sys
import platform
import importlib.util

def check_python_package(package_name, import_name=None):
    """Verifica si un paquete de Python está instalado"""
    if import_name is None:
        import_name = package_name

    try:
        spec = importlib.util.find_spec(import_name)
        if spec is not None:
            print(f"✅ {package_name}: OK")
            return True
        else:
            print(f"❌ {package_name}: NO INSTALADO")
            return False
    except ImportError:
        print(f"❌ {package_name}: NO INSTALADO")
        return False

def check_system_command(command, name):
    """Verifica si un comando del sistema está disponible"""
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=5)
        print(f"✅ {name}: OK")
        return True
    except (subprocess.TimeoutExpired, FileNotFoundError, subprocess.CalledProcessError):
        print(f"❌ {name}: NO INSTALADO")
        return False

def get_installation_commands():
    """Retorna comandos de instalación según el sistema operativo"""
    system = platform.system().lower()

    if system == "windows":
        return {
            "python_packages": "pip install scapy netifaces dnspython python-docx requests flask waitress",
            "nmap": "winget install Insecure.Nmap",
            "iperf3": "winget install iperf3",
            "nodejs": "winget install OpenJS.NodeJS",
            "fast-cli": "npm install -g fast-cli",
            "mtr": "winget install WinMTR"
        }
    elif system == "darwin":  # macOS
        return {
            "python_packages": "pip3 install scapy netifaces dnspython python-docx requests flask waitress",
            "nmap": "brew install nmap",
            "iperf3": "brew install iperf3",
            "nodejs": "brew install node",
            "fast-cli": "npm install -g fast-cli",
            "mtr": "brew install mtr"
        }
    else:  # Linux
        return {
            "python_packages": "pip3 install scapy netifaces dnspython python-docx requests flask waitress",
            "nmap": "sudo apt install nmap  # Ubuntu/Debian",
            "iperf3": "sudo apt install iperf3  # Ubuntu/Debian",
            "nodejs": "sudo apt install nodejs npm  # Ubuntu/Debian",
            "fast-cli": "sudo npm install -g fast-cli",
            "mtr": "sudo apt install mtr  # Ubuntu/Debian"
        }

def main():
    print("=" * 70)
    print("  VERIFICADOR DE DEPENDENCIAS - MONITOR DE RED PRUEBAS AVANZADAS")
    print("=" * 70)
    print()

    # Información del sistema
    system = platform.system()
    print(f"🖥️  Sistema: {system}")
    print(f"🐍 Python: {sys.version.split()[0]}")
    print()

    # Verificar paquetes Python
    print("📦 VERIFICANDO PAQUETES PYTHON:")
    print("-" * 35)

    python_packages = [
        ("scapy", "scapy"),
        ("netifaces", "netifaces"),
        ("dnspython", "dns"),
        ("python-docx", "docx"),
        ("requests", "requests"),
        ("flask", "flask"),
        ("waitress", "waitress")
    ]

    python_ok = 0
    for package, import_name in python_packages:
        if check_python_package(package, import_name):
            python_ok += 1

    print()
    print("🔧 VERIFICANDO HERRAMIENTAS DEL SISTEMA:")
    print("-" * 40)

    # Verificar herramientas del sistema
    system_tools = []
    if system.lower() == "windows":
        system_tools = [
            (["nmap", "--version"], "nmap"),
            (["iperf3", "--version"], "iperf3"),
            (["node", "--version"], "Node.js"),
            (["fast", "--version"], "fast-cli"),
            (["pathping"], "PathPing (incluido en Windows)"),
            (["winmtr"], "WinMTR")  # WinMTR no tiene --version
        ]
    else:
        system_tools = [
            (["nmap", "--version"], "nmap"),
            (["iperf3", "--version"], "iperf3"),
            (["mtr", "--version"], "mtr (equivalente a PathPing)"),
            (["node", "--version"], "Node.js"),
            (["fast", "--version"], "fast-cli")
        ]

    system_ok = 0
    for cmd, name in system_tools:
        if check_system_command(cmd, name):
            system_ok += 1

    print()
    print("=" * 70)
    print("📊 RESUMEN:")
    print(f"   Python packages: {python_ok}/{len(python_packages)}")
    print(f"   System tools: {system_ok}/{len(system_tools)}")

    if python_ok == len(python_packages) and system_ok == len(system_tools):
        print("✅ TODAS LAS DEPENDENCIAS ESTÁN INSTALADAS")
        print("🚀 Puedes ejecutar todas las pruebas avanzadas!")
    else:
        print("⚠️  FALTAN ALGUNAS DEPENDENCIAS")
        print()

        commands = get_installation_commands()
        print("🔧 COMANDOS DE INSTALACIÓN:")
        print("-" * 25)

        if python_ok < len(python_packages):
            print(f"📦 Paquetes Python:")
            print(f"   {commands['python_packages']}")
            print()

        if system_ok < len(system_tools):
            print("🔧 Herramientas del sistema:")
            for tool in ["nmap", "iperf3", "nodejs", "fast-cli", "mtr"]:
                if tool in commands:
                    print(f"   {tool}: {commands[tool]}")
            print()

        print("💡 INSTALACIÓN AUTOMÁTICA:")
        if system.lower() == "windows":
            print("   python quick_install.py       # Solo paquetes Python")
            print("   install_dependencies.bat      # Todo (requiere permisos admin)")
        else:
            print("   python3 quick_install.py      # Solo paquetes Python")
            print("   ./install_dependencies.sh     # Todo (requiere sudo)")

    print("=" * 70)

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Verificación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        sys.exit(1)