# CommonExternalTargetParams

Specifies the parameters which are common between all External Target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str, none_type** | Specifies the name of the External Target. | 
**purpose_type** | **str, none_type** | Specifies the purpose of the External Target. | 
**id** | **int, none_type** | Specifies the ID of the External Target. | [optional] [readonly] 
**compression** | **str, none_type** | Specifies whether the type of compression of the External Target | [optional] 
**status** | **str, none_type** | Specifies the registration status of the External Target | [optional] [readonly] 
**error_message** | **str, none_type** | Specifies the error message if the event is in failed state. | [optional] [readonly] 
**tenant_ids** | **[str]** | Specifies the list of tenantIds for the External Target | [optional] 
**cloud_domains** | [**[CloudDomain], none_type**](CloudDomain.md) | Specifies the cloud domain information. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


