# OneDriveParam

Specifies parameters to recover a OneDrive.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Specifies the OneDrive id. | [optional] 
**name** | **str** | Specifies the OneDrive name. | [optional] 
**recover_entire_drive** | **bool** | Specifies whether to recover the whole OneDrive. This is set to false when excluding recovering specific drive items. | [optional] 
**recover_items** | [**List[OneDriveItem]**](OneDriveItem.md) | Specifies a list of OneDrive items to recover. | [optional] 

## Example

```python
from cohesity_sdk.models.one_drive_param import OneDriveParam

# TODO update the JSON string below
json = "{}"
# create an instance of OneDriveParam from a JSON string
one_drive_param_instance = OneDriveParam.from_json(json)
# print the JSON string representation of the object
print(OneDriveParam.to_json())

# convert the object into a dict
one_drive_param_dict = one_drive_param_instance.to_dict()
# create an instance of OneDriveParam from a dict
one_drive_param_from_dict = OneDriveParam.from_dict(one_drive_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


