# ObjectOneDriveParam

Specifies OneDrive recovery parameters associated with a user.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**one_drive_params** | [**List[OneDriveParam]**](OneDriveParam.md) | Specifies parameters to recover a OneDrive. | [optional] 
**owner_info** | [**CommonRecoverObjectSnapshotParams**](CommonRecoverObjectSnapshotParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.object_one_drive_param import ObjectOneDriveParam

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectOneDriveParam from a JSON string
object_one_drive_param_instance = ObjectOneDriveParam.from_json(json)
# print the JSON string representation of the object
print(ObjectOneDriveParam.to_json())

# convert the object into a dict
object_one_drive_param_dict = object_one_drive_param_instance.to_dict()
# create an instance of ObjectOneDriveParam from a dict
object_one_drive_param_from_dict = ObjectOneDriveParam.from_dict(object_one_drive_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


