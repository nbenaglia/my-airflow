# https://github.com/marcospereirampj/python-keycloak

from keycloak import KeycloakOpenID

# Configure client
keycloak_openid = KeycloakOpenID(server_url="http://keycloak:9090/auth/",
                    client_id="airflow",
                    realm_name="example",
                    client_secret_key="387baaa8-24b5-42e9-87a9-7e0de8b1c942",
                    verify=False)

# Get WellKnow
#config_well_know = keycloak_openid.well_know()

# Get Token
token = keycloak_openid.token("nbenaglia", "password")
#token = keycloak_openid.token("user", "password", totp="password")

# Get Userinfo
userinfo = keycloak_openid.userinfo(token['access_token'])
print(userinfo)

# # Refresh token
# token = keycloak_openid.refresh_token(token['refresh_token'])

# # Logout
#keycloak_openid.logout(token['refresh_token'])

# # Get Certs
#certs = keycloak_openid.certs()

# # Get RPT (Entitlement)
# token = keycloak_openid.token("nbenaglia", "password")
# rpt = keycloak_openid.entitlement(token['access_token'], "resource_id")

# # Instropect RPT
# token_rpt_info = keycloak_openid.introspect(keycloak_openid.introspect(token['access_token'], rpt=rpt['rpt'],
#                                      token_type_hint="requesting_party_token"))

# # Introspect Token
# token_info = keycloak_openid.introspect(token['access_token'])

# # Decode Token
# KEYCLOAK_PUBLIC_KEY = keycloak_openid.public_key()
# options = {"verify_signature": True, "verify_aud": True, "exp": True}
# token_info = keycloak_openid.decode_token(token['access_token'], key=KEYCLOAK_PUBLIC_KEY, options=options)

# # Get permissions by token
# token = keycloak_openid.token("nbenaglia", "password")
# keycloak_openid.load_authorization_config("example-authz-config.json")
# policies = keycloak_openid.get_policies(token['access_token'], method_token_info='decode', key=KEYCLOAK_PUBLIC_KEY)
# permissions = keycloak_openid.get_permissions(token['access_token'], method_token_info='introspect')

