from notificaciones.base import Notificacion


class NotificacionEmail(Notificacion):
    def __init__(self, correo):
        self.correo = correo

    def enviar(self, mensaje):
        print(f"[Email -> {self.correo}] {mensaje}")
