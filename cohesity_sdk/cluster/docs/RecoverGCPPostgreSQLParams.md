# RecoverGCPPostgreSQLParams

Specifies the parameters to recover GCP PostgreSQL database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPPostgreSQL**](GCPTargetParamsForRecoverGCPPostgreSQL.md) |  | 
**snapshots** | [**List[RecoverGCPPostgreSQLSnapshotParams]**](RecoverGCPPostgreSQLSnapshotParams.md) | Specifies the details of the GCP PostgreSQL objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcp_postgre_sql_params import RecoverGCPPostgreSQLParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPPostgreSQLParams from a JSON string
recover_gcp_postgre_sql_params_instance = RecoverGCPPostgreSQLParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPPostgreSQLParams.to_json())

# convert the object into a dict
recover_gcp_postgre_sql_params_dict = recover_gcp_postgre_sql_params_instance.to_dict()
# create an instance of RecoverGCPPostgreSQLParams from a dict
recover_gcp_postgre_sql_params_from_dict = RecoverGCPPostgreSQLParams.from_dict(recover_gcp_postgre_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


