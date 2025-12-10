# AlertCategories

Alert category information

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_category** | **str** | Specifies the alert category. | [optional] 
**alert_name** | **str** | Name of the alert | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.alert_categories import AlertCategories

# TODO update the JSON string below
json = "{}"
# create an instance of AlertCategories from a JSON string
alert_categories_instance = AlertCategories.from_json(json)
# print the JSON string representation of the object
print(AlertCategories.to_json())

# convert the object into a dict
alert_categories_dict = alert_categories_instance.to_dict()
# create an instance of AlertCategories from a dict
alert_categories_from_dict = AlertCategories.from_dict(alert_categories_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


