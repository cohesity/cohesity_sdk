# SupportedConfig


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**min_nodes_allowed** | **int** | Specifies the minimum number of Nodes supported for this Cluster type. | [optional] 
**supported_erasure_coding** | **List[str]** | Array of Supported Erasure Coding Options. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.supported_config import SupportedConfig

# TODO update the JSON string below
json = "{}"
# create an instance of SupportedConfig from a JSON string
supported_config_instance = SupportedConfig.from_json(json)
# print the JSON string representation of the object
print(SupportedConfig.to_json())

# convert the object into a dict
supported_config_dict = supported_config_instance.to_dict()
# create an instance of SupportedConfig from a dict
supported_config_from_dict = SupportedConfig.from_dict(supported_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


