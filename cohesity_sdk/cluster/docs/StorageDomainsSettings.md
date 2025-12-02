# StorageDomainsSettings

Specifies storage domain related settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**allow_view_and_template_creation_in_optimized_sd** | **bool** | Specifies whether creation of views, templates inside throughput-optimized Storage Domains is allowed. | 
**throughput_optimized_sd_enabled** | **bool** | Indicates whether throughput-optimized Storage Domains are enabled. | 

## Example

```python
from cohesity_sdk.cluster.models.storage_domains_settings import StorageDomainsSettings

# TODO update the JSON string below
json = "{}"
# create an instance of StorageDomainsSettings from a JSON string
storage_domains_settings_instance = StorageDomainsSettings.from_json(json)
# print the JSON string representation of the object
print(StorageDomainsSettings.to_json())

# convert the object into a dict
storage_domains_settings_dict = storage_domains_settings_instance.to_dict()
# create an instance of StorageDomainsSettings from a dict
storage_domains_settings_from_dict = StorageDomainsSettings.from_dict(storage_domains_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


