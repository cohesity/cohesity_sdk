# PrimaryArchivalTarget

Specifies the primary archival settings. Mainly used for cloud direct archive (CAD) policy where primary backup is stored on archival target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_id** | **int** | Specifies the Archival target id to take primary backup. | 
**target_name** | **str** | Specifies the Archival target name where Snapshots are copied. | [optional] [readonly] 
**tier_settings** | [**TierLevelSettings**](TierLevelSettings.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.primary_archival_target import PrimaryArchivalTarget

# TODO update the JSON string below
json = "{}"
# create an instance of PrimaryArchivalTarget from a JSON string
primary_archival_target_instance = PrimaryArchivalTarget.from_json(json)
# print the JSON string representation of the object
print(PrimaryArchivalTarget.to_json())

# convert the object into a dict
primary_archival_target_dict = primary_archival_target_instance.to_dict()
# create an instance of PrimaryArchivalTarget from a dict
primary_archival_target_from_dict = PrimaryArchivalTarget.from_dict(primary_archival_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


