# DataTieringTaskRunRequest

Specifies the request to run tiering task once.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**uptier_path** | **str, none_type** | Only applicable for uptiering tasks. Ignore the uptiering policy and uptier the directory pointed by the &#39;uptierPath&#39;. If path is &#39;/&#39;, then uptier everything.  This is a global property which will be applied to all shares by default. This can be overriden by specifying uptierPath for each share. | [optional] 
**shares** | [**[DataTieringShareInfo], none_type**](DataTieringShareInfo.md) | Specifies the list of shares to tier. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


