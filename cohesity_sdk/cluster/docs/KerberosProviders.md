# KerberosProviders

Response of Kerberos Providers.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**kerberos_providers** | [**List[KerberosProvider]**](KerberosProvider.md) | A list of registered Kerberos Providers. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.kerberos_providers import KerberosProviders

# TODO update the JSON string below
json = "{}"
# create an instance of KerberosProviders from a JSON string
kerberos_providers_instance = KerberosProviders.from_json(json)
# print the JSON string representation of the object
print(KerberosProviders.to_json())

# convert the object into a dict
kerberos_providers_dict = kerberos_providers_instance.to_dict()
# create an instance of KerberosProviders from a dict
kerberos_providers_from_dict = KerberosProviders.from_dict(kerberos_providers_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


