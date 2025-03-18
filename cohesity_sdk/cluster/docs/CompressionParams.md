# CompressionParams

Specifies parameters for compression.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inline_enabled** | **bool** | Specifies whether inline compression is enabled. This field is appliciable only if inlineDeduplicationEnabled is set to true and compression is enabled. | [optional] 
**type** | **str** | Specifies copmpression type for a Storage Domain. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.compression_params import CompressionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CompressionParams from a JSON string
compression_params_instance = CompressionParams.from_json(json)
# print the JSON string representation of the object
print(CompressionParams.to_json())

# convert the object into a dict
compression_params_dict = compression_params_instance.to_dict()
# create an instance of CompressionParams from a dict
compression_params_from_dict = CompressionParams.from_dict(compression_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


