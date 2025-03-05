# EntityMetadataParams

Specifies the parameters to associate metadata with entities in the entity hierarchy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**AwsEntityMetadata**](AwsEntityMetadata.md) |  | [optional] 
**azure_params** | [**AzureEntityMetadata**](AzureEntityMetadata.md) |  | [optional] 
**entity_id** | **int** | Specifies the entity id of the entity whose metadata is being updated. | 
**maintenance_mode_config** | [**MaintenanceModeConfig**](MaintenanceModeConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.entity_metadata_params import EntityMetadataParams

# TODO update the JSON string below
json = "{}"
# create an instance of EntityMetadataParams from a JSON string
entity_metadata_params_instance = EntityMetadataParams.from_json(json)
# print the JSON string representation of the object
print(EntityMetadataParams.to_json())

# convert the object into a dict
entity_metadata_params_dict = entity_metadata_params_instance.to_dict()
# create an instance of EntityMetadataParams from a dict
entity_metadata_params_from_dict = EntityMetadataParams.from_dict(entity_metadata_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


