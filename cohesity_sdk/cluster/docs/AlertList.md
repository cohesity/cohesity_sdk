# AlertList

Specifies the response of get alerts.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts** | [**List[AlertInfo]**](AlertInfo.md) | Specifies the list of alerts. | 

## Example

```python
from cohesity_sdk.cluster.models.alert_list import AlertList

# TODO update the JSON string below
json = "{}"
# create an instance of AlertList from a JSON string
alert_list_instance = AlertList.from_json(json)
# print the JSON string representation of the object
print(AlertList.to_json())

# convert the object into a dict
alert_list_dict = alert_list_instance.to_dict()
# create an instance of AlertList from a dict
alert_list_from_dict = AlertList.from_dict(alert_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


