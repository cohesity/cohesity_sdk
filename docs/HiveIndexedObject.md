# HiveIndexedObject

Specifies a Hive indexed object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | Specifies the name of the object. | [optional] 
**path** | **str** | Specifies the path of the object. | [optional] 
**policy_id** | **str** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | [**ObjectSummary**](ObjectSummary.md) |  | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**id** | **str** | Specifies the id of the indexed object. | [optional] 
**type** | **str** | Specifies the Hive Object Type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.hive_indexed_object import HiveIndexedObject

# TODO update the JSON string below
json = "{}"
# create an instance of HiveIndexedObject from a JSON string
hive_indexed_object_instance = HiveIndexedObject.from_json(json)
# print the JSON string representation of the object
print(HiveIndexedObject.to_json())

# convert the object into a dict
hive_indexed_object_dict = hive_indexed_object_instance.to_dict()
# create an instance of HiveIndexedObject from a dict
hive_indexed_object_from_dict = HiveIndexedObject.from_dict(hive_indexed_object_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


