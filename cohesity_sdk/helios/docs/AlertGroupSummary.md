# AlertGroupSummary

Specifies alerts summary grouped for an alert category.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**category** | **str** | Category of alerts by which summary is grouped. | [optional] 
**critical_count** | **int** | Specifies count of critical alerts. | [optional] 
**info_count** | **int** | Specifies count of info alerts. | [optional] 
**total_count** | **int** | Specifies count of total alerts. | [optional] 
**type** | **str** | Type/bucket that this alert category belongs to. | [optional] 
**warning_count** | **int** | Specifies count of warning alerts. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.alert_group_summary import AlertGroupSummary

# TODO update the JSON string below
json = "{}"
# create an instance of AlertGroupSummary from a JSON string
alert_group_summary_instance = AlertGroupSummary.from_json(json)
# print the JSON string representation of the object
print(AlertGroupSummary.to_json())

# convert the object into a dict
alert_group_summary_dict = alert_group_summary_instance.to_dict()
# create an instance of AlertGroupSummary from a dict
alert_group_summary_from_dict = AlertGroupSummary.from_dict(alert_group_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


