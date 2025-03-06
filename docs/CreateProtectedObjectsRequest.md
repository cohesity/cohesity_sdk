# CreateProtectedObjectsRequest

Specifies the request for creating an object backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**abort_in_blackouts** | **bool** | Specifies whether currently executing object backup should abort if a blackout period specified by a policy starts. Available only if the selected policy has at least one blackout period. Default value is false. | [optional] 
**end_time_usecs** | **int** | Specifies the end time in micro seconds for this Protection Group. If this is not specified, the Protection Group won&#39;t be ended. | [optional] 
**policy_config** | [**PolicyConfig**](PolicyConfig.md) |  | [optional] 
**policy_id** | **str** | Specifies the unique id of the Protection Policy. The Policy settings will be attached with every object and will be used in backup. | [optional] 
**priority** | **str** | Specifies the priority for the objects backup. | [optional] 
**qos_policy** | **str** | Specifies whether object backup will be written to HDD or SSD. | [optional] 
**skip_rigel_for_backup** | **bool** | Specifies whether to skip Rigel for backup or not. | [optional] 
**sla** | [**List[SlaRule]**](SlaRule.md) | Specifies the SLA parameters for list of objects. | [optional] 
**start_time** | [**TimeOfDay**](TimeOfDay.md) |  | [optional] 
**storage_domain_id** | **int** | Specifies the Storage Domain (View Box) ID where the object backup will be taken. This is not required if Cloud archive direct is benig used. | [optional] 
**activate_remote_object_protection** | **bool** | If set to true, it will look for the remote backup of the given user and object, and activates it. Creates a new backup if the remote backup is not found. After activation, this object cannot get snapshots from remote clusters. | [optional] 
**is_paused** | **bool** | If set to true, then the object specs will be created in the paused state preventing any runs from happening until they are unpaused. | [optional] 
**objects** | [**List[EnvSpecificObjectProtectionRequestParams]**](EnvSpecificObjectProtectionRequestParams.md) | Specifies the list of objects to be protected. Multiple objects from different adapters can be provided as input. | 

## Example

```python
from cohesity_sdk.cluster.models.create_protected_objects_request import CreateProtectedObjectsRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProtectedObjectsRequest from a JSON string
create_protected_objects_request_instance = CreateProtectedObjectsRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProtectedObjectsRequest.to_json())

# convert the object into a dict
create_protected_objects_request_dict = create_protected_objects_request_instance.to_dict()
# create an instance of CreateProtectedObjectsRequest from a dict
create_protected_objects_request_from_dict = CreateProtectedObjectsRequest.from_dict(create_protected_objects_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


