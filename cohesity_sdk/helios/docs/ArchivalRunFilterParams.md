# ArchivalRunFilterParams

Specifies the additional filtering params for archival runs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_rpaas** | **bool** | Specifies whether the run is an RPaaS run or not. If this is true then only RPaaS archival runs are returned. Default is false. | [optional] 
**protection_environment_types** | **List[str]** | Specifies the protection environment types to filter archival runs. | [optional] 
**run_types** | **List[str]** | Specifies the run types to filter archival runs. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.archival_run_filter_params import ArchivalRunFilterParams

# TODO update the JSON string below
json = "{}"
# create an instance of ArchivalRunFilterParams from a JSON string
archival_run_filter_params_instance = ArchivalRunFilterParams.from_json(json)
# print the JSON string representation of the object
print(ArchivalRunFilterParams.to_json())

# convert the object into a dict
archival_run_filter_params_dict = archival_run_filter_params_instance.to_dict()
# create an instance of ArchivalRunFilterParams from a dict
archival_run_filter_params_from_dict = ArchivalRunFilterParams.from_dict(archival_run_filter_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


