# RecoverDB2Params

Specifies the parameters to recover DB2 objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**mounts** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**recover_to_new_source** | **bool** | Specifies the parameter whether the recovery should be performed to a new or an existing Source Target. | 
**recovery_job_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the restore job script. | [optional] 
**recovery_target_config** | [**RecoverDB2TargetConfig**](RecoverDB2TargetConfig.md) |  | [optional] 
**rollforward_database** | **bool** | Roll forward the database after the recovery is complete. Enabled by default. | [optional] [default to True]
**snapshots** | [**List[RecoverUdaSnapshotParams]**](RecoverUdaSnapshotParams.md) | Specifies the local snapshot ids and other details of the objects to be recovered. | 
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.cluster.models.recover_db2_params import RecoverDB2Params

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverDB2Params from a JSON string
recover_db2_params_instance = RecoverDB2Params.from_json(json)
# print the JSON string representation of the object
print(RecoverDB2Params.to_json())

# convert the object into a dict
recover_db2_params_dict = recover_db2_params_instance.to_dict()
# create an instance of RecoverDB2Params from a dict
recover_db2_params_from_dict = RecoverDB2Params.from_dict(recover_db2_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


