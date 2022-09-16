# VmwareCdpObject

Specifies the VMware specific CDP object details.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cdp_enabled** | **bool, none_type** | Specifies whether CDP is currently active or not. CDP might have been active on this object before, but it might not be anymore. | [optional] 
**last_run_info** | [**CdpObjectLastRunInfo**](CdpObjectLastRunInfo.md) |  | [optional] 
**protection_group_id** | **str, none_type** | Specifies the protection group id to which this CDP object belongs. | [optional] [readonly] 
**io_filter_status** | **str, none_type** | Specifies the state of CDP IO filter. CDP IO filter is an agent which will be installed on the object for performing continuous backup. &lt;br&gt; 1. &#39;kNotInstalled&#39; specifies that CDP is enabled on this object but filter is not installed. &lt;br&gt; 2. &#39;kInstallFilterInProgress&#39; specifies that IO filter installation is triggered and in progress. &lt;br&gt; 3. &#39;kFilterInstalledIOInactive&#39; specifies that IO filter is installed but IO streaming is disabled due to missing backup or explicitly disabled by the user. &lt;br&gt; 4. &#39;kIOActivationInProgress&#39; specifies that IO filter is activated to start streaming. &lt;br&gt; 5. &#39;kIOActive&#39; specifies that filter is attached to the object and started streaming. &lt;br&gt; 6. &#39;kIODeactivationInProgress&#39; specifies that deactivation has been initiated to stop the IO streaming. &lt;br&gt; 7. &#39;kUninstallFilterInProgress&#39; specifies that uninstallation of IO filter is in progress. | [optional] 
**io_filter_error_message** | **str, none_type** | Specifies the error message related to IO filter if there is any. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


