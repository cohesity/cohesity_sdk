# RecoverGCPMySqlParams

Specifies the parameters to recover GCP MySQL database.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gcp_target_params** | [**GCPTargetParamsForRecoverGCPMySql**](GCPTargetParamsForRecoverGCPMySql.md) |  | 
**snapshots** | [**List[RecoverGCPMySqlSnapshotParams]**](RecoverGCPMySqlSnapshotParams.md) | Specifies the details of the gcp spanner objects to be recovered. | 
**target_environment** | **str** | Specifies the environment of the recovery target. The corresponding params below must be filled out. | 

## Example

```python
from cohesity_sdk.cluster.models.recover_gcpmy_sql_params import RecoverGCPMySqlParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverGCPMySqlParams from a JSON string
recover_gcpmy_sql_params_instance = RecoverGCPMySqlParams.from_json(json)
# print the JSON string representation of the object
print(RecoverGCPMySqlParams.to_json())

# convert the object into a dict
recover_gcpmy_sql_params_dict = recover_gcpmy_sql_params_instance.to_dict()
# create an instance of RecoverGCPMySqlParams from a dict
recover_gcpmy_sql_params_from_dict = RecoverGCPMySqlParams.from_dict(recover_gcpmy_sql_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


