# Switch Manager

Este es el repositorio central de la aplicación Switch Manager.

Los componentes de la misma están concentrados en 4 repositorios
independientes:

1. `sm-api`: API para la interacción entre los clientes y AWX.
2. `sm-dashboard`: Dashboard para la administración de la aplicación.
3. `sm-infrastructure`: Archivos, scripts, y playbooks necesarios para levantar
   ambientes de producción y testing de la aplicación.
4. `sm-playbooks`: Playbooks que consume el AWX para interactuar con los
   equipos de red de los clientes.

Para simplificar la gestíon de estos proyectos se utilizará la herramienta
[`meta`](https://github.com/mateodelnorte/meta). Para utilizarla, es necesario
instalarla con `npm`.

```bash
npm install -g meta
```

Luego, clonamos este repositorio:

```bash
git clone https://github.com/conatel-i-d/sm
```

Y corremos `meta git clone` para descargar el código de todos los repositorios
que componen el proyecto.

```bash
meta git clone
```

Para correr un ambiente de desarrollo, es necesario crear un archivo llamado
`secret.yml` con las variables de Ansible correspondientes. Luego, ejecutar la
tarea `make dev`.

El mismo procedimiento es necesario para levantar un ambiente de producción, la
única diferencia siendo el nombre de la tarea: `make deploy`.
