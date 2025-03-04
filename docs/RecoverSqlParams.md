# RecoverSqlParams

Specifies the recovery options specific to Sql environment.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**recover_app_params** | [**List[RecoverSqlAppParams]**](RecoverSqlAppParams.md) | Specifies the parameters to recover Sql databases. | [optional] 
**recovery_action** | **str** | Specifies the type of recover action to be performed. | 
**vlan_config** | [**RecoveryVlanConfig**](RecoveryVlanConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.models.recover_sql_params import RecoverSqlParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverSqlParams from a JSON string
recover_sql_params_instance = RecoverSqlParams.from_json(json)
# print the JSON string representation of the object
print(RecoverSqlParams.to_json())

# convert the object into a dict
recover_sql_params_dict = recover_sql_params_instance.to_dict()
# create an instance of RecoverSqlParams from a dict
recover_sql_params_from_dict = RecoverSqlParams.from_dict(recover_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


