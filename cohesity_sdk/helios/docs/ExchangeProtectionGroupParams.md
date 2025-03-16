# ExchangeProtectionGroupParams

Specifies the parameters which are specific to Exchange related Protection Groups.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**backups_copy_only** | **bool** | Specifies whether the backups should be copy-only. | [optional] 
**exclude_database_ids** | **List[Optional[int]]** | Specifies the list of IDs of the databases to not be protected by this Protection Group. This can be used to ignore specific databases under Exchange Server/DAG which has been included for protection. | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**objects** | [**List[ExchangeProtectionGroupObjectParams]**](ExchangeProtectionGroupObjectParams.md) | Specifies the list of object ids to be protected. | 

## Example

```python
from cohesity_sdk.helios.models.exchange_protection_group_params import ExchangeProtectionGroupParams

# TODO update the JSON string below
json = "{}"
# create an instance of ExchangeProtectionGroupParams from a JSON string
exchange_protection_group_params_instance = ExchangeProtectionGroupParams.from_json(json)
# print the JSON string representation of the object
print(ExchangeProtectionGroupParams.to_json())

# convert the object into a dict
exchange_protection_group_params_dict = exchange_protection_group_params_instance.to_dict()
# create an instance of ExchangeProtectionGroupParams from a dict
exchange_protection_group_params_from_dict = ExchangeProtectionGroupParams.from_dict(exchange_protection_group_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


