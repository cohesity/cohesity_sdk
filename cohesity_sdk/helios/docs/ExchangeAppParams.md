# ExchangeAppParams

Specifies the Exchange special parameters for the Protection Group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_id** | **int** | Specifies the application id of the Exchange database which has to be protected. | [optional] 
**app_name** | **str** | Specifies the application name of the Exchange database which has to be protected. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.exchange_app_params import ExchangeAppParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeAppParams from a JSON string
exchange_app_params_instance = ExchangeAppParams.from_json(json)
# print the JSON string representation of the object
print(ExchangeAppParams.to_json())

# convert the object into a dict
exchange_app_params_dict = exchange_app_params_instance.to_dict()
# create an instance of ExchangeAppParams from a dict
exchange_app_params_from_dict = ExchangeAppParams.from_dict(exchange_app_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


