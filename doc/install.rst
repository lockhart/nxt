.. _install chapter:

************
Installation
************

Download and install Anaconda.

Create a local conda environment::

  conda create -n nxt --file config/conda.txt
  conda activate nxt

Install packages from pip which are not in the conda repositories::

  pip install -r config/pip.txt

Install bootstrap from
`https://getbootstrap.com/docs/5.0/getting-started/download/
<https://getbootstrap.com/docs/5.0/getting-started/download/>`_.

Install PostgreSQL.

TBD

Create PostgreSQL user and database.

Define environment variables for the next steps::

  export PGHOST=localhost
  export PGPORT=5432
  export PGDATA=/opt/local/var/db/postgresql14/defaultdb

Create a PostgreSQL superuser.

  createuser nxt

Create a Django DB instance::

  createdb nxt
  cd nxt
  ./manage.py createsuperuser
  ./manage.py migrate
  ./manage.py runserver 8000

