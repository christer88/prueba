#!/usr/bin/env python3
"""
Instalador rápido de dependencias Python para Monitor de Red - Pruebas Avanzadas
Ejecutar con: python quick_install.py
"""

import subprocess
import sys
import platform
import os

def run_command(command, description=""):
    """Ejecuta un comando y maneja errores"""
    try:
        print(f"📦 {description}")
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - OK")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ {description} - ERROR: {e.stderr}")
        return False

def check_command(command, name):
    """Verifica si un comando está disponible"""
    try:
        subprocess.run(command, shell=True, check=True, capture_output=True)
        print(f"✅ {name}: OK")
        return True
    except subprocess.CalledProcessError:
        print(f"❌ {name}: No instalado")
        return False

def main():
    print("=" * 60)
    print("  INSTALADOR RÁPIDO - MONITOR DE RED PRUEBAS AVANZADAS")
    print("=" * 60)
    print()

    # Detectar sistema
    system = platform.system()
    print(f"Sistema detectado: {system}")
    print()

    # Verificar Python
    python_cmd = "python3" if system != "Windows" else "python"
    pip_cmd = "pip3" if system != "Windows" else "pip"

    print("1. VERIFICANDO PYTHON Y PIP...")
    print("-" * 30)

    if not check_command(f"{python_cmd} --version", "Python"):
        print("❌ Python no está instalado. Instálalo desde https://python.org")
        return False

    if not check_command(f"{pip_cmd} --version", "pip"):
        print("❌ pip no está disponible")
        return False

    print()
    print("2. ACTUALIZANDO PIP...")
    print("-" * 30)
    run_command(f"{python_cmd} -m pip install --upgrade pip", "Actualizando pip")

    print()
    print("3. INSTALANDO DEPENDENCIAS BÁSICAS...")
    print("-" * 30)

    basic_packages = [
        "flask",
        "waitress",
        "requests",
        "dnspython",
        "python-docx"
    ]

    for package in basic_packages:
        run_command(f"{pip_cmd} install {package}", f"Instalando {package}")

    print()
    print("4. INSTALANDO DEPENDENCIAS PARA PRUEBAS AVANZADAS...")
    print("-" * 30)

    advanced_packages = [
        "scapy",
        "netifaces"
    ]

    for package in advanced_packages:
        run_command(f"{pip_cmd} install {package}", f"Instalando {package}")

    print()
    print("5. VERIFICANDO INSTALACIÓN...")
    print("-" * 30)

    # Verificar importaciones
    test_imports = [
        ("flask", "Flask"),
        ("waitress", "Waitress"),
        ("requests", "Requests"),
        ("dns.resolver", "DNS Python"),
        ("docx", "Python-docx"),
        ("scapy.all", "Scapy"),
        ("netifaces", "Netifaces")
    ]

    all_ok = True
    for module, name in test_imports:
        try:
            __import__(module)
            print(f"✅ {name}: OK")
        except ImportError:
            print(f"❌ {name}: ERROR")
            all_ok = False

    print()
    print("6. VERIFICANDO HERRAMIENTAS DEL SISTEMA...")
    print("-" * 30)

    system_tools = []
    if system == "Windows":
        system_tools = [
            ("nmap --version", "nmap"),
            ("iperf3 --version", "iperf3"),
            ("npm --version", "npm"),
            ("fast --version", "fast-cli")
        ]
    else:
        system_tools = [
            ("nmap --version", "nmap"),
            ("mtr --version", "mtr"),
            ("iperf3 --version", "iperf3"),
            ("npm --version", "npm"),
            ("fast --version", "fast-cli")
        ]

    for cmd, name in system_tools:
        check_command(cmd, name)

    print()
    print("=" * 60)
    if all_ok:
        print("✅ INSTALACIÓN DE DEPENDENCIAS PYTHON COMPLETADA")
    else:
        print("⚠️  INSTALACIÓN COMPLETADA CON ALGUNOS ERRORES")
    print("=" * 60)
    print()

    print("📋 HERRAMIENTAS DEL SISTEMA FALTANTES:")
    print()

    if system == "Windows":
        print("Para completar la instalación, ejecuta:")
        print("  install_dependencies.bat")
        print()
        print("O instala manualmente:")
        print("• nmap: https://nmap.org/download.html")
        print("• iperf3: https://iperf.fr/iperf-download.php")
        print("• Node.js: https://nodejs.org")
        print("• Después: npm install -g fast-cli")
    else:
        print("Para completar la instalación, ejecuta:")
        print("  ./install_dependencies.sh")
        print()
        print("O instala manualmente según tu distribución:")
        print("• Ubuntu/Debian: sudo apt-get install nmap mtr iperf3 nodejs npm")
        print("• CentOS/RHEL: sudo yum install nmap mtr iperf3 nodejs npm")
        print("• macOS: brew install nmap mtr iperf3 node")
        print("• Después: sudo npm install -g fast-cli")

    print()
    print("🔸 IMPORTANTE:")
    print("• Las pruebas DHCP requieren permisos de administrador")
    print("• Ejecutar como: sudo python3 network_monitor_with_report.py")
    print()
    print("🚀 Para ejecutar el monitor:")
    print(f"  {python_cmd} network_monitor_with_report.py")
    print()
    print("🌐 Acceso web: http://localhost:5000")
    print("🔬 Pruebas Avanzadas: Botón en el dashboard principal")

    return all_ok

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n❌ Instalación cancelada por el usuario")
        sys.exit(1)
    except Exception as e:
        print(f"\n\n❌ Error inesperado: {e}")
        sys.exit(1)