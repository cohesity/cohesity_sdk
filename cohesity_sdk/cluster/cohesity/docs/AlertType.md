# AlertType

Alert type definition

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_document_list** | [**[AlertDocument]**](AlertDocument.md) | List of alert message templates | [optional] 
**alert_type_bucket** | **str** | Bucket/category this alert type belongs to | [optional] 
**alert_type_id** | **int** | Unique identifier for the alert type | [optional] 
**category** | **str** | Alert category | [optional] 
**dedup_interval_seconds** | **int** | Time in seconds before duplicate alerts are allowed | [optional] 
**dedup_until_resolved** | **bool** | Whether deduplication continues until alert is resolved | [optional] 
**primary_key_list** | **[str]** | Properties used for identifying unique alerts | [optional] 
**property_list** | **[str]** | List of properties used in alert messages | [optional] 
**snmp_notification** | **bool** | Whether SNMP notification is enabled | [optional] 
**version** | **int** | Version of the alert type definition | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


