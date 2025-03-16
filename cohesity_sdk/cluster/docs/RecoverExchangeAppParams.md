# RecoverExchangeAppParams

Specifies the parameters to recover Sql databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_target_params** | [**ExchangeTargetParamsForRecoverExchangeApp**](ExchangeTargetParamsForRecoverExchangeApp.md) |  | [optional] 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_exchange_app_params import RecoverExchangeAppParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverExchangeAppParams from a JSON string
recover_exchange_app_params_instance = RecoverExchangeAppParams.from_json(json)
# print the JSON string representation of the object
print(RecoverExchangeAppParams.to_json())

# convert the object into a dict
recover_exchange_app_params_dict = recover_exchange_app_params_instance.to_dict()
# create an instance of RecoverExchangeAppParams from a dict
recover_exchange_app_params_from_dict = RecoverExchangeAppParams.from_dict(recover_exchange_app_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


