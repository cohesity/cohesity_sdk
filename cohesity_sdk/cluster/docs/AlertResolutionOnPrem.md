# AlertResolutionOnPrem

Provides Resolution details and the list of Alerts resolved by a Resolution. 

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_id_list** | **List[str]** | Specifies list of Alerts resolved by a Resolution, which are specified by Alert Ids.  | 
**resolution_details** | [**AlertResolutionDetailsV2**](AlertResolutionDetailsV2.md) |  | 
**tenant_ids** | **List[str]** | Specifies unique tenantIds of the alert contained in this resolution.  | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.alert_resolution_on_prem import AlertResolutionOnPrem

# TODO update the JSON string below
json = "{}"
# create an instance of AlertResolutionOnPrem from a JSON string
alert_resolution_on_prem_instance = AlertResolutionOnPrem.from_json(json)
# print the JSON string representation of the object
print(AlertResolutionOnPrem.to_json())

# convert the object into a dict
alert_resolution_on_prem_dict = alert_resolution_on_prem_instance.to_dict()
# create an instance of AlertResolutionOnPrem from a dict
alert_resolution_on_prem_from_dict = AlertResolutionOnPrem.from_dict(alert_resolution_on_prem_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


