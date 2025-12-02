# AlertType

Alert type definition

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_document_list** | [**List[AlertDocument]**](AlertDocument.md) | List of alert message templates | [optional] 
**alert_type_bucket** | **str** | Bucket/category this alert type belongs to | [optional] 
**alert_type_id** | **int** | Unique identifier for the alert type | [optional] 
**category** | **str** | Alert category | [optional] 
**dedup_interval_seconds** | **int** | Time in seconds before duplicate alerts are allowed | [optional] 
**dedup_until_resolved** | **bool** | Whether deduplication continues until alert is resolved | [optional] 
**primary_key_list** | **List[str]** | Properties used for identifying unique alerts | [optional] 
**property_list** | **List[str]** | List of properties used in alert messages | [optional] 
**snmp_notification** | **bool** | Whether SNMP notification is enabled | [optional] 
**version** | **int** | Version of the alert type definition | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.alert_type import AlertType

# TODO update the JSON string below
json = "{}"
# create an instance of AlertType from a JSON string
alert_type_instance = AlertType.from_json(json)
# print the JSON string representation of the object
print(AlertType.to_json())

# convert the object into a dict
alert_type_dict = alert_type_instance.to_dict()
# create an instance of AlertType from a dict
alert_type_from_dict = AlertType.from_dict(alert_type_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


