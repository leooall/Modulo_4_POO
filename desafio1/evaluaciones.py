from pizza import Pizza

#a #imprime atributos de clase tamaño y precio 
print(Pizza.tamaño, Pizza.precio) 

#b Si el elemento está presente en la lista posibles_valores, el método devuelve True; de lo contrario, devuelve False
print(Pizza.validar_elemento("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

#c crea una instancia de Pizza, solicita al usuario que ingrese valores sobre una pizza y luego valida esos valores
pizza =Pizza()
pizza.realizar_pedido()

#d muestra los ingredientes de la pizza ingresados por el usuario y si la combinación de ingredientes es válida según las validaciones realizadas en el método realizar_pedido()
print(pizza.vegetales, pizza.proteicos,pizza.masas)
print(f"la validacion es {pizza.pizza_valida}") 

#e
print(Pizza.pizza_valida)# falla porque es pizza_valida es un atributo de instancia