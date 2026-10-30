# Voluntariado Activo

Proyecto de Ingeniería Web hecho con Django. Es una web con oportunidades de voluntariado
para estudiantes de la universidad, ordenadas por causa y por entidad.

## Como arrancarlo

En Windows se puede hacer doble clic en `arrancar.bat`. Si no:

```bash
pip install -r requirements.txt
python manage.py runserver
```

Y abrir http://127.0.0.1:8000/

La base de datos (`db.sqlite3`) ya tiene los datos de prueba: 7 causas, 9 entidades y
17 oportunidades. Tambien tiene un usuario para entrar al admin (http://127.0.0.1:8000/admin/):

- usuario: `admin`
- contraseña: `admin1234`

Si se borra la base de datos, se puede volver a crear con:

```bash
python manage.py migrate
python manage.py loaddata datos_iniciales
python manage.py createsuperuser
```

## Estructura

- `voluntariado/models.py`: los modelos Causa, Entidad y Oportunidad. Cada oportunidad tiene
  una causa (FK) y puede tener varias entidades (ManyToMany).
- `voluntariado/admin.py`: configuracion del admin (columnas, filtros y busqueda).
- `voluntariado/views.py`: la portada y las vistas de lista y detalle (ListView y DetailView).
- `voluntariado/urls.py`: las URLs de la app.
- `voluntariado/templates/voluntariado/`: las plantillas. Hay tres niveles:
  `base.html` con la cabecera, el menu y el pie; `base_listado.html` y `base_detalle.html`
  que heredan de base; y las paginas de cada modelo que heredan de esas dos.
  `_tarjeta_oportunidad.html` es un trozo que se reutiliza con include.
- `voluntariado/static/voluntariado/css/estilos.css`: los estilos.
- `voluntariado/fixtures/datos_iniciales.json`: los datos de prueba.

## URLs

| URL | Pagina |
|---|---|
| `/` | Portada |
| `/oportunidades/` y `/oportunidades/<id>/` | Lista y detalle de oportunidades |
| `/causas/` y `/causas/<id>/` | Lista y detalle de causas |
| `/entidades/` y `/entidades/<id>/` | Lista y detalle de entidades |
| `/admin/` | Admin de Django |
