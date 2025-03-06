# RecoverExchangeDbsParams

Specifies the parameters to recover Exchange databases.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**exchange_target_params** | [**ExchangeTargetParamsForRecoverExchangeDbs**](ExchangeTargetParamsForRecoverExchangeDbs.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_exchange_dbs_params import RecoverExchangeDbsParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverExchangeDbsParams from a JSON string
recover_exchange_dbs_params_instance = RecoverExchangeDbsParams.from_json(json)
# print the JSON string representation of the object
print(RecoverExchangeDbsParams.to_json())

# convert the object into a dict
recover_exchange_dbs_params_dict = recover_exchange_dbs_params_instance.to_dict()
# create an instance of RecoverExchangeDbsParams from a dict
recover_exchange_dbs_params_from_dict = RecoverExchangeDbsParams.from_dict(recover_exchange_dbs_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


