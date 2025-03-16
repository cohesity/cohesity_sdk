# DataProtectUsage

Data Protect Usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backend_usage** | [**BackendConsumption**](BackendConsumption.md) |  | [optional] 
**frontend_usage** | [**FrontendConsumption**](FrontendConsumption.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.data_protect_usage import DataProtectUsage

# TODO update the JSON string below
json = "{}"
# create an instance of DataProtectUsage from a JSON string
data_protect_usage_instance = DataProtectUsage.from_json(json)
# print the JSON string representation of the object
print(DataProtectUsage.to_json())

# convert the object into a dict
data_protect_usage_dict = data_protect_usage_instance.to_dict()
# create an instance of DataProtectUsage from a dict
data_protect_usage_from_dict = DataProtectUsage.from_dict(data_protect_usage_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


