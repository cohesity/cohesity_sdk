# UnregisterKerberosRequest

Specifies the request to unregister a Kerberos Provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**admin_password** | **str** | Specifies the password of Kerberos admin principal. | 
**admin_principal** | **str** | Specifies the name of the Kerberos admin principal. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.unregister_kerberos_request import UnregisterKerberosRequest

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterKerberosRequest from a JSON string
unregister_kerberos_request_instance = UnregisterKerberosRequest.from_json(json)
# print the JSON string representation of the object
print(UnregisterKerberosRequest.to_json())

# convert the object into a dict
unregister_kerberos_request_dict = unregister_kerberos_request_instance.to_dict()
# create an instance of UnregisterKerberosRequest from a dict
unregister_kerberos_request_from_dict = UnregisterKerberosRequest.from_dict(unregister_kerberos_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


