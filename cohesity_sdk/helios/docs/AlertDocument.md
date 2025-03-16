# AlertDocument

Specifies the fields of alert document.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_cause** | **str** | Specifies the cause of alert. | [optional] 
**alert_description** | **str** | Specifies the description of alert. | [optional] 
**alert_help_text** | **str** | Specifies the help text for alert. | [optional] 
**alert_name** | **str** | Specifies the name of alert. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.alert_document import AlertDocument

# TODO update the JSON string below
json = "{}"
# create an instance of AlertDocument from a JSON string
alert_document_instance = AlertDocument.from_json(json)
# print the JSON string representation of the object
print(AlertDocument.to_json())

# convert the object into a dict
alert_document_dict = alert_document_instance.to_dict()
# create an instance of AlertDocument from a dict
alert_document_from_dict = AlertDocument.from_dict(alert_document_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


