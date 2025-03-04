# GetTrackingViewIdResponse

Specifies the response upon requesting a tracking view id

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tracking_view_id** | **int** | Specifies the local view id corresponding to the view uid. | [optional] 

## Example

```python
from cohesity_sdk.models.get_tracking_view_id_response import GetTrackingViewIdResponse

# TODO update the JSON string below
json = "{}"
# create an instance of GetTrackingViewIdResponse from a JSON string
get_tracking_view_id_response_instance = GetTrackingViewIdResponse.from_json(json)
# print the JSON string representation of the object
print(GetTrackingViewIdResponse.to_json())

# convert the object into a dict
get_tracking_view_id_response_dict = get_tracking_view_id_response_instance.to_dict()
# create an instance of GetTrackingViewIdResponse from a dict
get_tracking_view_id_response_from_dict = GetTrackingViewIdResponse.from_dict(get_tracking_view_id_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


