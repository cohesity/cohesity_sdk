# FileLevelDataLockConfig

Specifies a config to lock files in a view - to protect from malicious or an accidental attempt to delete or modify the files in this view.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**auto_lock_after_duration_idle_msecs** | **int** | Specifies the duration to lock a file that has not been accessed or modified (ie. has been idle) for a certain duration of time in milliseconds. Do not set if it is required to disable auto lock. | [optional] 
**coexisting_lock_mode** | **bool** | Specified if files in the View can be locked in different modes. This property is immutable and can only be set when enabling File level datalock. If this property is set for an S3 View, S3 bucket Versioning should also be enabled. | [optional] 
**default_retention_duration_msecs** | **int** | Specifies a global default retention duration for files in this view, if file lock is enabled for this view. Also, it is a required field if file lock is enabled. Set to -1 if the required default retention period is forever. | [optional] 
**default_retention_duration_years** | **int** | Specifies a global default retention duration in years for files in this view, if file/object lock is enabled for this view. | [optional] 
**expiry_timestamp_msecs** | **int** | Specifies a definite timestamp in milliseconds for retaining the file. | [optional] 
**locking_protocol** | **str** | Specifies the supported mechanisms to explicity lock a file from NFS/SMB interface. Supported locking protocols: SetReadOnly, SetAtime. &#39;SetReadOnly&#39; is compatible with Isilon/Netapp behaviour. This locks the file and the retention duration is determined in this order: 1) atime, if set by user/application and within min and max retention duration. 2) Min retention duration, if set. 3) Otherwise, file is switched to expired data automatically. &#39;SetAtime&#39; is compatible with Data Domain behaviour. | [optional] 
**max_retention_duration_msecs** | **int** | Specifies a maximum duration in milliseconds for which any file in this view can be retained for. Set to -1 if the required retention duration is forever. If set, it should be greater than or equal to the default retention period as well as the min retention period. | [optional] 
**min_retention_duration_msecs** | **int** | Specifies a minimum retention duration in milliseconds after a file gets locked. The file cannot be modified or deleted during this timeframe. Set to -1 if the required retention duration is forever. This should be set less than or equal to the default retention duration. | [optional] 
**mode** | **str** | Specifies the mode of file level datalock. Enterprise mode can be upgraded to Compliance mode, but Compliance mode cannot be downgraded to Enterprise mode. Compliance: This mode would disallow all user to delete/modify file or view under any condition when it &#39;s in locked status except for deleting view when the view is empty. Enterprise: This mode would follow the rules as compliance mode for normal users. But it would allow the storage admin (1) to delete view or file anytime no matter it is in locked status or expired. (2) to rename the view (3) to bring back the retention period when it&#39;s in locked mode A lock mode of a file in a view can be in one of the following: &#39;Compliance&#39;: Default mode of datalock, in this mode, Data Security Admin cannot modify/delete this view when datalock is in effect. Data Security Admin can delete this view when datalock is expired. &#39;kEnterprise&#39; : In this mode, Data Security Admin can change view name or delete view when datalock is in effect. Datalock in this mode can be upgraded to &#39;Compliance&#39; mode. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.file_level_data_lock_config import FileLevelDataLockConfig

# TODO update the JSON string below
json = "{}"
# create an instance of FileLevelDataLockConfig from a JSON string
file_level_data_lock_config_instance = FileLevelDataLockConfig.from_json(json)
# print the JSON string representation of the object
print(FileLevelDataLockConfig.to_json())

# convert the object into a dict
file_level_data_lock_config_dict = file_level_data_lock_config_instance.to_dict()
# create an instance of FileLevelDataLockConfig from a dict
file_level_data_lock_config_from_dict = FileLevelDataLockConfig.from_dict(file_level_data_lock_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


