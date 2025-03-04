# FileLockStatus

Specified the information about the lock status of a file.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**expiry_timestamp_msecs** | **int** | Specifies a expiry timestamp in milliseconds until the file is locked. | [optional] 
**hold_timestamp_msecs** | **int** | Specifies a override timestamp in milliseconds when an expired file is kept on hold. | [optional] 
**lock_timestamp_msecs** | **int** | Specifies the timestamp at which the file was locked. | [optional] 
**mode** | **str** | Specifies the mode of the file lock. A lock mode of a file in a view can be in one of the following: Compliance: Default mode of datalock, in this mode,   Data Security Admin cannot modify/delete this view when datalock   is in effect. Data Security Admin can delete this view   when datalock is expired. Enterprise: In this mode, Data Security Admin can change view name or   delete view when datalock is in effect. Datalock in this mode can   be upgraded to &#39;Compliance&#39; mode. | [optional] 
**state** | **str** | Specifies the lock state of the file. A lock state of a file in a view can be in one of the following: Unconfigured: File does not belong to data lock enabled view. Unlocked: A file created in a file lock enabled view. It will remain in   this state until auto-lock timer expires or user manually locks the file. Locked: A locked file has a set retention period that prevents users from   modifying the file data or extending, deleting, or renaming the file.   A locked file remain in this state untill retention period expires. Expired: When retention period ends, the file transition from the locked   state to the expired state. User can not modify or rename a file in expired   state, but can delete a file. Hold: Expired file is kept in hold for administrator specified retention   periods and deny any mutable or remove operation on locked files until a   specific date. | [optional] 

## Example

```python
from cohesity_sdk.models.file_lock_status import FileLockStatus

# TODO update the JSON string below
json = "{}"
# create an instance of FileLockStatus from a JSON string
file_lock_status_instance = FileLockStatus.from_json(json)
# print the JSON string representation of the object
print(FileLockStatus.to_json())

# convert the object into a dict
file_lock_status_dict = file_lock_status_instance.to_dict()
# create an instance of FileLockStatus from a dict
file_lock_status_from_dict = FileLockStatus.from_dict(file_lock_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


