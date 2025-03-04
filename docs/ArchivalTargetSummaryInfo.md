# ArchivalTargetSummaryInfo

Specifies archival target summary information.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_task_id** | **str** | Specifies the archival task id. This is a protection group UID which only applies when archival type is &#39;Tape&#39;. | [optional] 
**ownership_context** | **str** | Specifies the ownership context for the target. | [optional] 
**target_id** | **int** | Specifies the archival target ID. | [optional] 
**target_name** | **str** | Specifies the archival target name. | [optional] 
**target_type** | **str** | Specifies the archival target type. | [optional] 
**tier_settings** | [**ArchivalTargetTierInfo**](ArchivalTargetTierInfo.md) |  | [optional] 
**usage_type** | **str** | Specifies the usage type for the target. | [optional] 

## Example

```python
from cohesity_sdk.models.archival_target_summary_info import ArchivalTargetSummaryInfo

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalTargetSummaryInfo from a JSON string
archival_target_summary_info_instance = ArchivalTargetSummaryInfo.from_json(json)
# print the JSON string representation of the object
print(ArchivalTargetSummaryInfo.to_json())

# convert the object into a dict
archival_target_summary_info_dict = archival_target_summary_info_instance.to_dict()
# create an instance of ArchivalTargetSummaryInfo from a dict
archival_target_summary_info_from_dict = ArchivalTargetSummaryInfo.from_dict(archival_target_summary_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


