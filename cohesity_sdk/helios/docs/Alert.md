# Alert

Specifies the fields of an alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_category** | **str** | Specifies the alert category. | [optional] 
**alert_code** | **str** | Specifies a unique code that categorizes the Alert, for example: CE00200014, where CE stands for Cohesity Error, the alert state next 3 digits is the id of the Alert Category (e.g. 002 for &#39;kNode&#39;) and the last 5 digits is the id of the Alert Type (e.g. 00014 for &#39;kNodeHighCpuUsage&#39;). | [optional] 
**alert_document** | [**AlertDocument**](AlertDocument.md) |  | [optional] 
**alert_state** | **str** | Specifies the alert state. | [optional] 
**alert_type** | **int** | Specifies the alert type. | [optional] 
**alert_type_bucket** | **str** | Specifies the Alert type bucket. | [optional] 
**cluster_name** | **str** | Specifies the name of cluster which alert is raised from. | [optional] 
**dedup_count** | **int** | Specifies the dedup count of alert. | [optional] 
**dedup_timestamps** | **List[int]** | Specifies Unix epoch Timestamps (in microseconds) for the last 25 occurrences of duplicated Alerts that are stored with the original/primary Alert. Alerts are grouped into one Alert if the Alerts are the same type, are reporting on the same Object and occur within one hour. &#39;dedupCount&#39; always reports the total count of duplicated Alerts even if there are more than 25 occurrences. For example, if there are 100 occurrences of this Alert, dedupTimestamps stores the timestamps of the last 25 occurrences and dedupCount equals 100. | [optional] 
**first_timestamp_usecs** | **int** | SpeSpecifies Unix epoch Timestamp (in microseconds) of the first occurrence of the Alert. | [optional] 
**id** | **str** | Specifies unique id of the alert. | [optional] 
**latest_timestamp_usecs** | **int** | SpeSpecifies Unix epoch Timestamp (in microseconds) of the most recent occurrence of the Alert. | [optional] 
**region_id** | **str** | Specifies the region id of the alert. | [optional] 
**severity** | **str** | Specifies the alert severity. | [optional] 
**vaults** | [**List[Vault]**](Vault.md) | Specifies information about vaults where source object associated with alert is vaulted. This could be empty if alert is not related to any source object or it is not vaulted. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.alert import Alert

# TODO update the JSON string below
json = "{}"
# create an instance of Alert from a JSON string
alert_instance = Alert.from_json(json)
# print the JSON string representation of the object
print(Alert.to_json())

# convert the object into a dict
alert_dict = alert_instance.to_dict()
# create an instance of Alert from a dict
alert_from_dict = Alert.from_dict(alert_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


