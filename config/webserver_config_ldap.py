# -*- coding: utf-8 -*-
#
# Licensed to the Apache Software Foundation (ASF) under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  The ASF licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#   http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing,
# software distributed under the License is distributed on an
# "AS IS" BASIS, WITHOUT WARRANTIES OR CONDITIONS OF ANY
# KIND, either express or implied.  See the License for the
# specific language governing permissions and limitations
# under the License.

import os
from airflow import configuration as conf
# from flask_appbuilder.security.manager import AUTH_DB
from flask_appbuilder.security.manager import AUTH_LDAP
# from flask_appbuilder.security.manager import AUTH_OAUTH
# from flask_appbuilder.security.manager import AUTH_OID
# from flask_appbuilder.security.manager import AUTH_REMOTE_USER
basedir = os.path.abspath(os.path.dirname(__file__))

# The SQLAlchemy connection string.
SQLALCHEMY_DATABASE_URI = conf.get('core', 'SQL_ALCHEMY_CONN')

# Flask-WTF flag for CSRF
CSRF_ENABLED = True

FAB_API_SWAGGER_UI = True  # See swagger at /swaggerview/v1

# ----------------------------------------------------
# AUTHENTICATION CONFIG
# ----------------------------------------------------
# For details on how to set up each of the following authentication, see
# http://flask-appbuilder.readthedocs.io/en/latest/security.html# authentication-methods
# for details.

# The authentication type
# AUTH_OID : Is for OpenID
# AUTH_DB : Is for database
# AUTH_LDAP : Is for LDAP
# AUTH_REMOTE_USER : Is for using REMOTE_USER from web server
# AUTH_OAUTH : Is for OAuth
AUTH_TYPE = AUTH_LDAP

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Admin"

# When using LDAP Auth, setup the ldap server
AUTH_LDAP_SERVER = "ldap://ldap:389"
AUTH_LDAP_USE_TLS = False
AUTH_LDAP_ALLOW_SELF_SIGNED = True
AUTH_LDAP_SEARCH = 'dc=example,dc=org'
# AUTH_LDAP_SEARCH_FILTER = '(memberOf=cn=admins,ou=groups,dc=example,dc=org)'   # it appends the uid of the logging user and the query doesn't work.
AUTH_LDAP_FIRSTNAME_FIELD = 'cn'
AUTH_LDAP_LASTNAME_FIELD = 'sn'
AUTH_LDAP_EMAIL_FIELD = 'mail'
AUTH_LDAP_UID_FIELD = 'uid'
AUTH_LDAP_BIND_USER = "cn=admin,dc=example,dc=org"
AUTH_LDAP_BIND_PASSWORD = "admin"
#AUTH_LDAP_TLS_CACERTFILE = '/etc/ca/ca_bundle.crt'
