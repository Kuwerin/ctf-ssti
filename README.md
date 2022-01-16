# CTF SSTI task

The application requires Python3.10, packages are mentioned
in `requirements.txt`

## Application environment
You should specify some environment variables for the task:
### APP_HOST
The host name to run, default is `0.0.0.0`
### APP_PORT
The port number to run, default is `5000`
### APP_FLAG
Some application flag for task

To run this package on your PC, you should to perform an installation:

#### Installation:
```shell
python3.10 -m venv venv
source venv/bin/activate
export APP_FLAG={{YourFlag}}
pip install -r requirements.txt
```

#### Run locally:
python -u -m src

to run this app via `Docker`:

#### Run via Docker:
```shell
docker-compose -p ctf-ssti up --build
```

### There are also short aliases for both actions:

To run local:
```shell
make run
```

To run via Docker:

```shell
make docker-run
```

This application represents `Server-Side Template injection`
vulnerability of `Jinja2`. This is a modern template language for Python developers.

A server side template injection is a vulnerability that occurs when a server renders user input as a template of some sort.

In this task you have 3 routes:
* "/" -- root, which shows us a code in `transport/handler.py`
* "/hello" -- SSTI vulnerable page. This page accepts `username` as a request arg.
* "/answer" -- A page, which shows us a clue about that `Jinja2` is used for template rendering

To solve this task, you should pass some special payload to the server. Be prepared: there is also some middleware, that will abort some requests due certain payload.

More information about SSTI:
* https://pequalsnp-team.github.io/cheatsheet/flask-jinja2-ssti
* https://www.onsecurity.io/blog/server-side-template-injection-with-jinja2/