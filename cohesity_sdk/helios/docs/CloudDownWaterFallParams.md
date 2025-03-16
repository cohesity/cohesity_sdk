# CloudDownWaterFallParams

Specifies parameters for cloud down water fall thresholds.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**threshold_percentage** | **int** | Specifies the threshold percentage for cloud down water fall. This value indicates how full a storage domain is before cohesity cluster down water fall its data to cloud tier. This field is only appliciable if physicalQuota is set. | [optional] 
**threshold_secs** | **int** | Specifes a time in seconds when cloud down water fall starts. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.cloud_down_water_fall_params import CloudDownWaterFallParams

# TODO update the JSON string below
json = "{}"
# create an instance of CloudDownWaterFallParams from a JSON string
cloud_down_water_fall_params_instance = CloudDownWaterFallParams.from_json(json)
# print the JSON string representation of the object
print(CloudDownWaterFallParams.to_json())

# convert the object into a dict
cloud_down_water_fall_params_dict = cloud_down_water_fall_params_instance.to_dict()
# create an instance of CloudDownWaterFallParams from a dict
cloud_down_water_fall_params_from_dict = CloudDownWaterFallParams.from_dict(cloud_down_water_fall_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


