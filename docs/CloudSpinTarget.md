# CloudSpinTarget

Specifies the details about Cloud Spin target where backup snapshots may be converted and stored.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**aws_params** | [**AwsCloudSpinParams**](AwsCloudSpinParams.md) |  | [optional] 
**azure_params** | [**AzureCloudSpinParams**](AzureCloudSpinParams.md) |  | [optional] 
**id** | **int** | Specifies the unique id of the cloud spin entity. | [optional] 
**name** | **str** | Specifies the name of the already added cloud spin target. | [optional] [readonly] 

## Example

```python
from cohesity_sdk.models.cloud_spin_target import CloudSpinTarget

# TODO update the JSON string below
json = "{}"
# create an instance of CloudSpinTarget from a JSON string
cloud_spin_target_instance = CloudSpinTarget.from_json(json)
# print the JSON string representation of the object
print(CloudSpinTarget.to_json())

# convert the object into a dict
cloud_spin_target_dict = cloud_spin_target_instance.to_dict()
# create an instance of CloudSpinTarget from a dict
cloud_spin_target_from_dict = CloudSpinTarget.from_dict(cloud_spin_target_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


