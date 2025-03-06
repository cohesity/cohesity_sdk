# ObjectLastRun

Specifies last run info of an object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | [**ObjectStringIdentifier**](ObjectStringIdentifier.md) |  | [optional] 
**environment** | **str** | Specifies the environment of the object. | [optional] 
**id** | **int** | Specifies object id. | [optional] 
**name** | **str** | Specifies the name of the object. | [optional] 
**source_id** | **int** | Specifies registered source id to which object belongs. | [optional] 
**source_name** | **str** | Specifies registered source name to which object belongs. | [optional] 
**child_objects** | [**List[ObjectSummary]**](ObjectSummary.md) | Specifies child object details. | [optional] 
**global_id** | **str** | Specifies the global id which is a unique identifier of the object. | [optional] 
**logical_size_bytes** | **int** | Specifies the logical size of object in bytes. | [optional] 
**object_hash** | **str** | Specifies the hash identifier of the object. | [optional] 
**object_type** | **str** | Specifies the type of the object. | [optional] 
**os_type** | **str** | Specifies the operating system type of the object. | [optional] 
**protection_type** | **str** | Specifies the protection type of the object if any. | [optional] 
**sharepoint_site_summary** | [**SharepointObjectParams**](SharepointObjectParams.md) |  | [optional] 
**uuid** | **str** | Specifies the uuid which is a unique identifier of the object. | [optional] 
**v_center_summary** | [**ObjectTypeVCenterParams**](ObjectTypeVCenterParams.md) |  | [optional] 
**windows_cluster_summary** | [**ObjectTypeWindowsClusterParams**](ObjectTypeWindowsClusterParams.md) |  | [optional] 
**archival_run_status** | **str** | Specifies the status of last archival run. | [optional] 
**backup_run_status** | **str** | Specifies the status of last local back up run. | [optional] 
**is_sla_violated** | **bool** | Specifies if the sla is violated in last run. | [optional] 
**policy_id** | **str** | Specifies the policy id of last run. | [optional] 
**policy_name** | **str** | Specifies the policy name of last run. | [optional] 
**protection_group_id** | **str** | Specifies the protection group id of last run. | [optional] 
**protection_group_name** | **str** | Specifies the protection group name of last run. | [optional] 
**replication_run_status** | **str** | Specifies the status of last replication run. | [optional] 
**run_id** | **str** | Specifies the last run id. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.object_last_run import ObjectLastRun

# TODO update the JSON string below
json = "{}"
# create an instance of ObjectLastRun from a JSON string
object_last_run_instance = ObjectLastRun.from_json(json)
# print the JSON string representation of the object
print(ObjectLastRun.to_json())

# convert the object into a dict
object_last_run_dict = object_last_run_instance.to_dict()
# create an instance of ObjectLastRun from a dict
object_last_run_from_dict = ObjectLastRun.from_dict(object_last_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


