# StorageDomainPair

Specifies a Storage Domain pair.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_storage_domain_id** | **int** | Specifies the local Storage Domain id. | 
**local_storage_domain_name** | **str** | Specifies the local Storage Domain name. | [optional] [readonly] 
**remote_storage_domain_id** | **int** | Specifies the remote Storage Domain id. | 
**remote_storage_domain_name** | **str** | Specifies the remote Storage Domain name. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.storage_domain_pair import StorageDomainPair

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDomainPair from a JSON string
storage_domain_pair_instance = StorageDomainPair.from_json(json)
# print the JSON string representation of the object
print(StorageDomainPair.to_json())

# convert the object into a dict
storage_domain_pair_dict = storage_domain_pair_instance.to_dict()
# create an instance of StorageDomainPair from a dict
storage_domain_pair_from_dict = StorageDomainPair.from_dict(storage_domain_pair_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


