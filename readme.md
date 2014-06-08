UltimaDjango es una configuración básica mejorada de Django

Repositorio

    -> read.me
    -> git.ignore
    -> REQUIREMENTS
        -> base.txt
        -> local.txt
        -> produccion.txt
        -> staging.txt
    ->PROYECTO
        -> apps
            -> app_1
            -> app_2
        -> media
        -> static
            -> css
            -> js
            -> img
        -> templates
            -> app_1
            -> app_2
        -> manage.py
        -> PROYECTO
            ->urls.py
            ->wsgi.py
            ->SETTINGS
                -> local.py
                -> base.py
                -> production.py
                -> staging.py
                
                

La Carpeta REQUIREMENTS contiene las dependencias de cada ambiente de trabajo.
De esta manera tenemos un sistema de fácil instalacion de dependencias.
Ejemplo:

        pip install -r REQUIREMENTS/local.txt
        local.txt:
            -r base.txt
        base.txt:
            Django==1.6.5
            Pillow==2.4.0
            Unipath==1.0
            psycopg2==2.5.2

El archivo settings.py lo he dividio en los archivos que contienen la Carpeta SETTINGS.
De esta manera puedo camviar el ambiente trabajo sólo llamando al runserser:
Ejemplo:

    python manage.py runserser --settings=PROYECTO.settings.local
    base.py:
    
He dividido las INSTALLED_APPS en 3 tuplas para tenerlo mejor organizado:

    INSTALLED_APPS = DJANGO_APPS + THIRD_PARTY_APPS + LOCAL_APPS
He usado Unipath para llamar al directorio de TEMPLATES_DIR
