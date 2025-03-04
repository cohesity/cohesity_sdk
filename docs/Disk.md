# Disk

Specifies the details of a disk that belongs to a node.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**capacity_in_bytes** | **int** | Specifies capacity of disk in bytes. | [optional] 
**encryption_status** | **str** | Specifies disk encryption state. | [optional] 
**id** | **int** | Specifies id to uniquely identify a disk. | [optional] 
**location** | **str** | Specifies location of the disk in node. | [optional] 
**model** | **str** | Specifies product model of disk. | [optional] 
**node_id** | **int** | Specifies node id of the node that this disk belong to. | [optional] 
**precheck_timestamp_secs** | **int** | Specifies the last run time of the pre-checks execution in Unix epoch timestamp (in seconds). | [optional] 
**progress_percentage** | **int** | Specifies the overall progress percentage in removing the Disk. | [optional] 
**removal_progress_list** | [**List[ComponentRemovalProgress]**](ComponentRemovalProgress.md) | Specifies the removal progress details for services that are not acked yet. | [optional] 
**removal_reason** | **str** | Specifies the removal reason of the disk. | [optional] 
**removal_timestamp_secs** | **int** | Specifies the Unix epoch timestamp (in seconds) when the Disk was marked for removal. | [optional] 
**serial_number** | **str** | Specifies serial number of disk. | [optional] 
**services_acked_list** | **List[str]** | Specifies the services already ACKed for removal of this entity. | [optional] 
**services_not_acked** | **str** | Specifies the services that are not ACKed after disk is marked for removal. | [optional] 
**services_not_acked_list** | **List[str]** | Specifies the services not ACKed yet for removal of this entity. | [optional] 
**ssd_usage_level** | **str** | Specifies SSD usage level as Normal, Warning or Critical. | [optional] 
**ssd_used_percentage** | **int** | Specifies SSD used percentage. | [optional] 
**status** | **str** | Specifies status of the disk. | [optional] 
**time_remaining** | **int** | Specifies the total duration in seconds left to remove the Disk. | [optional] 
**type** | **str** | Specifies type of the disk. | [optional] 
**validation_checks** | [**List[PreCheckValidation]**](PreCheckValidation.md) | Specifies the pre-check validations results. | [optional] 

## Example

```python
from cohesity_sdk.models.disk import Disk

# TODO update the JSON string below
json = "{}"
# create an instance of Disk from a JSON string
disk_instance = Disk.from_json(json)
# print the JSON string representation of the object
print(Disk.to_json())

# convert the object into a dict
disk_dict = disk_instance.to_dict()
# create an instance of Disk from a dict
disk_from_dict = Disk.from_dict(disk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


