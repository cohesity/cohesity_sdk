# McmSourceInfo

Specifies the Protection Source information.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_id** | **int, none_type** | Specifies the cluster id. | [optional] 
**cluster_incarnation_id** | **int, none_type** | Specifies the cluster incarnation id. | [optional] 
**region_id** | **str, none_type** | Specifies the region id. | [optional] 
**source_id** | **int, none_type** | Specifies the id of the Protection Source. | [optional] 
**registration_id** | **str, none_type** | Specifies the registration id of the Protection Source. | [optional] 
**registration_details** | [**McmSourceRegistrationInfo**](McmSourceRegistrationInfo.md) |  | [optional] 
**applications** | **[str], none_type** | Specifies the list of applications registered with current Source. | [optional] 
**protection_stats** | [**[ObjectProtectionStatsSummary], none_type**](ObjectProtectionStatsSummary.md) | Specifies the protection statistics of the Source. | [optional] 
**physical_source_info** | [**McmPhysicalSourceInfo**](McmPhysicalSourceInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


