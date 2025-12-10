# GCPTargetParamsForRecoverGCPSqlServer

Specifies the recovery target params for Google SQL Server target config.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cloud_storage_bucket_name** | **str** | The Google Cloud Storage bucket name for SQL recovery. | [optional] 
**new_source_config** | [**RecoverGCPSqlServerNewSourceConfig**](RecoverGCPSqlServerNewSourceConfig.md) |  | [optional] 
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing target. | 

## Example

```python
from cohesity_sdk.cluster.models.gcp_target_params_for_recover_gcp_sql_server import GCPTargetParamsForRecoverGCPSqlServer

# TODO update the JSON string below
json = "{}"
# create an instance of GCPTargetParamsForRecoverGCPSqlServer from a JSON string
gcp_target_params_for_recover_gcp_sql_server_instance = GCPTargetParamsForRecoverGCPSqlServer.from_json(json)
# print the JSON string representation of the object
print(GCPTargetParamsForRecoverGCPSqlServer.to_json())

# convert the object into a dict
gcp_target_params_for_recover_gcp_sql_server_dict = gcp_target_params_for_recover_gcp_sql_server_instance.to_dict()
# create an instance of GCPTargetParamsForRecoverGCPSqlServer from a dict
gcp_target_params_for_recover_gcp_sql_server_from_dict = GCPTargetParamsForRecoverGCPSqlServer.from_dict(gcp_target_params_for_recover_gcp_sql_server_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


