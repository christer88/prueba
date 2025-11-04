# ⚡ INSTALACIÓN RÁPIDA - COMANDOS LISTOS

Este archivo contiene todos los comandos necesarios para instalar y ejecutar el sistema completo con **Pruebas Avanzadas**.
**Copia y pega cada bloque según tu sistema operativo.**

---

## 🚀 INSTALACIÓN AUTOMÁTICA (RECOMENDADA)

### Opción 1: Instalador Completo
```bash
# Linux/Mac
./install_dependencies.sh

# Windows
install_dependencies.bat
```

### Opción 2: Solo Dependencias Python
```bash
python quick_install.py
# o
python3 quick_install.py
```

---

## 🐧 LINUX (Ubuntu/Debian)

### Paso 1: Verificar Python
```bash
python3 --version
# Debe mostrar Python 3.7 o superior
```

### Paso 2: Instalar Dependencias Básicas
```bash
# Instalar librerías básicas del monitor
pip3 install flask waitress requests dnspython urllib3 python-docx --break-system-packages
```

### Paso 2b: Instalar Dependencias para Pruebas Avanzadas
```bash
# Para pruebas avanzadas de red
pip3 install scapy netifaces --break-system-packages
```

### Paso 2c: Instalar Herramientas del Sistema
```bash
# Herramientas necesarias para pruebas avanzadas
sudo apt-get update
sudo apt-get install -y nmap mtr iperf3 nodejs npm

# Fast-cli para test de Netflix
sudo npm install -g fast-cli
```

### Paso 3: Instalar Speedtest CLI (Opcional)
```bash
# Método 1: Desde repositorios
sudo apt update
sudo apt install speedtest-cli -y

# Método 2: Usando pip
pip3 install speedtest-cli --break-system-packages
```

### Paso 4: Crear Directorio de Trabajo
```bash
mkdir ~/network-monitor
cd ~/network-monitor
```

### Paso 5: Descargar el Script
```bash
# Coloca aquí el archivo network_monitor_with_report.py
# O copia y pega el contenido del script
```

### Paso 6: Ejecutar
```bash
python3 network_monitor_with_report.py
```

---

## 🪟 WINDOWS

### Paso 1: Verificar Python
```cmd
python --version
REM Debe mostrar Python 3.7 o superior
```

### Paso 2: Instalar Dependencias Básicas
```cmd
pip install flask waitress requests dnspython urllib3 python-docx
```

### Paso 2b: Instalar Dependencias para Pruebas Avanzadas
```cmd
pip install scapy netifaces
```

### Paso 2c: Instalar Herramientas del Sistema
```cmd
REM Opción 1: Chocolatey (recomendado)
choco install nmap iperf3 nodejs -y

REM Después instalar fast-cli
npm install -g fast-cli

REM Opción 2: Instalación manual
REM nmap: https://nmap.org/download.html
REM iperf3: https://iperf.fr/iperf-download.php
REM WinMTR: https://winmtr.net/
REM Node.js: https://nodejs.org
```

### Paso 3: Instalar Speedtest CLI (Opcional)
```cmd
REM Descargar desde: https://www.speedtest.net/apps/cli
REM O usar Chocolatey:
choco install speedtest
```

### Paso 4: Crear Directorio de Trabajo
```cmd
mkdir C:\network-monitor
cd C:\network-monitor
```

### Paso 5: Descargar el Script
```cmd
REM Coloca aquí el archivo network_monitor_with_report.py
```

### Paso 6: Ejecutar
```cmd
python network_monitor_with_report.py
```

---

## 🍎 macOS

### Paso 1: Verificar Python
```bash
python3 --version
# Debe mostrar Python 3.7 o superior
```

### Paso 2: Instalar Dependencias Básicas
```bash
pip3 install flask waitress requests dnspython urllib3 python-docx
```

### Paso 2b: Instalar Dependencias para Pruebas Avanzadas
```bash
pip3 install scapy netifaces
```

### Paso 2c: Instalar Herramientas del Sistema
```bash
# Usando Homebrew
brew install nmap mtr iperf3 node

# Fast-cli para test de Netflix
npm install -g fast-cli
```

### Paso 3: Instalar Speedtest CLI (Opcional)
```bash
# Usando Homebrew
brew install speedtest-cli

# O usando pip
pip3 install speedtest-cli
```

### Paso 4: Crear Directorio de Trabajo
```bash
mkdir ~/network-monitor
cd ~/network-monitor
```

### Paso 5: Descargar el Script
```bash
# Coloca aquí el archivo network_monitor_with_report.py
```

### Paso 6: Ejecutar
```bash
python3 network_monitor_with_report.py
```

---

## 🔧 VERIFICACIÓN DE INSTALACIÓN

### Verificar Librerías Instaladas
```bash
# Python
python3 -c "import flask; print('Flask OK')"
python3 -c "import waitress; print('Waitress OK')"
python3 -c "import requests; print('Requests OK')"
python3 -c "import dns.resolver; print('DNSPython OK')"
python3 -c "import urllib3; print('urllib3 OK')"
python3 -c "import docx; print('python-docx OK')"
```

### Verificar Speedtest
```bash
speedtest --version
```

---

## 📝 CREAR ARCHIVO DE SITIOS PERSONALIZADO

### Linux/macOS
```bash
cat > websites.txt << 'EOF'
# Sitios a monitorear
google.com
8.8.8.8
facebook.com
1.1.1.1
# Agrega tus propios sitios aquí
EOF
```

### Windows (PowerShell)
```powershell
@"
# Sitios a monitorear
google.com
8.8.8.8
facebook.com
1.1.1.1
# Agrega tus propios sitios aquí
"@ | Out-File -FilePath websites.txt -Encoding UTF8
```

---

## 🚀 EJECUCIÓN COMO SERVICIO (OPCIONAL)

### Linux (systemd)

#### Paso 1: Crear archivo de servicio
```bash
sudo nano /etc/systemd/system/network-monitor.service
```

#### Paso 2: Contenido del archivo
```ini
[Unit]
Description=Network Monitor with Reports
After=network.target

[Service]
Type=simple
User=tu_usuario
WorkingDirectory=/home/tu_usuario/network-monitor
ExecStart=/usr/bin/python3 /home/tu_usuario/network-monitor/network_monitor_with_report.py
Restart=always
RestartSec=10

[Install]
WantedBy=multi-user.target
```

#### Paso 3: Habilitar e iniciar
```bash
sudo systemctl daemon-reload
sudo systemctl enable network-monitor
sudo systemctl start network-monitor
```

#### Paso 4: Verificar estado
```bash
sudo systemctl status network-monitor
```

#### Comandos útiles
```bash
# Ver logs
sudo journalctl -u network-monitor -f

# Reiniciar servicio
sudo systemctl restart network-monitor

# Detener servicio
sudo systemctl stop network-monitor
```

---

### Windows (Tarea Programada)

#### Método 1: Usando GUI
1. Abrir "Programador de Tareas"
2. Crear tarea básica
3. Nombre: "Network Monitor"
4. Desencadenador: Al iniciar el sistema
5. Acción: Iniciar programa
6. Programa: `C:\Python39\python.exe`
7. Argumentos: `C:\network-monitor\network_monitor_with_report.py`
8. Finalizar

#### Método 2: Usando PowerShell (Administrador)
```powershell
$action = New-ScheduledTaskAction -Execute 'python.exe' -Argument 'C:\network-monitor\network_monitor_with_report.py' -WorkingDirectory 'C:\network-monitor'
$trigger = New-ScheduledTaskTrigger -AtStartup
$principal = New-ScheduledTaskPrincipal -UserId "$env:USERDOMAIN\$env:USERNAME" -LogonType ServiceAccount
Register-ScheduledTask -TaskName "Network Monitor" -Action $action -Trigger $trigger -Principal $principal
```

---

## 🐳 DOCKER (OPCIONAL)

### Paso 1: Crear Dockerfile
```dockerfile
FROM python:3.11-slim

WORKDIR /app

RUN apt-get update && apt-get install -y \
    iputils-ping \
    curl \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir flask waitress requests dnspython urllib3 python-docx

# Instalar speedtest-cli
RUN curl -s https://packagecloud.io/install/repositories/ookla/speedtest-cli/script.deb.sh | bash && \
    apt-get install -y speedtest

COPY network_monitor_with_report.py .
COPY websites.txt .

EXPOSE 5000

CMD ["python", "network_monitor_with_report.py"]
```

### Paso 2: Construir imagen
```bash
docker build -t network-monitor .
```

### Paso 3: Ejecutar contenedor
```bash
docker run -d \
  --name network-monitor \
  -p 5000:5000 \
  -v $(pwd)/reports:/app/reports \
  -v $(pwd)/data_backups:/app/data_backups \
  -v $(pwd)/ping_results.json:/app/ping_results.json \
  -v $(pwd)/speedtest_results.json:/app/speedtest_results.json \
  network-monitor
```

### Paso 4: Ver logs
```bash
docker logs -f network-monitor
```

---

## 🔍 COMANDOS DE DIAGNÓSTICO

### Verificar que el Servicio Está Corriendo
```bash
# Linux/macOS
curl http://localhost:5000

# Windows (PowerShell)
Invoke-WebRequest -Uri http://localhost:5000
```

### Ver Procesos Python
```bash
# Linux/macOS
ps aux | grep python

# Windows (PowerShell)
Get-Process python
```

### Verificar Puerto 5000
```bash
# Linux
sudo netstat -tulpn | grep 5000

# macOS
sudo lsof -i :5000

# Windows (PowerShell)
netstat -ano | findstr 5000
```

### Probar Conectividad Básica
```bash
# Ping a Google DNS
ping -c 4 8.8.8.8

# Resolución DNS
nslookup google.com

# Speedtest
speedtest
```

---

## 🛠️ SOLUCIÓN RÁPIDA DE PROBLEMAS

### Error: "ModuleNotFoundError: No module named 'docx'"
```bash
pip3 install python-docx --break-system-packages
```

### Error: "Permission denied" al crear archivos
```bash
# Linux/macOS
chmod 755 .
mkdir -p reports data_backups

# Windows (ejecutar como Administrador)
icacls . /grant Everyone:F
```

### Puerto 5000 ya en uso
```bash
# Cambiar puerto en el script
# Editar línea: FLASK_PORT = 5001
```

### Speedtest no funciona
```bash
# Verificar instalación
speedtest --version

# Aceptar licencia manualmente
speedtest --accept-license --accept-gdpr
```

---

## 📊 COMANDOS PARA GENERAR REPORTES

### Desde Línea de Comandos (usando curl)

```bash
# Generar reporte
curl -X POST http://localhost:5000/api/generate-report

# Ver resultado (copiar el nombre del archivo de la respuesta)
curl http://localhost:5000/api/download-report/Reporte_Red_20251026_173045.docx -o reporte.docx
```

### Desde Python (script auxiliar)

```python
import requests
import json

# Generar reporte
response = requests.post('http://localhost:5000/api/generate-report')
result = response.json()

if result['success']:
    print(f"Reporte generado: {result['filename']}")
    
    # Descargar
    download_url = f"http://localhost:5000{result['download_url']}"
    report = requests.get(download_url)
    
    with open(result['filename'], 'wb') as f:
        f.write(report.content)
    
    print(f"Reporte descargado: {result['filename']}")
else:
    print(f"Error: {result['error']}")
```

---

## 🔄 ACTUALIZACIÓN DEL SCRIPT

### Backup del Script Actual
```bash
# Linux/macOS
cp network_monitor_with_report.py network_monitor_with_report.py.backup

# Windows
copy network_monitor_with_report.py network_monitor_with_report.py.backup
```

### Aplicar Nueva Versión
```bash
# Detener el servicio
sudo systemctl stop network-monitor  # Linux
# O cerrar manualmente en Windows

# Reemplazar archivo
# Copiar nuevo script

# Reiniciar
sudo systemctl start network-monitor  # Linux
# O ejecutar nuevamente en Windows
```

---

## 📦 ESTRUCTURA DE ARCHIVOS FINAL

```
network-monitor/
├── network_monitor_with_report.py  (Script principal)
├── websites.txt                    (Sitios a monitorear)
├── ping_results.json               (Datos de ping)
├── speedtest_results.json          (Datos de velocidad)
├── reports/                        (Reportes generados)
│   ├── Reporte_Red_20251026_100000.docx
│   ├── Reporte_Red_20251026_170000.docx
│   └── ...
├── templates/                      (Plantillas HTML - auto-generadas)
│   ├── index.html
│   ├── history.html
│   └── speedtest_history.html
└── data_backups/                   (Respaldos - auto-generados)
    ├── backup_20251026_120000.json
    └── ...
```

---

## ✅ CHECKLIST RÁPIDO

```
□ Python 3.7+ instalado
□ Dependencias pip instaladas (6 paquetes)
□ Speedtest CLI instalado (opcional)
□ Script descargado
□ Archivo websites.txt configurado
□ Permisos de escritura verificados
□ Puerto 5000 disponible
□ Script ejecutándose
□ Navegador abierto en localhost:5000
□ Datos capturándose (esperar 5-10 min)
□ Primer reporte generado exitosamente
```

---

## 🎯 COMANDOS DE USO DIARIO

### Iniciar el Sistema
```bash
python3 network_monitor_with_report.py
```

### Verificar Estado
```bash
curl http://localhost:5000/api/dashboard-stats | python3 -m json.tool
```

### Generar Reporte (API)
```bash
curl -X POST http://localhost:5000/api/generate-report
```

### Ver Últimos Logs
```bash
tail -f nohup.out  # Si se ejecutó con nohup
```

### Backup Manual de Datos
```bash
cp ping_results.json ping_results.json.$(date +%Y%m%d_%H%M%S)
cp speedtest_results.json speedtest_results.json.$(date +%Y%m%d_%H%M%S)
```

---

## 🚨 EN CASO DE EMERGENCIA

### Reinicio Completo
```bash
# 1. Detener el proceso
killall python3  # Linux/macOS
# O Ctrl+C en la ventana de ejecución

# 2. Limpiar archivos temporales
rm -rf __pycache__
rm -rf templates/*.pyc

# 3. Verificar integridad de datos
python3 -c "import json; json.load(open('ping_results.json'))"

# 4. Reiniciar
python3 network_monitor_with_report.py
```

### Restaurar desde Backup
```bash
# Copiar último backup
cp data_backups/backup_*.json ping_results.json
```

---

---

## 🔬 PRUEBAS AVANZADAS

### ¿Qué Son?
Las **Pruebas Avanzadas** son 6 nuevas funcionalidades de diagnóstico de red:

1. **🔍 Descubrimiento DHCP** - Detecta servidores DHCP en la red
2. **🌐 Descubrimiento de Red** - Escanea dispositivos con nmap
3. **🛣️ Análisis MTR** - Análisis continuo de rutas de red
4. **🎬 Test Netflix CDN** - Velocidad específica de Netflix
5. **📞 Test Jitter UDP** - Simula videollamadas (iperf3)
6. **🌍 Test DNS CDN** - Análisis de resolución DNS

### Cómo Acceder
1. Ejecutar el monitor: `python3 network_monitor_with_report.py`
2. Abrir navegador en: `http://localhost:5000`
3. Hacer clic en el botón **"🔬 Pruebas Avanzadas"**

### Permisos Especiales
- **Pruebas DHCP**: Requieren permisos de administrador
  ```bash
  # Linux/Mac
  sudo python3 network_monitor_with_report.py

  # Windows
  # Ejecutar CMD como Administrador
  python network_monitor_with_report.py
  ```

### Verificar Instalación Completa
```bash
# Verificar dependencias Python
python3 -c "import scapy, netifaces; print('✅ Pruebas avanzadas: OK')"

# Verificar herramientas del sistema
nmap --version      # ✅ nmap OK
mtr --version       # ✅ mtr OK (Linux/Mac)
iperf3 --version    # ✅ iperf3 OK
npm --version       # ✅ npm OK
fast --version      # ✅ fast-cli OK
```

---

**¡Listo para comenzar el monitoreo profesional de tu red con Pruebas Avanzadas!** 🚀

Para más detalles, consulta:
- **PRUEBAS_AVANZADAS_README.md** (guía completa de pruebas avanzadas)
- README.md (visión general)
- INSTRUCCIONES_REPORTE.md (guía completa)
- EJEMPLO_REPORTE.md (ejemplo de reporte)
- RESUMEN_CAMBIOS.md (detalles técnicos)
