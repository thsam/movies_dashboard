# movies_dashboard
Descargar dataset: https://www.kaggle.com/dm4006/amazon-movie-reviews
## REQUERIMIENTO
Desarrollar una aplicación web sin autenticación que muestre la siguiente información respecto a los datos.
Los datos deben ser consumidos de una base de datos persistente (ejemplo: MySql, PostgreSQL, otros) y
mostrados en un dashboard, todos los resultados deben obedecer a filtros elegidos por el usuario.
### Fuente de datos:
1. Guardar los data sets en una base de datos persistente de su preferencia.
### Filtros:
1. Rango de fechas.
2. Búsqueda de una película.
3. Búsqueda de usuarios.
#### Indicadores según la selección de filtros:
1. Cantidad usuarios.
2. Máximo y Mínimo score value.
3. Promedio score value.
#### Tablas según la selección de filtros:
1. Top 10 de mejores score. (Mostrar todos los datos de los score)
2. Top 10 de peores score. (Mostrar todos los datos de los score)

#### Visualizaciones según la selección de filtros:
1. Línea de tiempo doble eje: fechas VS promedio de score y fechas VS promedio de
helpfulness

### Recomendaciones:
*  La aplicación debe tener la arquitectura cliente-servidor. Servidor en Django. (Backend)
* Debe consumir los datos guardados en la base. No usar el ORM de Django, lazar consultas mediante
SQL.
* Aplicar principios de Responsive Design, puede utilizar Django o cualquier otro framework de su
elección. (Frontend)
* Emplear librerías JavaScript de su elección para crear los gráficos y tablas.
## Desarrollo
* Se procesó el dataset y posteriormente se subieron los datos como migración a través de Django.
* Se utilizó MySQL, Django, Bootstrap y Chart.js.
![Screenshot](Front/dashboard_img.jpg)
