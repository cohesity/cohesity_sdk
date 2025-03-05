# EntityExternalMetadata

Specifies the External metadata of an entity

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**maintenance_mode_config** | [**MaintenanceModeConfig**](MaintenanceModeConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.entity_external_metadata import EntityExternalMetadata

# TODO update the JSON string below
json = "{}"
# create an instance of EntityExternalMetadata from a JSON string
entity_external_metadata_instance = EntityExternalMetadata.from_json(json)
# print the JSON string representation of the object
print(EntityExternalMetadata.to_json())

# convert the object into a dict
entity_external_metadata_dict = entity_external_metadata_instance.to_dict()
# create an instance of EntityExternalMetadata from a dict
entity_external_metadata_from_dict = EntityExternalMetadata.from_dict(entity_external_metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


