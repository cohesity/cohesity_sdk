# ErasureCodingParams

Specifies parameters for erasure coding.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**delay_secs** | **int** | Specifies the time in seconds when erasure coding starts. | [optional] 
**enabled** | **bool** | Specifies whether to enable erasure coding on a Storage Domain. | 
**inline_enabled** | **bool** | Specifies whether inline erasure coding is enabled. This field is appliciable only if enabled is set to true. | [optional] 
**num_coded_stripes** | **int** | Specifies the number of coded stripes. | 
**num_data_stripes** | **int** | Specifies the number of data stripes. | 

## Example

```python
from cohesity_sdk.models.erasure_coding_params import ErasureCodingParams

# TODO update the JSON string below
json = "{}"
# create an instance of ErasureCodingParams from a JSON string
erasure_coding_params_instance = ErasureCodingParams.from_json(json)
# print the JSON string representation of the object
print(ErasureCodingParams.to_json())

# convert the object into a dict
erasure_coding_params_dict = erasure_coding_params_instance.to_dict()
# create an instance of ErasureCodingParams from a dict
erasure_coding_params_from_dict = ErasureCodingParams.from_dict(erasure_coding_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


