# RecoveryTimeRangeInfo

Specifies a valid time range to which this object can be recovered.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_time_usecs** | **int** | Specifies the end time of this time range. | [optional] 
**protection_group_id** | **str** | Specifies id of the Protection Group corresponding to this time range. | [optional] 
**start_time_usecs** | **int** | Specifies the start time of this time range. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.recovery_time_range_info import RecoveryTimeRangeInfo

# TODO update the JSON string below
json = "{}"
# create an instance of RecoveryTimeRangeInfo from a JSON string
recovery_time_range_info_instance = RecoveryTimeRangeInfo.from_json(json)
# print the JSON string representation of the object
print(RecoveryTimeRangeInfo.to_json())

# convert the object into a dict
recovery_time_range_info_dict = recovery_time_range_info_instance.to_dict()
# create an instance of RecoveryTimeRangeInfo from a dict
recovery_time_range_info_from_dict = RecoveryTimeRangeInfo.from_dict(recovery_time_range_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


