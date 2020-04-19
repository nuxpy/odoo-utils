### otoolsdev

Script para crear estructura de desarrollo de módulos o aplicaciones _Odoo_.

<a href="https://wiki.nuxpy.com/index.php/Odoo_utils">Información general del <i>script</i></a>

### Descripción

La idea de estos _scripts_ es crear un ambiente de programación de módulos, vistas y modelos en Odoo con una estructura estándar, se cargan ciertos parámetros más usados, si el programador desea puede agregar o quitar los parámetros que requiera en determinado momento.

Estos scripts están diseñados para usar sobre ambientes de distribuciones _Linux_.

### Descarga y configuración

El código fuente se puede descargar desde el repositorio.

Luego de descargado, se puede configurar de la siguiente manera, como usuario root:

* Se copian los dos archivos olibdevs.py y otoolsdev.py en un directorio llamado otoolsdev en un sitio donde no se borren accidentalmente. Ejemplo **/opt/otoolsdev**
* Se debe tener permisos de ejecución: **chmod 755 /opt/otoolsdev -R**
* Se crea un enlace simbólico solo del fichero _otoolsdev.py_, puede ser ejemplo:
```
    ln -s /opt/otoolsdevs.py /usr/local/bin/otoolsdev
```

### Contenido

Fichero _olibdevs.py_ contiene el esquema de la estructura de aplicación o módulo Odoo, también provee del contenido que contendrá cada fichero principal de la estructura de la aplicación. Igualmente, suministra el contenido de ficheros para estructura de clases, modelos y vistas de los ficheros que se desean generar a la medida.

Son estructuras básicas para rellenar los ficheros y empezar con los datos mínimos requeridos.

Fichero _otoolsdev.py_ es el script funcional, con este se recoge la información que el usuario desarrollador desea implementar, captura las opciones las deduce y llama al fichero olibdevs.py para obtener los datos mínimos requeridos según las opciones seleccionadas.

### ¿Qué hace?

Este script genera un árbol básico de un módulo o aplicación para Odoo, igualmente permite crear ficheros de modelos heredados o nuevos, ficheros de vistas heredadas o nuevas.

La estructura base de una aplicación o módulo para Odoo es parecida a la siguiente:

    nombre_del_modulo
       .
       ├── data
       ├── i18n
       ├── __init__.py
       ├── __manifest__.py
       ├── models
       │   └── __init__.py
       ├── report
       ├── security
       │   └── ir.model.access.csv
       ├── static
       │   ├── description
       │   ├── img
       │   └── src
       │       ├── css
       │       ├── js
       │       └── less
       ├── test
       │   └── __init__.py
       ├── views
       └── wizard
           └── __init__.py

Los archivos principales se cargan con datos básicos, se deben modificar según los requerimientos.

### ¿Cómo se usa?

Inicialmente, para ver opciones de ayuda:

    otoolsdev -h

**Crear modelos**

Para crear un modelo se debe ingresar en el directorio donde será creado el fichero del modelo en cuestión, posteriormente se usa la siguiente instrucción: 

    otoolsdev -o sale.order -m inherit

Este comando genera un fichero según el objeto o modelo seleccionado, del ejemplo anterior, generaría un fichero: **sale_order.py**

Cabe destacar que se debe ir antes a la ruta donde irán dispuestos los modelos en la estructura de la aplicación o módulo Odoo. Ejemplo: **my_app/models**

**Crear modelos para un wizard**

La estructura de la clase de los wizards en Odoo es similar a la estructura de las clases para modelos o tablas estándares, sin embargo cambian algunas cosas, para crear dicha estructura se puede realizar de la siguiente manera:

    otoolsdev -w sale.order -m inherit

Dentro del directorio correspondiente de wizard en la aplicación.

**Crear vistas**

Esta instrucción es un poco más extendida, requiere pasar por parámetros tanto el objeto, modo y la vista que se desea crear, por ejemplo:

    otoolsdev --views=form,menu -m inherit -o sale.order

Si se desea crear todas las vistas, se puede usar el recurso all en el parámetro, por ejemplo:

    otoolsdev --views=all -m inherit -o sale.order

Esto permitirá crear una estructura de lo que pudiera tener un fichero vista completo en Odoo, luego se eliminan o agregan los elementos que realmente son requeridos. 

Autor
-----
Félix Urbina
