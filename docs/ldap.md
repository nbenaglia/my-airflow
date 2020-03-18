# LDAP auth

Image [osixia/openldap](https://github.com/osixia/docker-openldap) is going to be used as LDAP server.

1. Start docker containers:

   `docker-compose -f airflow-CeleryExecutor-ldap-auth.yml up`

2. Populate LDAP with some data from your localhost (connecting to docker opened port, 3890):

  `ldapadd -Z -H ldap://localhost:3890 -D "cn=admin,dc=example,dc=org" -w admin -f ./data/ldif/users.ldif`

  Test with:
  
  `ldapsearch -x -H ldap://localhost:3890 -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin -s sub "(objectclass=*)"`
  `ldapsearch -x -H ldap://localhost:3890 -b dc=example,dc=org -D "cn=admin,dc=example,dc=org" -w admin -s sub "(&(objectclass=groupOfNames)(cn=admins))"`

## References

- [enable memberOf](https://www.adimian.com/blog/2014/10/how-to-enable-memberof-using-openldap)
