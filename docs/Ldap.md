# Ldap

Specifies an LDAP.

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
**id** | **int** | Specifies the LDAP id. | [optional] 
**tenant_id** | **str** | Specifies the LDAP tenant id. | [optional] 

## Example

```python
from cohesity_sdk.models.ldap import Ldap

# TODO update the JSON string below
json = "{}"
# create an instance of Ldap from a JSON string
ldap_instance = Ldap.from_json(json)
# print the JSON string representation of the object
print(Ldap.to_json())

# convert the object into a dict
ldap_dict = ldap_instance.to_dict()
# create an instance of Ldap from a dict
ldap_from_dict = Ldap.from_dict(ldap_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


