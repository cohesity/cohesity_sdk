# AcropolisProtectionGroupParams

Specifies the parameters which are related to Acropolis Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**continue_on_quiesce_failure** | **bool** | Specifies whether to continue backing up on quiesce failure | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the object ids to be excluded in the Protection Group. | [optional] 
**global_exclude_disks** | [**List[AcropolisDiskInfo]**](AcropolisDiskInfo.md) | Specifies a list of disks to exclude from the backup. | [optional] 
**global_include_disks** | [**List[AcropolisDiskInfo]**](AcropolisDiskInfo.md) | Specifies a list of disks to include in the backup. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[AcropolisProtectionGroupObjectParams]**](AcropolisProtectionGroupObjectParams.md) | Specifies the objects included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.acropolis_protection_group_params import AcropolisProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of AcropolisProtectionGroupParams from a JSON string
acropolis_protection_group_params_instance = AcropolisProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(AcropolisProtectionGroupParams.to_json())

# convert the object into a dict
acropolis_protection_group_params_dict = acropolis_protection_group_params_instance.to_dict()
# create an instance of AcropolisProtectionGroupParams from a dict
acropolis_protection_group_params_from_dict = AcropolisProtectionGroupParams.from_dict(acropolis_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


