# GCPTargetParamsForRecoverGCPPostgreSQL

Specifies the recovery target params for Google PostgreSQL target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**new_source_config** | [**RecoverGCPPostgreSQLNewSourceConfig**](RecoverGCPPostgreSQLNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_gcp_postgre_sql import GCPTargetParamsForRecoverGCPPostgreSQL

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTargetParamsForRecoverGCPPostgreSQL from a JSON string
gcp_target_params_for_recover_gcp_postgre_sql_instance = GCPTargetParamsForRecoverGCPPostgreSQL.from_json(json)
# print the JSON string representation of the object
print(GCPTargetParamsForRecoverGCPPostgreSQL.to_json())

# convert the object into a dict
gcp_target_params_for_recover_gcp_postgre_sql_dict = gcp_target_params_for_recover_gcp_postgre_sql_instance.to_dict()
# create an instance of GCPTargetParamsForRecoverGCPPostgreSQL from a dict
gcp_target_params_for_recover_gcp_postgre_sql_from_dict = GCPTargetParamsForRecoverGCPPostgreSQL.from_dict(gcp_target_params_for_recover_gcp_postgre_sql_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


