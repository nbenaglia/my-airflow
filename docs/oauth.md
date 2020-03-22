# OAUTH

Airflow docker image must have `Flask-OAuthlib` in PYTHON_DEPS.

We need an OAuth server and we'll use [keycloak](https://www.keycloak.org/).

I have already configured an example.org realm and we need to import into keycloak.

If we use the GUI to do the import operation, we'll get this error:

`ERROR [org.keycloak.services.error.KeycloakErrorHandler] (default task-3) Uncaught server error: java.lang.RuntimeException: Script upload is disabled`

Because (from keycloak docs) "Ability to upload scripts through the admin console is deprecated and will be removed in a future version of Keycloak."

We need to execute the following command from inside the container:

Import:

```
/opt/jboss/keycloak/bin/standalone.sh \
-Djboss.socket.binding.port-offset=100 \
-Dkeycloak.migration.action=import \
-Dkeycloak.profile.feature.upload_scripts=enabled \
-Dkeycloak.migration.provider=singleFile \
-Dkeycloak.migration.file=/etc/settings/import_realm.json
```

Export:

```
/opt/jboss/keycloak/bin/standalone.sh \
-Djboss.socket.binding.port-offset=100 \
-Dkeycloak.migration.action=export \
-Dkeycloak.migration.provider=singleFile \
-Dkeycloak.migration.realmName=example.org \
-Dkeycloak.migration.usersExportStrategy=REALM_FILE \
-Dkeycloak.migration.file=/tmp/import_realm.json
```

Airflow client in keycloak:

`airflow` with secret `387baaa8-24b5-42e9-87a9-7e0de8b1c942`

## TLS

openssl req \
       -newkey rsa:2048 -nodes -keyout tls.key \
       -x509 -days 365 -out tls.crt
