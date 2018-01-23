# Evaluación - Notas

- Te dejaste un "fi" (supongo que de la traducción de un script bash) dentro del archivo
- No se uso docker para hacer provisioning, sino make.
- El proyecto asume que la base de datos definida en el url de SQLAlchemy existe. Aún no usando docker, la base de datos debería crearse automáticamente con make run. 
- make run no funciona por defecto porque hace falta activar la extension postgis (``CREATE EXTENSION postgis;``)

Una vez arreglado esto va perfectamente.

Cosas buenas:

* +3 usando manager de FLASK para las operaciones del backend
* +3 flask_jwt para login
* +3 ORM (sqlalchemy) para base de datos
* +3 Buena estructura de archivos
* +3 blueprints para URLs
* +2 separación modelado vs serialización
* +1 el planteamiento del docker file podría haber sido válido para el servidor (usando)
el ``Makefile``. Sin embargo lo suyo era usar un contenedor para la base de datos y otro
para el servidor con un link.

Cosas que hubieran estado bien

* +0 marshmallow para serialización 
* +0 usar docker-compose con separación de containers
* +0 No se realiza ningna operación geométrica a nivel de base datos.

Cosas no tan buenas:

* -1 los parámetros ``<QUERY>`` (como en /api/postal_codes/<QUERY>) no están documentados. De hecho,
mirando ``database.converters.Postals_converter`` parece que no se usan.
* -1 algunos problemas de indentación, spacios mezclados con tabulación
* -2 make vs docker
* -2 Por algún motivo, los postprocessors definidos ``app.initialize_api`` no se llaman y los
endpoints devuelven error de que el WKB no se puede serializar. Los dos endpoints fallan pues.
```bash
127.0.0.1 - - [23/Jan/2018 17:24:14] "GET /api/paystats HTTP/1.1" 500 -
Traceback (most recent call last):
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1997, in __call__
    return self.wsgi_app(environ, start_response)
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1985, in wsgi_app
    response = self.handle_exception(e)
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1540, in handle_exception
    reraise(exc_type, exc_value, tb)
  File "venv/lib/python3.6/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1982, in wsgi_app
    response = self.full_dispatch_request()
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1614, in full_dispatch_request
    rv = self.handle_user_exception(e)
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1517, in handle_user_exception
    reraise(exc_type, exc_value, tb)
  File "venv/lib/python3.6/site-packages/flask/_compat.py", line 33, in reraise
    raise value
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1612, in full_dispatch_request
    rv = self.dispatch_request()
  File "venv/lib/python3.6/site-packages/flask/app.py", line 1598, in dispatch_request
    return self.view_functions[rule.endpoint](**req.view_args)
  File "venv/lib/python3.6/site-packages/flask_restless/views.py", line 157, in decorator
    return func(*args, **kw)
  File "venv/lib/python3.6/site-packages/mimerender.py", line 265, in wrapper
    content = renderer(**result)
  File "venv/lib/python3.6/site-packages/flask_restless/views.py", line 303, in jsonpify
    response = jsonify(*args, **kw)
  File "venv/lib/python3.6/site-packages/flask_restless/views.py", line 219, in jsonify
    response = _jsonify(*args, **kw)
  File "venv/lib/python3.6/site-packages/flask/json.py", line 263, in jsonify
    (dumps(data, indent=indent, separators=separators), '\n'),
  File "venv/lib/python3.6/site-packages/flask/json.py", line 123, in dumps
    rv = _json.dumps(obj, **kwargs)
  File "/usr/lib64/python3.6/json/__init__.py", line 238, in dumps
    **kw).encode(obj)
  File "/usr/lib64/python3.6/json/encoder.py", line 201, in encode
    chunks = list(chunks)
  File "/usr/lib64/python3.6/json/encoder.py", line 430, in _iterencode
    yield from _iterencode_dict(o, _current_indent_level)
  File "/usr/lib64/python3.6/json/encoder.py", line 404, in _iterencode_dict
    yield from chunks
  File "/usr/lib64/python3.6/json/encoder.py", line 325, in _iterencode_list
    yield from chunks
  File "/usr/lib64/python3.6/json/encoder.py", line 404, in _iterencode_dict
    yield from chunks
  File "/usr/lib64/python3.6/json/encoder.py", line 404, in _iterencode_dict
    yield from chunks
  File "/usr/lib64/python3.6/json/encoder.py", line 437, in _iterencode
    o = _default(o)
  File "venv/lib/python3.6/site-packages/flask/json.py", line 80, in default
    return _json.JSONEncoder.default(self, o)
  File "/usr/lib64/python3.6/json/encoder.py", line 180, in default
    o.__class__.__name__)
TypeError: Object of type 'WKBElement' is not JSON serializable
```
* -4 Con los endpoints implementados, no se pueden implementar todos los widgets provistos. Salvo
que me equivoque en la lectura, se podría dibujar el mapa de coropletas y los popups sobre ellos,
pero no los widgets de agregados totales de la izquierda.
  
