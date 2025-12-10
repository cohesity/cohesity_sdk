# EwsExchangeTargetParam

Describes the Exchange target to recover to.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ews_exchange_server_entity_id** | **int** | Specifies the entity ID of the exchange server. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.ews_exchange_target_param import EwsExchangeTargetParam

# TODO update the JSON string below
json = "{}"
# create an instance of EwsExchangeTargetParam from a JSON string
ews_exchange_target_param_instance = EwsExchangeTargetParam.from_json(json)
# print the JSON string representation of the object
print(EwsExchangeTargetParam.to_json())

# convert the object into a dict
ews_exchange_target_param_dict = ews_exchange_target_param_instance.to_dict()
# create an instance of EwsExchangeTargetParam from a dict
ews_exchange_target_param_from_dict = EwsExchangeTargetParam.from_dict(ews_exchange_target_param_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


