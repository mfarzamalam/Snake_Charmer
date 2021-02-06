############# importing whole module 
import pizza

pizza.pizza_order(18,'pepparoni','extra cheese','green peppers','extra ketchup')
pizza.pizza_order(12,'pepparoni','extra cheese','green peppers','extra ketchup')


############# importing a specific funtion from a module
from pizza import sandwich
sandwich('chicken','beef','narcotics')


############# importing a specifc function from a module and give it an alias
from pizza import pizza as pi
pi('pepparoni','extra cheese','green peppers','extra ketchup')


############# importing all the functions from a module by using asterik
from pizza import *