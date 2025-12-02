# SanEnvJobParams

Specifies job parameters applicable for all SAN Environment types Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**max_snapshots_on_primary** | **int** | Specifies how many recent snapshots of each backed up entity to retain on the primary environment. If not specified, then snapshots will not be be deleted from the primary environment. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.san_env_job_params import SanEnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of SanEnvJobParams from a JSON string
san_env_job_params_instance = SanEnvJobParams.from_json(json)
# print the JSON string representation of the object
print(SanEnvJobParams.to_json())

# convert the object into a dict
san_env_job_params_dict = san_env_job_params_instance.to_dict()
# create an instance of SanEnvJobParams from a dict
san_env_job_params_from_dict = SanEnvJobParams.from_dict(san_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


