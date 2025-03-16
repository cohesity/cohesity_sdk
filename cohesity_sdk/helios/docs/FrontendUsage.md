# FrontendUsage

Specifies the TiB usage statistics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_usage** | **int** | The current usage from the start of the month. This includes only DMaaS statistics. | [optional] 
**draas_usage** | [**DraaSFETBUsage**](DraaSFETBUsage.md) |  | [optional] 
**region_id** | **str** | The current region for which usage is calculated. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.frontend_usage import FrontendUsage

# TODO update the JSON string below
json = "{}"
# create an instance of FrontendUsage from a JSON string
frontend_usage_instance = FrontendUsage.from_json(json)
# print the JSON string representation of the object
print(FrontendUsage.to_json())

# convert the object into a dict
frontend_usage_dict = frontend_usage_instance.to_dict()
# create an instance of FrontendUsage from a dict
frontend_usage_from_dict = FrontendUsage.from_dict(frontend_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


