# ViewClientsSummary

Specifies the View Client summary.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**summary** | [**List[ViewClientsSummaryInfo]**](ViewClientsSummaryInfo.md) | Specifies a list of summary. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.view_clients_summary import ViewClientsSummary

# TODO update the JSON string below
json = "{}"
# create an instance of ViewClientsSummary from a JSON string
view_clients_summary_instance = ViewClientsSummary.from_json(json)
# print the JSON string representation of the object
print(ViewClientsSummary.to_json())

# convert the object into a dict
view_clients_summary_dict = view_clients_summary_instance.to_dict()
# create an instance of ViewClientsSummary from a dict
view_clients_summary_from_dict = ViewClientsSummary.from_dict(view_clients_summary_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


