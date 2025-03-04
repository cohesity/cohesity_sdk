# CreateProtectionGroupRunRequest

Specifies the request to create a protection run. On success, the system will accept the request and return the Protection Group id for which the run is supposed to start. The actual run may start at a later time if the system is busy. Consumers must query the Protection Group to see the run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_params** | [**CassandraProtectionRunParams**](CassandraProtectionRunParams.md) |  | [optional] 
**objects** | [**List[RunObject]**](RunObject.md) | Specifies the list of objects to be protected by this Protection Group run. These can be leaf objects or non-leaf objects in the protection hierarchy. This must be specified only if a subset of objects from the Protection Groups needs to be protected. | [optional] 
**run_type** | **str** | Type of protection run. &#39;kRegular&#39; indicates an incremental (CBT) backup. Incremental backups utilizing CBT (if supported) are captured of the target protection objects. The first run of a kRegular schedule captures all the blocks. &#39;kFull&#39; indicates a full (no CBT) backup. A complete backup (all blocks) of the target protection objects are always captured and Change Block Tracking (CBT) is not utilized. &#39;kLog&#39; indicates a Database Log backup. Capture the database transaction logs to allow rolling back to a specific point in time. &#39;kSystem&#39; indicates system volume backup. It produces an image for bare metal recovery. | 
**targets_config** | [**RunTargetsConfiguration**](RunTargetsConfiguration.md) |  | [optional] 
**uda_params** | [**UdaProtectionRunParams**](UdaProtectionRunParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.create_protection_group_run_request import CreateProtectionGroupRunRequest

# TODO update the JSON string below
json = "{}"
# create an instance of CreateProtectionGroupRunRequest from a JSON string
create_protection_group_run_request_instance = CreateProtectionGroupRunRequest.from_json(json)
# print the JSON string representation of the object
print(CreateProtectionGroupRunRequest.to_json())

# convert the object into a dict
create_protection_group_run_request_dict = create_protection_group_run_request_instance.to_dict()
# create an instance of CreateProtectionGroupRunRequest from a dict
create_protection_group_run_request_from_dict = CreateProtectionGroupRunRequest.from_dict(create_protection_group_run_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


