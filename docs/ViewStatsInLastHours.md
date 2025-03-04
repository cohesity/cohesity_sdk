# ViewStatsInLastHours

Specifies the View stats for last hours.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**last_hours** | **int** | Specifies the time range. | [optional] 
**nfs_protocol_value** | **int** | Specifies the stats value for NFS protocol. | [optional] 
**s3_protocol_value** | **int** | Specifies the stats value for S3 protocol. | [optional] 
**smb_protocol_value** | **int** | Specifies the stats value for SMB protocol. | [optional] 
**value** | **int** | Specifies the stats value for any protocols. | [optional] 

## Example

```python
from cohesity_sdk.models.view_stats_in_last_hours import ViewStatsInLastHours

# TODO update the JSON string below
json = "{}"
# create an instance of ViewStatsInLastHours from a JSON string
view_stats_in_last_hours_instance = ViewStatsInLastHours.from_json(json)
# print the JSON string representation of the object
print(ViewStatsInLastHours.to_json())

# convert the object into a dict
view_stats_in_last_hours_dict = view_stats_in_last_hours_instance.to_dict()
# create an instance of ViewStatsInLastHours from a dict
view_stats_in_last_hours_from_dict = ViewStatsInLastHours.from_dict(view_stats_in_last_hours_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


