# Office365ProtectionGroupParams

Specifies the parameters which are specific to Office 365 related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exclude_object_ids** | **List[int]** | Specifies the objects to be excluded in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[Office365ProtectionGroupObjectParams]**](Office365ProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**one_drive_protection_type_params** | [**Office365OneDriveProtectionGroupParams**](Office365OneDriveProtectionGroupParams.md) |  | [optional] 
**outlook_protection_type_params** | [**Office365OutlookProtectionGroupParams**](Office365OutlookProtectionGroupParams.md) |  | [optional] 
**protection_types** | **List[str]** | Specifies the Office 365 Protection Group types. | 
**public_folders_protection_type_params** | [**Office365PublicFoldersProtectionGroupParams**](Office365PublicFoldersProtectionGroupParams.md) |  | [optional] 
**share_point_protection_type_params** | [**Office365SharePointProtectionGroupParams**](Office365SharePointProtectionGroupParams.md) |  | [optional] 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.office365_protection_group_params import Office365ProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of Office365ProtectionGroupParams from a JSON string
office365_protection_group_params_instance = Office365ProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(Office365ProtectionGroupParams.to_json())

# convert the object into a dict
office365_protection_group_params_dict = office365_protection_group_params_instance.to_dict()
# create an instance of Office365ProtectionGroupParams from a dict
office365_protection_group_params_from_dict = Office365ProtectionGroupParams.from_dict(office365_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


