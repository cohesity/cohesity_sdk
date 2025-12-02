# AlertResolutionDetailsV2

Specifies information about the Alert Resolution.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**resolution_details** | **str** | Specifies detailed notes about the Resolution. | [optional] 
**resolution_id** | **int** | Specifies the unique resolution id assigned in helios. | [optional] 
**resolution_summary** | **str** | Specifies short description about the Resolution. | 
**timestamp_usecs** | **int** | Specifies unix epoch timestamp (in microseconds) when the Alert was resolved.  | [optional] 
**user_name** | **str** | Specifies name of the Cohesity Cluster user who resolved the Alerts.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.alert_resolution_details_v2 import AlertResolutionDetailsV2

# TODO update the JSON string below
json = "{}"
# create an instance of AlertResolutionDetailsV2 from a JSON string
alert_resolution_details_v2_instance = AlertResolutionDetailsV2.from_json(json)
# print the JSON string representation of the object
print(AlertResolutionDetailsV2.to_json())

# convert the object into a dict
alert_resolution_details_v2_dict = alert_resolution_details_v2_instance.to_dict()
# create an instance of AlertResolutionDetailsV2 from a dict
alert_resolution_details_v2_from_dict = AlertResolutionDetailsV2.from_dict(alert_resolution_details_v2_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


