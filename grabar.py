import subprocess
import datetime

STREAM_URL = "https://27593.live.streamtheworld.com/LOS40_VILLAO.mp3"
# 4 horas y 30 minutos = 16200 segundos
DURACION_SEGUNDOS = 16200  

fecha_hoy = (datetime.datetime.utcnow() - datetime.timedelta(hours=5)).strftime("%Y-%m-%d")
nombre_archivo = f"Los40_Villavicencio_{fecha_hoy}.mp3"

print(f"Iniciando captura del stream para el archivo: {nombre_archivo}")

comando = [
    "ffmpeg",
    "-y",
    "-reconnect", "1",
    "-reconnect_at_eof", "1",
    "-reconnect_streamed", "1",
    "-reconnect_delay_max", "5",
    "-i", STREAM_URL,
    "-t", str(DURACION_SEGUNDOS),
    "-c", "copy",
    nombre_archivo
]

resultado = subprocess.run(comando)

if resultado.returncode == 0:
    print("Grabación finalizada correctamente.")
else:
    print(f"La grabación finalizó con código de salida {resultado.returncode}")
