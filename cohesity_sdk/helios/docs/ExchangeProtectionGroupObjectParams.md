# ExchangeProtectionGroupObjectParams

Specifies the object identifier to for the exchange protection group.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**app_params** | [**List[ExchangeAppParams]**](ExchangeAppParams.md) | Specifies the specific parameters required for Exchange app configuration. | [optional] 
**id** | **int** | Specifies the id of the registered Exchange DAG(Database Availability Group) source or Exchange physical source. | 
**name** | **str** | Specifies the name of the registered Exchange DAG(Database Availability Group) source or Exchange physical source. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.exchange_protection_group_object_params import ExchangeProtectionGroupObjectParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeProtectionGroupObjectParams from a JSON string
exchange_protection_group_object_params_instance = ExchangeProtectionGroupObjectParams.from_json(json)
# print the JSON string representation of the object
print(ExchangeProtectionGroupObjectParams.to_json())

# convert the object into a dict
exchange_protection_group_object_params_dict = exchange_protection_group_object_params_instance.to_dict()
# create an instance of ExchangeProtectionGroupObjectParams from a dict
exchange_protection_group_object_params_from_dict = ExchangeProtectionGroupObjectParams.from_dict(exchange_protection_group_object_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


