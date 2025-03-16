# HeliosCloudSpinTarget

Specifies the details about Cloud Spin target where backup snapshots may be converted and stored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**HeliosAwsCloudSpinParams**](HeliosAwsCloudSpinParams.md) |  | [optional] 
**azure_params** | [**HeliosAzureCloudSpinParams**](HeliosAzureCloudSpinParams.md) |  | [optional] 
**id** | **int** | Specifies the unique id of the cloud spin entity. | [optional] 
**name** | **str** | Specifies the name of the already added cloud spin target. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.helios.models.helios_cloud_spin_target import HeliosCloudSpinTarget

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosCloudSpinTarget from a JSON string
helios_cloud_spin_target_instance = HeliosCloudSpinTarget.from_json(json)
# print the JSON string representation of the object
print(HeliosCloudSpinTarget.to_json())

# convert the object into a dict
helios_cloud_spin_target_dict = helios_cloud_spin_target_instance.to_dict()
# create an instance of HeliosCloudSpinTarget from a dict
helios_cloud_spin_target_from_dict = HeliosCloudSpinTarget.from_dict(helios_cloud_spin_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


