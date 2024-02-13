#!/usr/bin/env python
# coding: utf-8

# In[1]:


cena = float(input("Introduzca el precio de la cena"))
propina = float(input("Introduzca el porcentaje de propina a dejar"))
total = cena + propina
def calcular_propina(cena,propina):
    propina =  cena * propina/100
    return propina
def calcular_total(cena,propina):
    total = cena + propina
    return total
print("La propina a dejar es", propina)
print("El monto total es", total)


# In[66]:


coste_producto = float(input("Introduzca el precio del producto"))
impuestos = float(input("Introduzca cuanto se debe abonar por impuestos"))
cargos_envio = float(input("Introduzca los cargos de envio"))
total = (coste_producto + (impuestos) + (cargos_envio)) * 0.21 + coste_producto

def calcular_impuestos(impuestos,total):
    total = total + impuestos
    return impuestos
def calcular_precio_total(coste_producto,impuestos,cargos_envio):
    total = (coste_producto + impuestos + cargos_envio) 
    return total
print("El coste total es de ", total)


# In[55]:


131 * 0.21


# In[10]:


numero1 = 5
numero2 = 2
resultado = numero1 + numero2
print("La suma de los números es:" + str(resultado))
print("La multiplicación de los numero es:" + str(numero1 * numero2))
numeroa = input("Vamos a sumar 2 numeros.Introduce un número")
numerob = input("Vamos a sumar 2 numeros.Introduce un número")
print("La suma de los numero es: " + str(int(numeroa) + int(numerob)))


# In[11]:


numeroa = input("Vamos a sumar 2 numeros.Introduce un número")
numerob = input("Vamos a sumar 2 numeros.Introduce un número")
print("La suma de los numero es: " + str(int(numeroa) + int(numerob)))


# In[14]:


numero1 = 10
numero2 = 5
if numero1 < numero2:
    print("El numero2 es mayor")
else:
    print("El numero 1 es mayor")


# In[17]:


mi_lista = [1,2,3,4,5,6,7,8,9,10]
print("Mi lista es " + str(mi_lista))
for elemento in mi_lista:
    print("El doble de cada elemento de la lista es:" + str(elemento*2))


# In[ ]:


mi_lista = [1,2,3,4,5,6,7,8,9,10]
while (elemento)

