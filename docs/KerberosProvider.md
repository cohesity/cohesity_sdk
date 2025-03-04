# KerberosProvider

Specifies the the Kerberos Provider details.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_server** | **str** | Specifies the admin server used for registration from the list of KDC servers. | 
**host_alias** | **List[str]** | Specifies the DNS routable host alias names. | 
**id** | **str** | Specifies the id. | [optional] [readonly] 
**kdc_servers** | **List[str]** | Specifies a list of Key distribution Centre(KDC) Severs. | 
**ldap_provider_id** | **int** | Specifies the LDAP provider id to be mapped | [optional] 
**overwritehost_alias** | **bool** | Specifies if specified host alias should overwrite existing host alias. | [optional] 
**realm_name** | **str** | Specifies the realm name. | 

## Example

```python
from cohesity_sdk.models.kerberos_provider import KerberosProvider

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosProvider from a JSON string
kerberos_provider_instance = KerberosProvider.from_json(json)
# print the JSON string representation of the object
print(KerberosProvider.to_json())

# convert the object into a dict
kerberos_provider_dict = kerberos_provider_instance.to_dict()
# create an instance of KerberosProvider from a dict
kerberos_provider_from_dict = KerberosProvider.from_dict(kerberos_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


