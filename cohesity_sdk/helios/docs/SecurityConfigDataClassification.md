# SecurityConfigDataClassification

Specifies security config for data classification.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**classified_data_message** | **str** | Specifies the classified data message. | [optional] 
**is_data_classified** | **bool** | Specifies whether to mark the web page data classified/unclassified. | [optional] 
**unclassified_data_message** | **str** | Specifies the unclassified data message. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.security_config_data_classification import SecurityConfigDataClassification

# TODO update the JSON string below
json = "{}"
# create an instance of SecurityConfigDataClassification from a JSON string
security_config_data_classification_instance = SecurityConfigDataClassification.from_json(json)
# print the JSON string representation of the object
print(SecurityConfigDataClassification.to_json())

# convert the object into a dict
security_config_data_classification_dict = security_config_data_classification_instance.to_dict()
# create an instance of SecurityConfigDataClassification from a dict
security_config_data_classification_from_dict = SecurityConfigDataClassification.from_dict(security_config_data_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


