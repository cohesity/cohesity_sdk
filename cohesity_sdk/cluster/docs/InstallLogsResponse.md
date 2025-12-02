# InstallLogsResponse

\"Response containing install logs for services.\" 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helios_install_status** | **str** | \&quot;The overall install status \&quot; \&quot;(e.g., Success, InProgress, Failed, Pending).\&quot;  | [optional] 
**helios_install_version** | **str** | Helios install version. | [optional] 
**helios_restore_status** | **str** | \&quot;The overall restore status \&quot; \&quot;(e.g., Success, InProgress, Failed, Pending, NotApplicable).\&quot;  | [optional] 
**services** | [**[ServiceInstallLog]**](ServiceInstallLog.md) | List of service install logs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


