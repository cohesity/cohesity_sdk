# RegisterOrUpdateKerberosProviderRequest

Specifies the request to register or update a Kerberos Provider.

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
**admin_password** | **str** | Specifies the password of Kerberos admin principal. | 
**admin_principal** | **str** | Specifies the name of the Kerberos admin principal. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.register_or_update_kerberos_provider_request import RegisterOrUpdateKerberosProviderRequest

# TODO update the JSON string below
json = "{}"
# create an instance of RegisterOrUpdateKerberosProviderRequest from a JSON string
register_or_update_kerberos_provider_request_instance = RegisterOrUpdateKerberosProviderRequest.from_json(json)
# print the JSON string representation of the object
print(RegisterOrUpdateKerberosProviderRequest.to_json())

# convert the object into a dict
register_or_update_kerberos_provider_request_dict = register_or_update_kerberos_provider_request_instance.to_dict()
# create an instance of RegisterOrUpdateKerberosProviderRequest from a dict
register_or_update_kerberos_provider_request_from_dict = RegisterOrUpdateKerberosProviderRequest.from_dict(register_or_update_kerberos_provider_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


