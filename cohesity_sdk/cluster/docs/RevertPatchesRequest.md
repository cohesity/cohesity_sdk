# RevertPatchesRequest

Specifies the request to revert a patch. An optional patch level can be specified. When a patch level is specified, system keeps reverting patches until the given patch level is reverted. If no patch level is specified, just the last applied patch is reverted.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**service** | **str** | Specifies the name of the service whose patch should be reverted. | 
**patch_level** | **int, none_type** | Specifies optional patch level upto which the patches should be reverted. If given, it should be between 1 and the current patch level inclusive. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


