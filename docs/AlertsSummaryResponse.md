# AlertsSummaryResponse

Specifies the response of alerts summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alerts_summary** | [**List[AlertGroupSummary]**](AlertGroupSummary.md) | Specifies a list of alerts summary grouped by category. | [optional] 

## Example

```python
from cohesity_sdk.models.alerts_summary_response import AlertsSummaryResponse

# TODO update the JSON string below
json = "{}"
# create an instance of AlertsSummaryResponse from a JSON string
alerts_summary_response_instance = AlertsSummaryResponse.from_json(json)
# print the JSON string representation of the object
print(AlertsSummaryResponse.to_json())

# convert the object into a dict
alerts_summary_response_dict = alerts_summary_response_instance.to_dict()
# create an instance of AlertsSummaryResponse from a dict
alerts_summary_response_from_dict = AlertsSummaryResponse.from_dict(alerts_summary_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


