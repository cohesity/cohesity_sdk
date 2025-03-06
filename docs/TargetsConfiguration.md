# TargetsConfiguration

Specifies the replication, archival and cloud spin targets of Protection Policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_targets** | [**List[ArchivalConfig]**](ArchivalConfig.md) |  | [optional] 
**cloud_spin_targets** | [**List[CloudSpinConfig]**](CloudSpinConfig.md) |  | [optional] 
**onprem_deploy_targets** | [**List[OnpremDeployConfig]**](OnpremDeployConfig.md) |  | [optional] 
**replication_targets** | [**List[ReplicationConfig]**](ReplicationConfig.md) |  | [optional] 
**rpaas_targets** | [**List[RpaasConfig]**](RpaasConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.targets_configuration import TargetsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of TargetsConfiguration from a JSON string
targets_configuration_instance = TargetsConfiguration.from_json(json)
# print the JSON string representation of the object
print(TargetsConfiguration.to_json())

# convert the object into a dict
targets_configuration_dict = targets_configuration_instance.to_dict()
# create an instance of TargetsConfiguration from a dict
targets_configuration_from_dict = TargetsConfiguration.from_dict(targets_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


