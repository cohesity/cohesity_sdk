# ExchangeTargetParamsForRecoverExchangeApp

Specifies the parameters to recover Exchange applications to an Exchange target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**object** | [**RecoverExchangeAppSnapshotParams**](RecoverExchangeAppSnapshotParams.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.exchange_target_params_for_recover_exchange_app import ExchangeTargetParamsForRecoverExchangeApp

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTargetParamsForRecoverExchangeApp from a JSON string
exchange_target_params_for_recover_exchange_app_instance = ExchangeTargetParamsForRecoverExchangeApp.from_json(json)
# print the JSON string representation of the object
print(ExchangeTargetParamsForRecoverExchangeApp.to_json())

# convert the object into a dict
exchange_target_params_for_recover_exchange_app_dict = exchange_target_params_for_recover_exchange_app_instance.to_dict()
# create an instance of ExchangeTargetParamsForRecoverExchangeApp from a dict
exchange_target_params_for_recover_exchange_app_from_dict = ExchangeTargetParamsForRecoverExchangeApp.from_dict(exchange_target_params_for_recover_exchange_app_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


