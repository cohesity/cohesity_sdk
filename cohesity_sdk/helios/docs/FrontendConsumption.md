# FrontendConsumption

Specifies the current consumption in terms of frontend usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **int** | Specifies the end date for the subscription. | [optional] 
**total_subscription** | **int** | The total subscribed usage for the month. | [optional] 
**usage** | [**List[FrontendUsage]**](FrontendUsage.md) | The current usage per region. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.frontend_consumption import FrontendConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of FrontendConsumption from a JSON string
frontend_consumption_instance = FrontendConsumption.from_json(json)
# print the JSON string representation of the object
print(FrontendConsumption.to_json())

# convert the object into a dict
frontend_consumption_dict = frontend_consumption_instance.to_dict()
# create an instance of FrontendConsumption from a dict
frontend_consumption_from_dict = FrontendConsumption.from_dict(frontend_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


