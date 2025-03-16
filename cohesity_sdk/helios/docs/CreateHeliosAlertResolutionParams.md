# CreateHeliosAlertResolutionParams

Provides Resolution details and the list of Alerts to be resolved

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**description** | **str** | Specifies the full description about the Resolution. | 
**resolution_name** | **str** | Specifies the unique name of the resolution. | 
**resolved_alerts** | [**List[CreateHeliosAlertResolutionParamsResolvedAlertsInner]**](CreateHeliosAlertResolutionParamsResolvedAlertsInner.md) |  | 

## Example

```python
from cohesity_sdk.helios.models.create_helios_alert_resolution_params import CreateHeliosAlertResolutionParams

# TODO update the JSON string below
json = "{}"
# create an instance of CreateHeliosAlertResolutionParams from a JSON string
create_helios_alert_resolution_params_instance = CreateHeliosAlertResolutionParams.from_json(json)
# print the JSON string representation of the object
print(CreateHeliosAlertResolutionParams.to_json())

# convert the object into a dict
create_helios_alert_resolution_params_dict = create_helios_alert_resolution_params_instance.to_dict()
# create an instance of CreateHeliosAlertResolutionParams from a dict
create_helios_alert_resolution_params_from_dict = CreateHeliosAlertResolutionParams.from_dict(create_helios_alert_resolution_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


