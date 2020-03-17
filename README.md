# airflow

Choose your auth type:

1. db
2. ldap

## Database auth

1. Start docker containers:

   `docker-compose -f airflow-CeleryExecutor-db-auth.yml up`

2. Run init.sh to create admin user (admin/admin credentials)

3. Enjoy airflow and its RBAC menus.

## LDAP auth

Image [osixia/openldap](https://github.com/osixia/docker-openldap) is going to be used as LDAP server.

1. Start docker containers:

   `docker-compose -f airflow-CeleryExecutor-ldap-auth.yml up`

2. Populate LDAP with some data from your localhost (connecting to docker opened port, 3890):

  `ldapadd -Z -H ldap://localhost:3890 -D "cn=admin,dc=example,dc=org" -w admin -f ./ldif/users.ldif`

  Test with:
  
  `ldapsearch -x -H ldap://localhost:3890 -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin -s sub "(objectclass=*)"`
  `ldapsearch -x -H ldap://localhost:3890 -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin -s sub "(&(objectclass=groupOfNames)(cn=admins))"`
