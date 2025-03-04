# RecoverVolumeMapping

Specifies the mapping from a source volume to a destination volume.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**destination_volume_guid** | **str** | Specifies the guid of the destination volume. | 
**source_volume_guid** | **str** | Specifies the guid of the source volume. | 

## Example

```python
from cohesity_sdk.models.recover_volume_mapping import RecoverVolumeMapping

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverVolumeMapping from a JSON string
recover_volume_mapping_instance = RecoverVolumeMapping.from_json(json)
# print the JSON string representation of the object
print(RecoverVolumeMapping.to_json())

# convert the object into a dict
recover_volume_mapping_dict = recover_volume_mapping_instance.to_dict()
# create an instance of RecoverVolumeMapping from a dict
recover_volume_mapping_from_dict = RecoverVolumeMapping.from_dict(recover_volume_mapping_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


