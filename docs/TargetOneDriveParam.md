# TargetOneDriveParam

Specifies the target OneDrive to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int** | Specifies the id of the target onedrive. Atleast one of id or primarySMTPAddress need to be defined. In case both id and primarySMTPAddress are defined then id takes precedence. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] [readonly] 
**parent_source_id** | **int** | Specifies the id of the domain for alternate domain recovery. | [optional] 
**primary_smtp_address** | **str** | Specifies the primary SMTP address of the target onedrive. Atleast one of id or primarySMTPAddress needs to be defined. In case both id and primarySMTPAddress are defined then id takes precedence. | [optional] 
**target_folder_path** | **str** | Specifies the path to the target folder. | 

## Example

```python
from cohesity_sdk.cluster.models.target_one_drive_param import TargetOneDriveParam

# TODO update the JSON string below
json = "{}"
# create an instance of TargetOneDriveParam from a JSON string
target_one_drive_param_instance = TargetOneDriveParam.from_json(json)
# print the JSON string representation of the object
print(TargetOneDriveParam.to_json())

# convert the object into a dict
target_one_drive_param_dict = target_one_drive_param_instance.to_dict()
# create an instance of TargetOneDriveParam from a dict
target_one_drive_param_from_dict = TargetOneDriveParam.from_dict(target_one_drive_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


