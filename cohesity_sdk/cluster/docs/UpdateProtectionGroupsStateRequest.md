# UpdateProtectionGroupsStateRequest

Specifies the parameters to perform an action of list of Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**action** | **str, none_type** | Specifies the action to be performed on all the specfied Protection Groups. &#39;kActivate&#39; specifies that Protection Group should be activated. &#39;kDeactivate&#39; sepcifies that Protection Group should be deactivated. &#39;kPause&#39; specifies that Protection Group should be paused. &#39;kResume&#39; specifies that Protection Group should be resumed. | 
**ids** | **[str], none_type** | Specifies a list of Protection Group ids for which the state should change. | 
**last_pause_reason** | **str, none_type** | Specifies the reason why the protection group was paused | [optional]  if omitted the server will use the default value of "kTenantDeactivation"
**paused_note** | **str, none_type** | A note from the current user explaining the reason for pausing future runs, if applicable. | [optional] 
**tenant_id** | **str, none_type** | Specifies the tenant id who has access to these protection groups. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


