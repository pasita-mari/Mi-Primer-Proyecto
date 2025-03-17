import rclpy
from rclpy.node import Node
from geometry_msgs.msg import Twist
import time
import math

class DibujanteTortuga(Node):
    def __init__(self):
        super().__init__('dibujante_tortuga')
        self.publisher_ = self.create_publisher(Twist, '/turtle1/cmd_vel', 10)

    def mover_tortuga(self, velocidad_lineal, velocidad_angular, tiempo):
        msg = Twist()
        msg.linear.x = velocidad_lineal
        msg.angular.z = velocidad_angular
        self.publisher_.publish(msg)
        time.sleep(tiempo)

    def dibujar_circulo(self, radio, completo=False):  # Añadido parámetro 'completo'
        velocidad_angular = 0.5  # Ajusta este valor para controlar la curvatura
        tiempo_total = (2 * math.pi * radio) / abs(velocidad_angular)  # Cálculo más preciso

        tiempo_transcurrido = 0.0
        while tiempo_transcurrido < tiempo_total / (2 if not completo else 1):  # Controla si dibuja medio círculo o completo
            tiempo_a_avanzar = 0.05  # Ajusta este valor para la suavidad del círculo
            self.mover_tortuga(0.0, velocidad_angular, tiempo_a_avanzar)  # Solo gira para dibujar el círculo
            tiempo_transcurrido += tiempo_a_avanzar

def main(args=None):
    rclpy.init(args=args)
    dibujante_tortuga = DibujanteTortuga()

    radio = 2.0

    # Avanza una distancia (ajusta los valores según tu preferencia)
    dibujante_tortuga.mover_tortuga(3.0, 0.0, 2.0)  # Avanza 2 segundos

    # Dibuja medio círculo
    dibujante_tortuga.dibujar_circulo(radio)

    rclpy.shutdown()

if __name__ == '__main__':
    main()