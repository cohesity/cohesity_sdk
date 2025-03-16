# RecoverUdaParams

Specifies the parameters to recover Universal Data Adapter objects.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**concurrency** | **int** | Specifies the maximum number of concurrent IO Streams that will be created to exchange data with the cluster. If not specified, the default value is taken as 1. | [optional] [default to 1]
**mounts** | **int** | Specifies the maximum number of view mounts per host. If not specified, the default value is taken as 1. | [optional] [default to 1]
**recover_to** | **int** | Specifies the &#39;Source Registration ID&#39; of the source where the objects are to be recovered. If this is not specified, the recovery job will recover to the original location. | [optional] 
**recovery_args** | **str** | Specifies the custom arguments to be supplied to the restore job script. This field is deprecated. Use recoveryJobArguments instead. | [optional] 
**recovery_job_arguments** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the map of custom arguments to be supplied to the restore job script. | [optional] 
**snapshots** | [**List[RecoverUdaSnapshotParams]**](RecoverUdaSnapshotParams.md) | Specifies the local snapshot ids and other details of the objects to be recovered. | 
**warnings** | **List[str]** | This field will hold the warnings in cases where the job status is SucceededWithWarnings. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.recover_uda_params import RecoverUdaParams

# TODO update the JSON string below
json = "{}"
# create an instance of RecoverUdaParams from a JSON string
recover_uda_params_instance = RecoverUdaParams.from_json(json)
# print the JSON string representation of the object
print(RecoverUdaParams.to_json())

# convert the object into a dict
recover_uda_params_dict = recover_uda_params_instance.to_dict()
# create an instance of RecoverUdaParams from a dict
recover_uda_params_from_dict = RecoverUdaParams.from_dict(recover_uda_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


