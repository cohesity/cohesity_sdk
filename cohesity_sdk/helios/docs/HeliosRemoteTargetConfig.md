# HeliosRemoteTargetConfig

Specifies the configuration for adding remote cluster as repilcation target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id of the target replication cluster. | 
**cluster_name** | **str** | Specifies the cluster name of the target replication cluster. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.helios_remote_target_config import HeliosRemoteTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosRemoteTargetConfig from a JSON string
helios_remote_target_config_instance = HeliosRemoteTargetConfig.from_json(json)
# print the JSON string representation of the object
print(HeliosRemoteTargetConfig.to_json())

# convert the object into a dict
helios_remote_target_config_dict = helios_remote_target_config_instance.to_dict()
# create an instance of HeliosRemoteTargetConfig from a dict
helios_remote_target_config_from_dict = HeliosRemoteTargetConfig.from_dict(helios_remote_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


