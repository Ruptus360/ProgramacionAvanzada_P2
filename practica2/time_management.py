import re

class Time():
    TIME_FORMATS:list = ["AM","PM","24 HOURS"]
    time_count:int=0

    def __init__(self,hours,minutes,seconds,time_format)->None:

        self.time_format= time_format
        self.hours = hours
        self.minutes= minutes
        self.seconds = seconds
        
        Time.time_count += 1

    @property
    def hours(self)->int:
        return self._hours

    @hours.setter
    def hours(self,hora)->None:
        if isinstance(hora,int) and hora>=0:
            self._hours=hora
        else:
            raise TypeError("errror de tipo")

    @property
    def minutes(self)->int:
        return self._minutes
    @minutes.setter
    def minutes(self,minutos):
        if isinstance(minutos,int) and minutos>=0 and minutos<60:
            self._minutes = minutos
        else:
            raise ValueError("error de tipo o de valor")

    @property                                        
    def seconds(self) -> int:
        return self._seconds

    @seconds.setter
    def seconds(self, segundos: int) -> None:
        if not isinstance(segundos, int):
            raise TypeError("Los segundos deben ser un entero")
        if not 0 <= segundos <= 59:
            raise ValueError("Los segundos deben estar entre 0 y 59")
        self._seconds = segundos

    @property
    def time_format(self) -> str:
        return self._time_format

    @time_format.setter
    def time_format(self, formato: str) -> None:
        if formato not in Time.TIME_FORMATS:
            raise ValueError(f"Formato no válido. Opciones: {Time.TIME_FORMATS}")
        self._time_format = formato

    def __assign_format(self,time_format):
        if not isinstance(time_format,str):
            return False
        time_format = time_format.upper()
        if time_format not in Time.TIME_FORMATS:
             return False
        else:
            return True                              

    def _is_valid_time(self,hours,minutes,seconds,time_format):   

        if not (0 <= minutes <=59 and 0<= seconds <=59):          
            return False
        if time_format == "24 HOURS":                           
            return 0<= hours <=23
        else:
            return 0<= hours <=12

    def set_time(self,hours,minutes,seconds,time_format):

        if self.__assign_format(time_format):                    
            time_format = time_format.upper()                    
            if self._is_valid_time(hours,minutes,seconds,time_format):   
                self._hours = hours
                self._minutes = minutes
                self._seconds = seconds
                self._time_format = time_format
                return True
        return False    
    
    def get_time(self):
         print(f"{self._hours}:{self._minutes:02d}:{self._seconds:02d} {self._time_format}")

    @classmethod                                         
    def from_strin(cls):                                 

        x = cls(0, 0, 0, "24 HOURS")                      

        while True:                                      
            try:                                         
                hora=int(input("Ingrese Hora:    "))
                minutes=int(input("Ingrese Minutos: "))
                segundos= int(input("Ingrese Segundos: "))
                formato= input("ingrese formato AM,PM,24 HOURS: ")   

                if x.set_time(hora,minutes,segundos,formato):       
                    return x                             
                print("Hora o formato no válidos")        

            except ValueError:                            
                print("error")

    @classmethod

    def get_time_count(cls):
        return cls.time_count


def main():                                                  # CAMBIO: fuera de la clase
    hora = None

    while True:
        print("\n--- MENÚ ---")
        print("1. Crear hora")
        print("2. Mostrar hora")
        print("3. Modificar hora")
        print("4. Número de horas creadas")
        print("0. Salir")
        opcion = input("Elija una opción: ")

        if opcion == "1":
            hora = Time.from_strin()

        elif opcion == "2":
            if hora is None:
                print("Primero cree una hora (opción 1)")
            else:
                hora.get_time()

        elif opcion == "3":
            if hora is None:
                print("Primero cree una hora (opción 1)")
            else:
                try:
                    h = int(input("Ingrese Hora:    "))
                    m = int(input("Ingrese Minutos: "))
                    s = int(input("Ingrese Segundos: "))
                    f = input("Ingrese formato AM,PM,24 HOURS: ")
                    if hora.set_time(h, m, s, f):
                        print("Hora modificada")
                    else:
                        print("Hora o formato no válidos")
                except ValueError:
                    print("Error: introduzca números enteros")

        elif opcion == "4":
            print("Horas creadas:", Time.get_time_count())

        elif opcion == "0":
            print("Hasta luego")
            break

        else:
            print("Opción no válida")



if __name__ == "__main__":
    main()


    
