# HeliosHiveObjectsInner


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | List of Clusters Identifiers to filter from. The format is clusterId:clusterIncarnationId. | [optional] 
**region_id** | **str** | Specifies the region id of the cluster. Only valid for DMaaS clusters. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**path** | **str** | Specifies the path of the object. | [optional] 
**policy_id** | **str** | Specifies the protection policy id for this file. | [optional] 
**policy_name** | **str** | Specifies the protection policy name for this file. | [optional] 
**protection_group_id** | **str** | \&quot;Specifies the protection group id which contains this object.\&quot; | [optional] 
**protection_group_name** | **str** | \&quot;Specifies the protection group name which contains this object.\&quot; | [optional] 
**source_info** | **object** | Specifies the Source Object information. | [optional] 
**storage_domain_id** | **int** | \&quot;Specifies the Storage Domain id where the backup data of Object is present.\&quot; | [optional] 
**snapshot_tags** | [**List[SnapshotTagInfo]**](SnapshotTagInfo.md) | Specifies snapshot tags applied to the object. | [optional] 
**tags** | [**List[TagInfo]**](TagInfo.md) | Specifies tag applied to the object. | [optional] 
**id** | **str** | Specifies the id of the indexed object. | [optional] 
**type** | **str** | Specifies the Hive Object Type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_hive_objects_inner import HeliosHiveObjectsInner

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosHiveObjectsInner from a JSON string
helios_hive_objects_inner_instance = HeliosHiveObjectsInner.from_json(json)
# print the JSON string representation of the object
print(HeliosHiveObjectsInner.to_json())

# convert the object into a dict
helios_hive_objects_inner_dict = helios_hive_objects_inner_instance.to_dict()
# create an instance of HeliosHiveObjectsInner from a dict
helios_hive_objects_inner_from_dict = HeliosHiveObjectsInner.from_dict(helios_hive_objects_inner_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


