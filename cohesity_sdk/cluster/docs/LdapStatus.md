# LdapStatus

Specifies the LDAP connection status.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**connection_status** | **str** | Specifies the connection status. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ldap_status import LdapStatus

# TODO update the JSON string below
json = "{}"
# create an instance of LdapStatus from a JSON string
ldap_status_instance = LdapStatus.from_json(json)
# print the JSON string representation of the object
print(LdapStatus.to_json())

# convert the object into a dict
ldap_status_dict = ldap_status_instance.to_dict()
# create an instance of LdapStatus from a dict
ldap_status_from_dict = LdapStatus.from_dict(ldap_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


