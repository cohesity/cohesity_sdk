# AlertResolutionsList

Specifies the alert resolutions for get alert resolutions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_resolutions_list** | [**List[AlertResolution]**](AlertResolution.md) | List of alert resolutions. | 

## Example

```python
from cohesity_sdk.helios.models.alert_resolutions_list import AlertResolutionsList

# TODO update the JSON string below
json = "{}"
# create an instance of AlertResolutionsList from a JSON string
alert_resolutions_list_instance = AlertResolutionsList.from_json(json)
# print the JSON string representation of the object
print(AlertResolutionsList.to_json())

# convert the object into a dict
alert_resolutions_list_dict = alert_resolutions_list_instance.to_dict()
# create an instance of AlertResolutionsList from a dict
alert_resolutions_list_from_dict = AlertResolutionsList.from_dict(alert_resolutions_list_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


