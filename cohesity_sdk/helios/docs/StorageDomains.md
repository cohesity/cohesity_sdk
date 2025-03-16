# StorageDomains

Specifies a list of Storage Domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**storage_domains** | [**List[StorageDomain]**](StorageDomain.md) | Specifies the list of storage domains. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.storage_domains import StorageDomains

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDomains from a JSON string
storage_domains_instance = StorageDomains.from_json(json)
# print the JSON string representation of the object
print(StorageDomains.to_json())

# convert the object into a dict
storage_domains_dict = storage_domains_instance.to_dict()
# create an instance of StorageDomains from a dict
storage_domains_from_dict = StorageDomains.from_dict(storage_domains_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


