# CommonIndexedObjectParams

Holds parameters common to an indexed object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**path** | **str** | Specifies the path of the object. | [optional] 
**policy_id** | **str** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.common_indexed_object_params import CommonIndexedObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of CommonIndexedObjectParams from a JSON string
common_indexed_object_params_instance = CommonIndexedObjectParams.from_json(json)
# print the JSON string representation of the object
print(CommonIndexedObjectParams.to_json())

# convert the object into a dict
common_indexed_object_params_dict = common_indexed_object_params_instance.to_dict()
# create an instance of CommonIndexedObjectParams from a dict
common_indexed_object_params_from_dict = CommonIndexedObjectParams.from_dict(common_indexed_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


