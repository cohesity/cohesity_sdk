# RpaasUsage

RPaaS data usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_usage** | [**List[RpaasBackendConsumption]**](RpaasBackendConsumption.md) | The RPaaS usage per region. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_usage import RpaasUsage

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasUsage from a JSON string
rpaas_usage_instance = RpaasUsage.from_json(json)
# print the JSON string representation of the object
print(RpaasUsage.to_json())

# convert the object into a dict
rpaas_usage_dict = rpaas_usage_instance.to_dict()
# create an instance of RpaasUsage from a dict
rpaas_usage_from_dict = RpaasUsage.from_dict(rpaas_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


