# Alert

Specifies the fields of an alert.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str, none_type** | Specifies unique id of the alert. | [optional] 
**alert_code** | **str, none_type** | Specifies a unique code that categorizes the Alert, for example: CE00200014, where CE stands for Cohesity Error, the alert state next 3 digits is the id of the Alert Category (e.g. 002 for &#39;kNode&#39;) and the last 5 digits is the id of the Alert Type (e.g. 00014 for &#39;kNodeHighCpuUsage&#39;). | [optional] 
**first_timestamp_usecs** | **int, none_type** | SpeSpecifies Unix epoch Timestamp (in microseconds) of the first occurrence of the Alert. | [optional] 
**latest_timestamp_usecs** | **int, none_type** | SpeSpecifies Unix epoch Timestamp (in microseconds) of the most recent occurrence of the Alert. | [optional] 
**alert_type** | **int, none_type** | Specifies the alert type. | [optional] 
**dedup_timestamps** | **[int], none_type** | Specifies Unix epoch Timestamps (in microseconds) for the last 25 occurrences of duplicated Alerts that are stored with the original/primary Alert. Alerts are grouped into one Alert if the Alerts are the same type, are reporting on the same Object and occur within one hour. &#39;dedupCount&#39; always reports the total count of duplicated Alerts even if there are more than 25 occurrences. For example, if there are 100 occurrences of this Alert, dedupTimestamps stores the timestamps of the last 25 occurrences and dedupCount equals 100. | [optional] 
**dedup_count** | **int, none_type** | Specifies the dedup count of alert. | [optional] 
**cluster_name** | **str, none_type** | Specifies the name of cluster which alert is raised from. | [optional] 
**region_id** | **str, none_type** | Specifies the region id of the alert. | [optional] 
**alert_type_bucket** | **str, none_type** | Specifies the Alert type bucket. | [optional] 
**alert_category** | **str, none_type** | Specifies the alert category. | [optional] 
**severity** | **str, none_type** | Specifies the alert severity. | [optional] 
**alert_state** | **str, none_type** | Specifies the alert state. | [optional] 
**alert_document** | [**AlertDocument**](AlertDocument.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


