# CascadedTargetConfiguration

Specifies the source of the cascadded replication and list of all remote targets that needs to added. Each source cluster and remote targets are considered as nodes and immediate connections between them are considered as edges.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**remote_targets** | [**TargetsConfiguration**](TargetsConfiguration.md) |  | 
**source_cluster_id** | **int** | Specifies the source cluster id from where the remote operations will be performed to the next set of remote targets. | 

## Example

```python
from cohesity_sdk.cluster.models.cascaded_target_configuration import CascadedTargetConfiguration

# TODO update the JSON string below
json = "{}"
# create an instance of CascadedTargetConfiguration from a JSON string
cascaded_target_configuration_instance = CascadedTargetConfiguration.from_json(json)
# print the JSON string representation of the object
print(CascadedTargetConfiguration.to_json())

# convert the object into a dict
cascaded_target_configuration_dict = cascaded_target_configuration_instance.to_dict()
# create an instance of CascadedTargetConfiguration from a dict
cascaded_target_configuration_from_dict = CascadedTargetConfiguration.from_dict(cascaded_target_configuration_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


