tarea_1= {"nombre": "proyecto 1",
          "descripcion": "presentar informe del estado del proyecto",
          "estado": "intermedio"}

tarea_2 ={"nombre": "aires del beagle",
          "descripcion": "presentar maqueta de finalizacion",
          "estado": "avanzado"}

tarea_3 ={"nombre": "el faro",
          "descripcion": "entregar carpeta con proyecto original",
          "estado": "inicial"}


lista_tareas = []
lista_tareas.insert(0, tarea_1)
lista_tareas.insert(1, tarea_2)
lista_tareas.insert(2, tarea_3)
print("El listado de tareas es: ", lista_tareas)


lista_tareas.pop(1)
print ("El listado de tareas pendientes es: ", lista_tareas[0:2])




