# airflow

1. Start docker containers:

   `docker-compose -f airflow-CeleryExecutor.yml up`

2. Populate LDAP with some data:

  `ldapadd -Z -H ldap://localhost:3890 -D "cn=admin,dc=example,dc=org" -w admin -f ./ldif/users.ldif`
