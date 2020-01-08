import os
from jupyter_client.localinterfaces import public_ips

# The docker instances need access to the Hub, so the default loopback port doesn't work:
c.JupyterHub.hub_ip = public_ips()[0]

c.JupyterHub.authenticator_class = 'jupyterhub_magpie_authenticator.MagpieAuthenticator'
c.MagpieAuthenticator.magpie_url = "https://www.example.com/magpie"

c.JupyterHub.spawner_class = 'dockerspawner.DockerSpawner'
c.DockerSpawner.use_internal_ip = True
c.DockerSpawner.network_name = 'jupyterhub_network'
c.DockerSpawner.remove = True

c.Authenticator.admin_users = {'admin'}
