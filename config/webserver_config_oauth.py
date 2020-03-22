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
# from flask_appbuilder.security.manager import AUTH_LDAP
from flask_appbuilder.security.manager import AUTH_OAUTH
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
AUTH_TYPE = AUTH_OAUTH

# Uncomment to setup Full admin role name
AUTH_ROLE_ADMIN = 'Admin'

# Uncomment to setup Public role name, no authentication needed
# AUTH_ROLE_PUBLIC = 'Public'

# Will allow user self registration
AUTH_USER_REGISTRATION = True

# The default user self registration role
AUTH_USER_REGISTRATION_ROLE = "Admin"

# When using OAuth Auth, uncomment to setup provider(s) info
OAUTH_PROVIDERS = [{
	'name':'example',
    'whitelist': ['@example'],  # optional
    'token_key':'access_token',
    'icon':'fa-key',
        'remote_app': {
            'base_url':'http://keycloak:9090',
            'request_token_params':{
                'scope': 'email profile'
            },
            'access_token_url':'http://keycloak:9090/auth/realms/example/protocol/openid-connect/token',
            'authorize_url':'http://keycloak:9090/auth/realms/example/protocol/openid-connect/auth',
            'request_token_url': 'http://keycloak:9090/auth/realms/example/protocol/openid-connect/token',
            'consumer_key': "airflow",
            'consumer_secret': "387baaa8-24b5-42e9-87a9-7e0de8b1c942"
        }
}]

# When using OpenID Auth, uncomment to setup OpenID providers.
# example for OpenID authentication
OPENID_PROVIDERS = [
   { 'name': 'Yahoo', 'url': 'https://me.yahoo.com' },
   { 'name': 'AOL', 'url': 'http://openid.aol.com/<username>' },
   { 'name': 'Flickr', 'url': 'http://www.flickr.com/<username>' },
   { 'name': 'MyOpenID', 'url': 'https://www.myopenid.com' },
   { 'name': 'keycloak', 'url': 'http://keycloak:9090/auth/realms/example' }]
