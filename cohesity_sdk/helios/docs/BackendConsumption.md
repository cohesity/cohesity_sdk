# BackendConsumption

Specifies the current consumption in terms of backend usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**end_date** | **int** | Specifies the end date for the subscription. | [optional] 
**total_subscription** | **int** | The total subscribed usage for the month. | [optional] 
**usage** | [**List[BackendUsage]**](BackendUsage.md) | The current usage per region. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.backend_consumption import BackendConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of BackendConsumption from a JSON string
backend_consumption_instance = BackendConsumption.from_json(json)
# print the JSON string representation of the object
print(BackendConsumption.to_json())

# convert the object into a dict
backend_consumption_dict = backend_consumption_instance.to_dict()
# create an instance of BackendConsumption from a dict
backend_consumption_from_dict = BackendConsumption.from_dict(backend_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


