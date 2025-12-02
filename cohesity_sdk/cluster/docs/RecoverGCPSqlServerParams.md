# RecoverGCPSqlServerParams

Specifies the parameters to recover GCP SQL Server database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPSqlServer**](GCPTargetParamsForRecoverGCPSqlServer.md) |  | 
**snapshots** | [**List[RecoverGCPSqlServerSnapshotParams]**](RecoverGCPSqlServerSnapshotParams.md) | Specifies the details of the gcp sql server objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_sql_server_params import RecoverGCPSqlServerParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPSqlServerParams from a JSON string
recover_gcp_sql_server_params_instance = RecoverGCPSqlServerParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPSqlServerParams.to_json())

# convert the object into a dict
recover_gcp_sql_server_params_dict = recover_gcp_sql_server_params_instance.to_dict()
# create an instance of RecoverGCPSqlServerParams from a dict
recover_gcp_sql_server_params_from_dict = RecoverGCPSqlServerParams.from_dict(recover_gcp_sql_server_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


