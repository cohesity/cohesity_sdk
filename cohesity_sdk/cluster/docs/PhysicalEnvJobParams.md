# PhysicalEnvJobParams

Protection Job parameters applicable to 'kPhysical' Environment type. Specifies job parameters applicable for all 'kPhysical' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cobmr_backup** | **bool** | Specifies whether to enable CoBMR backup. | [optional] 
**file_path_filters** | [**FileFilteringPolicy**](FileFilteringPolicy.md) |  | [optional] 
**incremental_snapshot_upon_restart** | **bool** | If true, performs an incremental backup after server restarts. Otherwise a full backup is done. NOTE: This is applicable only to Windows servers. If not set, default value is false. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.physical_env_job_params import PhysicalEnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of PhysicalEnvJobParams from a JSON string
physical_env_job_params_instance = PhysicalEnvJobParams.from_json(json)
# print the JSON string representation of the object
print(PhysicalEnvJobParams.to_json())

# convert the object into a dict
physical_env_job_params_dict = physical_env_job_params_instance.to_dict()
# create an instance of PhysicalEnvJobParams from a dict
physical_env_job_params_from_dict = PhysicalEnvJobParams.from_dict(physical_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


