# RecoverExchangeParams

Specifies the recovery options specific to Exchange environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_app_params** | [**RecoverExchangeAppParams**](RecoverExchangeAppParams.md) |  | [optional] 
**recover_exchange_dbs_params** | [**RecoverExchangeDbsParams**](RecoverExchangeDbsParams.md) |  | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_exchange_params import RecoverExchangeParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverExchangeParams from a JSON string
recover_exchange_params_instance = RecoverExchangeParams.from_json(json)
# print the JSON string representation of the object
print(RecoverExchangeParams.to_json())

# convert the object into a dict
recover_exchange_params_dict = recover_exchange_params_instance.to_dict()
# create an instance of RecoverExchangeParams from a dict
recover_exchange_params_from_dict = RecoverExchangeParams.from_dict(recover_exchange_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


