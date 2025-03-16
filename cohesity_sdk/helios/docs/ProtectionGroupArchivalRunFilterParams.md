# ProtectionGroupArchivalRunFilterParams

Specifies the additional filtering params for archival runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_full_archive** | **bool** | Specifies if the archival run is full archive to filter activities. | [optional] 
**is_rpaas** | **bool** | Specifies whether the run is an RPaaS run or not. If this is true then only RPaaS archival runs are returned. Default is false. | [optional] 
**protection_environment_types** | **List[str]** | Specifies the protection environment types to filter archival runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.protection_group_archival_run_filter_params import ProtectionGroupArchivalRunFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ProtectionGroupArchivalRunFilterParams from a JSON string
protection_group_archival_run_filter_params_instance = ProtectionGroupArchivalRunFilterParams.from_json(json)
# print the JSON string representation of the object
print(ProtectionGroupArchivalRunFilterParams.to_json())

# convert the object into a dict
protection_group_archival_run_filter_params_dict = protection_group_archival_run_filter_params_instance.to_dict()
# create an instance of ProtectionGroupArchivalRunFilterParams from a dict
protection_group_archival_run_filter_params_from_dict = ProtectionGroupArchivalRunFilterParams.from_dict(protection_group_archival_run_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


