# ExchangeTargetParamsForRecoverExchangeDbs

Specifies the parameters to recover Exchange applications to an Exchange target.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**objects** | [**List[RecoverExchangeDbsSnapshotParams]**](RecoverExchangeDbsSnapshotParams.md) | Specifies the Exchange Database object parameters. | 

## Example

```python
from cohesity_sdk.helios.models.exchange_target_params_for_recover_exchange_dbs import ExchangeTargetParamsForRecoverExchangeDbs

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeTargetParamsForRecoverExchangeDbs from a JSON string
exchange_target_params_for_recover_exchange_dbs_instance = ExchangeTargetParamsForRecoverExchangeDbs.from_json(json)
# print the JSON string representation of the object
print(ExchangeTargetParamsForRecoverExchangeDbs.to_json())

# convert the object into a dict
exchange_target_params_for_recover_exchange_dbs_dict = exchange_target_params_for_recover_exchange_dbs_instance.to_dict()
# create an instance of ExchangeTargetParamsForRecoverExchangeDbs from a dict
exchange_target_params_for_recover_exchange_dbs_from_dict = ExchangeTargetParamsForRecoverExchangeDbs.from_dict(exchange_target_params_for_recover_exchange_dbs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


