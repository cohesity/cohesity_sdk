# FilterObjectsRequest

Specifies the filter details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**filters** | [**[Filter], none_type**](Filter.md) | Specifies the list of filters that need to be applied on given list of discovered objects. | 
**object_ids** | **[int], none_type** | Specifies a list of non leaf object ids to filter the leaf level objects. Non leaf object such host (physical or vm) or database instance can be specified. | 
**filter_type** | **str, none_type** | Specifies the type of filtering user wants to perform. Currently, we only support exclude type of filter. | defaults to "exclude"
**application_environment** | **str, none_type** | Specifies the type of application enviornment needed for filtering to be applied on. This is needed because in case of applications like SQL, Oracle, a single source can contain multiple application enviornments. | [optional]  if omitted the server will use the default value of "kSQL"
**include_tenants** | **bool, none_type** | If true, the response will include objects which belongs to all tenants which the current user has permission to see. Default value is false. | [optional]  if omitted the server will use the default value of False
**tenant_ids** | **[str], none_type** | TenantIds contains list of the tenant for which objects are to be returned. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


