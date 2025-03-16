# UnregisterKerberosProvider

Response of Unregister Kerberos Provider.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | A status message returned upon unregistering. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.unregister_kerberos_provider import UnregisterKerberosProvider

# TODO update the JSON string below
json = "{}"
# create an instance of UnregisterKerberosProvider from a JSON string
unregister_kerberos_provider_instance = UnregisterKerberosProvider.from_json(json)
# print the JSON string representation of the object
print(UnregisterKerberosProvider.to_json())

# convert the object into a dict
unregister_kerberos_provider_dict = unregister_kerberos_provider_instance.to_dict()
# create an instance of UnregisterKerberosProvider from a dict
unregister_kerberos_provider_from_dict = UnregisterKerberosProvider.from_dict(unregister_kerberos_provider_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


