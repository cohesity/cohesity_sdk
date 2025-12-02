# GCPTargetParamsForRecoverGCPMySql

Specifies the recovery target params for Google Spanner target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverGCPMySqlNewSourceConfig**](RecoverGCPMySqlNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_gcpmy_sql import GCPTargetParamsForRecoverGCPMySql

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTargetParamsForRecoverGCPMySql from a JSON string
gcp_target_params_for_recover_gcpmy_sql_instance = GCPTargetParamsForRecoverGCPMySql.from_json(json)
# print the JSON string representation of the object
print(GCPTargetParamsForRecoverGCPMySql.to_json())

# convert the object into a dict
gcp_target_params_for_recover_gcpmy_sql_dict = gcp_target_params_for_recover_gcpmy_sql_instance.to_dict()
# create an instance of GCPTargetParamsForRecoverGCPMySql from a dict
gcp_target_params_for_recover_gcpmy_sql_from_dict = GCPTargetParamsForRecoverGCPMySql.from_dict(gcp_target_params_for_recover_gcpmy_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


