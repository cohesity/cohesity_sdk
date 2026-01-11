# AlertInfo

Specifies the fields of an alert.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_category** | **str, none_type** | Specifies the alert category. | [optional] 
**alert_code** | **str, none_type** | Specifies a unique code that categorizes the Alert, for example: CE00200014, where CE stands for Cohesity Error, the alert state next 3 digits is the id of the Alert Category (e.g. 002 for &#39;kNode&#39;) and the last 5 digits is the id of the Alert Type (e.g. 00014 for &#39;kNodeHighCpuUsage&#39;). | [optional] 
**alert_document** | [**AlertDocument**](AlertDocument.md) |  | [optional] 
**alert_state** | **str, none_type** | Specifies the alert state. | [optional] 
**alert_type** | **int, none_type** | Specifies the alert type. | [optional] 
**alert_type_bucket** | **str, none_type** | Specifies the Alert type bucket. | [optional] 
**cluster_id** | **int, none_type** | Id of the cluster which the alert is associated | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of cluster which alert is raised from. | [optional] 
**dedup_count** | **int, none_type** | Specifies the dedup count of alert. | [optional] 
**dedup_timestamps** | **[int]** | Specifies Unix epoch Timestamps (in microseconds) for the last 25 occurrences of duplicated Alerts that are stored with the original/primary Alert. Alerts are grouped into one Alert if the Alerts are the same type, are reporting on the same Object and occur within one hour. &#39;dedupCount&#39; always reports the total count of duplicated Alerts even if there are more than 25 occurrences. For example, if there are 100 occurrences of this Alert, dedupTimestamps stores the timestamps of the last 25 occurrences and dedupCount equals 100. | [optional] 
**event_source** | **str, none_type** | Specifies source where the event occurred. | [optional] 
**first_timestamp_usecs** | **int, none_type** | Specifies Unix epoch Timestamp (in microseconds) of the first occurrence of the Alert. | [optional] 
**id** | **str, none_type** | Specifies unique id of the alert. | [optional] 
**label_ids** | **[str], none_type** | Specifies the labels for which this alert has been raised. | [optional] 
**latest_timestamp_usecs** | **int, none_type** | Specifies Unix epoch Timestamp (in microseconds) of the most recent occurrence of the Alert. | [optional] 
**property_list** | [**[Label]**](Label.md) | List of property key and values associated with alert | [optional] 
**region_id** | **str, none_type** | Specifies the region id of the alert. | [optional] 
**resolution_details** | [**AlertResolutionDetails**](AlertResolutionDetails.md) |  | [optional] 
**resolution_id_string** | **str, none_type** | Resolution Id String. | [optional] 
**resolved_timestamp_usecs** | **int, none_type** | Specifies Unix epoch Timestamps in microseconds when alert is resolved. | [optional] 
**severity** | **str, none_type** | Specifies the alert severity. | [optional] 
**suppression_id** | **int, none_type** | Specifies unique id generated when the Alert is suppressed by the admin. | [optional] 
**tenant_ids** | **[str]** | Specifies the tenants for which this alert has been raised. | [optional] 
**vaults** | [**[Vault], none_type**](Vault.md) | Specifies information about vaults where source object associated with alert is vaulted. This could be empty if alert is not related to any source object or it is not vaulted. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


