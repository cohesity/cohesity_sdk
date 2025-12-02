# CdpObjectLastRunInfo

Specifies the last backup information for a given CDP object.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**local_backup_info** | [**CdpLocalBackupInfo**](CdpLocalBackupInfo.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cdp_object_last_run_info import CdpObjectLastRunInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CdpObjectLastRunInfo from a JSON string
cdp_object_last_run_info_instance = CdpObjectLastRunInfo.from_json(json)
# print the JSON string representation of the object
print(CdpObjectLastRunInfo.to_json())

# convert the object into a dict
cdp_object_last_run_info_dict = cdp_object_last_run_info_instance.to_dict()
# create an instance of CdpObjectLastRunInfo from a dict
cdp_object_last_run_info_from_dict = CdpObjectLastRunInfo.from_dict(cdp_object_last_run_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


