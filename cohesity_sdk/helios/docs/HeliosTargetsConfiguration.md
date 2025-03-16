# HeliosTargetsConfiguration

Specifies the replication, archival and cloud spin targets of Protection Policy.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_targets** | [**List[HeliosArchivalConfig]**](HeliosArchivalConfig.md) |  | [optional] 
**cloud_spin_targets** | [**List[HeliosCloudSpinConfig]**](HeliosCloudSpinConfig.md) |  | [optional] 
**onprem_deploy_targets** | [**List[HeliosOnpremDeployConfig]**](HeliosOnpremDeployConfig.md) |  | [optional] 
**replication_targets** | [**List[HeliosReplicationConfig]**](HeliosReplicationConfig.md) |  | [optional] 
**rpaas_targets** | [**List[HeliosRpaasConfig]**](HeliosRpaasConfig.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_targets_configuration import HeliosTargetsConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosTargetsConfiguration from a JSON string
helios_targets_configuration_instance = HeliosTargetsConfiguration.from_json(json)
# print the JSON string representation of the object
print(HeliosTargetsConfiguration.to_json())

# convert the object into a dict
helios_targets_configuration_dict = helios_targets_configuration_instance.to_dict()
# create an instance of HeliosTargetsConfiguration from a dict
helios_targets_configuration_from_dict = HeliosTargetsConfiguration.from_dict(helios_targets_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


