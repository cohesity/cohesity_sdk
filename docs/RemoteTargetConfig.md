# RemoteTargetConfig

Specifies the configuration for adding remote cluster as repilcation target

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int** | Specifies the cluster id of the target replication cluster. | 
**cluster_name** | **str** | Specifies the cluster name of the target replication cluster. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.remote_target_config import RemoteTargetConfig

# TODO update the JSON string below
json = "{}"
# create an instance of RemoteTargetConfig from a JSON string
remote_target_config_instance = RemoteTargetConfig.from_json(json)
# print the JSON string representation of the object
print(RemoteTargetConfig.to_json())

# convert the object into a dict
remote_target_config_dict = remote_target_config_instance.to_dict()
# create an instance of RemoteTargetConfig from a dict
remote_target_config_from_dict = RemoteTargetConfig.from_dict(remote_target_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


