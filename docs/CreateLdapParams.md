# CreateLdapParams

Specifies the parameters to create an LDAP.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**active_directory_id** | **int** | Specifies the Active Directory id which is mapped to this LDAP. | [optional] 
**ad_domain_name** | **str** | Specifies the domain name of an Active Directory which is mapped to this LDAP provider | [optional] 
**attribute_common_name** | **str** | Specifies name of the LDAP attribute used for common name of an object. | [optional] 
**attribute_gid** | **str** | Specifies name of the attribute used to lookup unix GID of an LDAP user. | [optional] 
**attribute_member_of** | **str** | Specifies name of the LDAP attribute used to lookup members of a group. | [optional] 
**attribute_uid** | **str** | Specifies name of the attribute used to lookup unix UID of an LDAP user. | [optional] 
**attribute_username** | **str** | Specifies name of the LDAP attribute used to lookup a user by user ID. | [optional] 
**auth_type** | **str** | Specifies the LDAP authentication type. | 
**base_distinguished_name** | **str** | Specifies the base distinguished name used as the base for LDAP search requests. | 
**domain_name** | **str** | Specifies the name of the domain name to be used for querying LDAP servers from DNS. | [optional] 
**name** | **str** | Specifies the LDAP name. | 
**object_class_group** | **str** | Specifies name of the LDAP group object class for user accounts. | [optional] 
**object_class_user** | **str** | Specifies name of the LDAP user object class for user accounts. | [optional] 
**port** | **int** | Specifies the LDAP server port. | [optional] 
**preferred_ldap_servers** | **List[str]** | Specifies a list of preferred LDAP servers. Servers should either be FQDNs or IP addresses. | [optional] 
**simple_auth_params** | [**SimpleAuthParams**](SimpleAuthParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.create_ldap_params import CreateLdapParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateLdapParams from a JSON string
create_ldap_params_instance = CreateLdapParams.from_json(json)
# print the JSON string representation of the object
print(CreateLdapParams.to_json())

# convert the object into a dict
create_ldap_params_dict = create_ldap_params_instance.to_dict()
# create an instance of CreateLdapParams from a dict
create_ldap_params_from_dict = CreateLdapParams.from_dict(create_ldap_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


