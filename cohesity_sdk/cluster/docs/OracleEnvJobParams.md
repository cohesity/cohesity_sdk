# OracleEnvJobParams

Specifies job parameters applicable for all 'kOracle' Environment type Protection Sources in a Protection Job.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**persist_mountpoints** | **bool** | Specifies whether the mountpoints created while backing up Oracle DBs should be persisted. Note: This parameter is for the entire Job. For overriding persistence of mountpoints for a subset of Oracle hosts within the job, refer OracleSourceParams. | [optional] 
**vlan_params** | [**VlanParams**](VlanParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.oracle_env_job_params import OracleEnvJobParams

# TODO update the JSON string below
json = "{}"
# create an instance of OracleEnvJobParams from a JSON string
oracle_env_job_params_instance = OracleEnvJobParams.from_json(json)
# print the JSON string representation of the object
print(OracleEnvJobParams.to_json())

# convert the object into a dict
oracle_env_job_params_dict = oracle_env_job_params_instance.to_dict()
# create an instance of OracleEnvJobParams from a dict
oracle_env_job_params_from_dict = OracleEnvJobParams.from_dict(oracle_env_job_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


