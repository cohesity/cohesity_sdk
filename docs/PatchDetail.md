# PatchDetail

Detail of a patch. It gives the service and version information of the the patch.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str, none_type** | Specifies the name of the service. | [optional] 
**component** | **str, none_type** | Specifies the user friendly name of the service. | [optional] 
**version** | **str, none_type** | Specifies the existing version of the service. This is the available service patch version if exists. If there is no patch available, then it is the applied patch version if applied. If both don&#39;t exist, it is the base version of the service. | [optional] 
**import_version** | **str, none_type** | Specifies the version of the imported service patch. | [optional] 
**status** | **str, none_type** | Specifies the status of the patch whether it is accepted or rejected. A patch is rejected if it is older than the version available or applied on the cluster. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


