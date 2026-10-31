from notificaciones.servicios import NotificacionEmail


class NotificacionFactory:
    @staticmethod
    def crear(tipo, **datos):
        if tipo == "email":
            return NotificacionEmail(datos["correo"])
        raise ValueError(f"Tipo de notificacion no soportado: {tipo}")
