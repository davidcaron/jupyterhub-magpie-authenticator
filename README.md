# Magpie JupyterHub Authenticator

Magpie authenticator for [JupyterHub](http://github.com/jupyter/jupyterhub/)
that allows allows login using Magpie credentials with the default ziggurat provider.

## Demonstration

Configure the `c.MagpieAuthenticator.magpie_url` url in `docker/jupyterhub_config.py`
to point to a running instance of Magpie, then:

```
cd docker
docker-compose up -d
```

Go to the jupyterhub url (`http://localhost`) and try to login using magpie credentials.

If there is an error, check the docker logs.

### Note

Installed directly in the jupyterhub docker image here: https://github.com/ouranosinc/jupyterhub
