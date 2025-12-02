# StorageDomainConfig

Specifies a Storage Domain config. This contains the storage domain ids and names on the Primary Cluster and the Vault Cluster. The storage domain on the Primary Cluster is referred as Primary Domain, and the storage domain on the Vault Cluster is referred as Vault Domain. It also contains the vaulting window between the two domains.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_domain_id** | **int** | Specifies the Storage Domain id on the Primary Cluster. | 
**primary_domain_name** | **str** | Specifies the Storage Domain name on the Primary Cluster. | [optional] 
**vault_domain_id** | **int** | Specifies the Storage Domain id on the Vault Cluster. | 
**vault_domain_name** | **str** | Specifies the Storage Domain name on the Primary Cluster. | [optional] 
**vaulting_window_config** | [**VaultingWindowConfig**](VaultingWindowConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.storage_domain_config import StorageDomainConfig

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDomainConfig from a JSON string
storage_domain_config_instance = StorageDomainConfig.from_json(json)
# print the JSON string representation of the object
print(StorageDomainConfig.to_json())

# convert the object into a dict
storage_domain_config_dict = storage_domain_config_instance.to_dict()
# create an instance of StorageDomainConfig from a dict
storage_domain_config_from_dict = StorageDomainConfig.from_dict(storage_domain_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


