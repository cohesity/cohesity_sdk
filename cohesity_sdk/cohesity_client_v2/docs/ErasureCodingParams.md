# ErasureCodingParams

Specifies parameters for erasure coding.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**enabled** | **bool, none_type** | Specifies whether to enable erasure coding on a Storage Domain. | 
**num_data_stripes** | **int, none_type** | Specifies the number of data stripes. | 
**num_coded_stripes** | **int, none_type** | Specifies the number of coded stripes. | 
**algorithm** | **str, none_type** | Specifies the algorithm used for erasure coding. | [optional] 
**inline_enabled** | **bool, none_type** | Specifies whether inline erasure coding is enabled. This field is appliciable only if enabled is set to true. | [optional] 
**delay_secs** | **int, none_type** | Specifies the time in seconds when erasure coding starts. | [optional] 
**use_container** | **bool, none_type** | Whether to encode chunk files as part of a container. This field is appliciable only if enabled is set to true. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


