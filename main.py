from notificaciones.factory import NotificacionFactory

servicio = NotificacionFactory.crear("email", correo="estudiante@ecotec.edu.ec")
servicio.enviar("Hola desde el servicio de Email")
