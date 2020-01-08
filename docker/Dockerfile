FROM jupyterhub/jupyterhub:1.0.0

COPY . /jupyterhub_magpie_authenticator

RUN pip install dockerspawner jupyter_client /jupyterhub_magpie_authenticator

RUN rm -rf /jupyterhub_magpie_authenticator
