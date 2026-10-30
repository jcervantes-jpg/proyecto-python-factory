import threading
import time
import random
from datetime import datetime

# Código de colores ANSI para la consola
GREEN = "\033[92m"
WHITE = "\033[97m"
RESET = "\033[0m"

def simular_notificaciones(stop_event):
    contactos = ["Carlos", "María", "Grupo Trabajo", "Ana", "Mamá"]
    mensajes = [
        "¡Hola! ¿Cómo estás?",
        "¿Viste el código que subí a GitHub?",
        "Mañana nos vemos a las 10.",
        "Enviado una imagen 📷",
        "¿Tienes un minuto para revisar algo?"
    ]

    while not stop_event.is_set():
        # Esperar un tiempo aleatorio entre 2 y 5 segundos
        tiempo_espera = random.uniform(2.0, 5.0)
        
        # Esperar en intervalos cortos para responder rápido al salir
        if stop_event.wait(tiempo_espera):
            break

        contacto = random.choice(contactos)
        mensaje = random.choice(mensajes)
        hora = datetime.now().strftime("%H:%M:%S")

        # Imprimir la notificación en consola
        print(f"\n{GREEN}[💬 WhatsApp - {hora}]{RESET}")
        print(f"{WHITE}De: {contacto}{RESET}")
        print(f"Mensaje: {mensaje}")
        print("-" * 40)

def main():
    print("=== SIMULADOR DE NOTIFICACIONES DE WHATSAPP (PYTHON) ===")
    print("Presiona ENTER para salir en cualquier momento.\n")

    # Evento para detener el hilo secundario al finalizar
    stop_event = threading.Event()

    # Iniciar el hilo de notificaciones en segundo plano (daemon)
    hilo_notificaciones = threading.Thread(
        target=simular_notificaciones, 
        args=(stop_event,), 
        daemon=True
    )
    hilo_notificaciones.start()

    # Esperar entrada del usuario para salir
    input()
    stop_event.set()
    print("\nCerrando aplicación...")

if __name__ == "__main__":
    main()