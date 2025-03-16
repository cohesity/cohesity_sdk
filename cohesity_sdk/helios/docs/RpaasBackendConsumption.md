# RpaasBackendConsumption

Specifies the RPaaS consumption in terms of backend usage.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region_id** | **str** | The current region for which usage is calculated. | [optional] 
**usage** | [**List[RpaasBackendUsage]**](RpaasBackendUsage.md) | The current usage per region. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.rpaas_backend_consumption import RpaasBackendConsumption

# TODO update the JSON string below
json = "{}"
# create an instance of RpaasBackendConsumption from a JSON string
rpaas_backend_consumption_instance = RpaasBackendConsumption.from_json(json)
# print the JSON string representation of the object
print(RpaasBackendConsumption.to_json())

# convert the object into a dict
rpaas_backend_consumption_dict = rpaas_backend_consumption_instance.to_dict()
# create an instance of RpaasBackendConsumption from a dict
rpaas_backend_consumption_from_dict = RpaasBackendConsumption.from_dict(rpaas_backend_consumption_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


