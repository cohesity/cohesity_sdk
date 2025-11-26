# GetM365SourceRegionEndpointResponseParams

Specifies the response parameters containing region and various endpoint for Microsoft365 source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**device_auth_endpoint** | **str, none_type** | Specifies the device authorization endpoint to be used for Microsoft graph calls. | [optional] 
**graph_endpoint** | **str, none_type** | Specifies the Microsoft graph host url to be used for graph calls. | [optional] 
**region** | **str, none_type** | Specifies the scope of the region. For eg NA for North America or AS for Australia. For Azure Gov cloud it can be USG or USGov. | [optional] 
**sub_region** | **str, none_type** | Specifies the scope of the sub region. | [optional] 
**tenant_region** | **str, none_type** | Specifies the tenant region for the given domain. This can be either Default(Commercial), GCC, GCC High or DoD. This is different from the Geo location which is represented by the region parameter. | [optional] 
**token_endpoint** | **str, none_type** | Specifies the token endpoint of the Microsoft365 source. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


