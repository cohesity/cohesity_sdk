# UpgradeLogsResponse

\"Response containing upgrade logs for services.\" 

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**helios_upgrade_status** | **str** | \&quot;The overall upgrade status\&quot; \&quot;(e.g., Success, InProgress, Failed, Pending).\&quot;  | [optional] 
**helios_upgrade_version** | **str** | Helios upgrade version. | [optional] 
**services** | [**[ServiceUpgradeLog]**](ServiceUpgradeLog.md) | List of service upgrade logs. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


