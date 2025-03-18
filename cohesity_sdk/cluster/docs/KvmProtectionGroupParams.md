# KvmProtectionGroupParams

Specifies the parameters which are specific to Kvm related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_consistent_snapshot** | **bool** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. If not specified or false then snapshots will not be app consistent. | [optional] 
**exclude_object_ids** | **List[int]** | Specifies the object ids to be excluded in the Protection Group. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[KvmProtectionGroupObjectParams]**](KvmProtectionGroupObjectParams.md) | Specifies the objects to be included in the Protection Group. | 
**source_id** | **int** | Specifies the id of the parent of the objects. | [optional] [readonly] 
**source_name** | **str** | Specifies the name of the parent of the objects. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.kvm_protection_group_params import KvmProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of KvmProtectionGroupParams from a JSON string
kvm_protection_group_params_instance = KvmProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(KvmProtectionGroupParams.to_json())

# convert the object into a dict
kvm_protection_group_params_dict = kvm_protection_group_params_instance.to_dict()
# create an instance of KvmProtectionGroupParams from a dict
kvm_protection_group_params_from_dict = KvmProtectionGroupParams.from_dict(kvm_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


