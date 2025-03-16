# DraaSFETBUsage

Specifies the TiB usage statistics for DraaS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**current_usage** | **int** | The current usage from the start of the month. This includes only DraaS usage. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.draa_sfetb_usage import DraaSFETBUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DraaSFETBUsage from a JSON string
draa_sfetb_usage_instance = DraaSFETBUsage.from_json(json)
# print the JSON string representation of the object
print(DraaSFETBUsage.to_json())

# convert the object into a dict
draa_sfetb_usage_dict = draa_sfetb_usage_instance.to_dict()
# create an instance of DraaSFETBUsage from a dict
draa_sfetb_usage_from_dict = DraaSFETBUsage.from_dict(draa_sfetb_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


