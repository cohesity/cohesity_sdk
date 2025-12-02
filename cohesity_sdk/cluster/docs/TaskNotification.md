# TaskNotification

Structure that captures Task Notifications for a user.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**agent_upgrade_task** | [**AgentUpgradeTaskInfo**](AgentUpgradeTaskInfo.md) |  | [optional] 
**analysis_task** | [**AnalysisTaskInfo**](AnalysisTaskInfo.md) |  | [optional] 
**backup_task** | [**BackupTaskInfo**](BackupTaskInfo.md) |  | [optional] 
**bulk_install_app_task** | [**BulkInstallAppTaskInfo**](BulkInstallAppTaskInfo.md) |  | [optional] 
**clone_task** | [**CloneTaskInfo**](CloneTaskInfo.md) |  | [optional] 
**created_time_secs** | **int, none_type** | Timestamp at which the notification was created. | [optional] 
**description** | **str, none_type** | Description holds the actual notification text generated for the event. | [optional] 
**dismissed** | **bool, none_type** | Dismissed keeps track of whether a notification has been seen or not. User may choose to dismiss individual event or all notifications at once. Nil or 0 value represents false. | [optional] 
**dismissed_time_secs** | **int, none_type** | Timestamp at which user dismissed this notification event. | [optional] 
**field_message_task** | [**BasicTaskInfo**](BasicTaskInfo.md) |  | [optional] 
**id** | **str, none_type** | id identifies a user notification event uniquely. This can also be used to dismiss individual notifications. | [optional] 
**recovery_task** | [**RecoveryTaskInfo**](RecoveryTaskInfo.md) |  | [optional] 
**status** | **str, none_type** | Status of the task. Status of the task. &#39;kSuccess&#39; indicates that task completed successfully. &#39;kError&#39; indicates that task encountered errors. | [optional] 
**task_type** | **str, none_type** | Task type denotes which type of task this notification is for. This param is used to reflect the taskType. &#39;Restore&#39; notification type is generated upon completion of Restore tasks. &#39;Clone&#39; notification type is generated upon completion of Clone tasks. &#39;BackupNow&#39; notification type is generated upon completion of Backup tasks. &#39;FieldMessage&#39; notification type is generated when field message from Cohesity support is created. &#39;bulkInstallApp&#39; notification type is generated from bulk install app &#39;tiering&#39; notification type is generated upon completion of tiering tasks. &#39;analysis&#39; notification type is generated upon completion of analysis tasks. &#39;agentUpgradeTask&#39; notification type is generated upon completion of upgrade task. | [optional] 
**tiering_task** | [**TieringTaskInfo**](TieringTaskInfo.md) |  | [optional] 
**visited** | **bool, none_type** | Visited keeps track of whether a notification has been seen or not. | [optional] 
**visited_time_secs** | **int, none_type** | Timestamp at which user visited this notification event. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


