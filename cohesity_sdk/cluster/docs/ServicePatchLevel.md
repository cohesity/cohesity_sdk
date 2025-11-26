# ServicePatchLevel

Patch level of a service. It is the number of patches applied for the service on the cluster. If a service is never patched the patch level is 0. If two patches were applied, patch level is 2.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**patch_level** | **int, none_type** | Specifies patch level of the service after the patch operation. | [optional] 
**patch_version** | **str, none_type** | Specifies the version of the service patch after the patch operation. | [optional] 
**service** | **str, none_type** | Specifies the name of the service. | [optional] 
**start_level** | **int, none_type** | Specifies patch level of the service before the patch operation. | [optional] 
**start_version** | **str, none_type** | Specifies the version of the service running on the cluster before the patch operation. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


