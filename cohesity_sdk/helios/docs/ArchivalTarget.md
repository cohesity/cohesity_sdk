# ArchivalTarget

Specifies the information about archival target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_cloud_tier** | **bool** | Specifies if the external target is a cloud tier. | [optional] 
**name** | **str** | Specifies the name of the archival target. | [optional] 
**target_id** | **int** | Specifies the id of the archival target. | [optional] 
**target_type** | **str** | Specifies the type of the archival target. | [optional] 
**uuid** | **str** | Specifies the unique Id of the archival target. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.archival_target import ArchivalTarget

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalTarget from a JSON string
archival_target_instance = ArchivalTarget.from_json(json)
# print the JSON string representation of the object
print(ArchivalTarget.to_json())

# convert the object into a dict
archival_target_dict = archival_target_instance.to_dict()
# create an instance of ArchivalTarget from a dict
archival_target_from_dict = ArchivalTarget.from_dict(archival_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


