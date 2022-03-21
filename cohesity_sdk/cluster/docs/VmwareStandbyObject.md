# VmwareStandbyObject

Specifies the VMware specific standby object details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entity_id** | **int, none_type** | Specifies the entity id of the corresponding backup object for which this standby is configured. | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id to which this standby object belongs. | [optional] [readonly] 
**cdp_standby_status** | **str, none_type** | Specifies the current status of the standby object protected using continuous data protection policy. | [optional] 
**guest_id** | **str, none_type** | Specifies the guest ID(OS) of the standby VM for the corresponding backup object. | [optional] [readonly] 
**standby_m_oref** | [**MOref**](MOref.md) |  | [optional] 
**standby_time** | **int, none_type** | Specifies the time till which the standby object has been hydrated for the corresponding backup object. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


