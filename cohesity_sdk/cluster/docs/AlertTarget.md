# AlertTarget

Specifies an alert target to receive an alert.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**email_address** | **str** | Specifies an email address to receive an alert. | 
**language** | **str** | Specifies the language of the delivery target. Default value is &#39;en-us&#39;. | [optional] 
**recipient_type** | **str** | Specifies the recipient type of email recipient. Default value is &#39;kTo&#39;. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.alert_target import AlertTarget

# TODO update the JSON string below
json = "{}"
# create an instance of AlertTarget from a JSON string
alert_target_instance = AlertTarget.from_json(json)
# print the JSON string representation of the object
print(AlertTarget.to_json())

# convert the object into a dict
alert_target_dict = alert_target_instance.to_dict()
# create an instance of AlertTarget from a dict
alert_target_from_dict = AlertTarget.from_dict(alert_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


