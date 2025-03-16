# HeliosAwsCloudSpinParams

Specifies various resources when converting and deploying a VM to AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **int** | Specifies id of the AWS region in which to deploy the VM. | 
**subnet_id** | **int** | Specifies id of the subnet within above VPC. | [optional] 
**vpc_id** | **int** | Specifies id of the Virtual Private Cloud to chose for the instance type. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_aws_cloud_spin_params import HeliosAwsCloudSpinParams

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAwsCloudSpinParams from a JSON string
helios_aws_cloud_spin_params_instance = HeliosAwsCloudSpinParams.from_json(json)
# print the JSON string representation of the object
print(HeliosAwsCloudSpinParams.to_json())

# convert the object into a dict
helios_aws_cloud_spin_params_dict = helios_aws_cloud_spin_params_instance.to_dict()
# create an instance of HeliosAwsCloudSpinParams from a dict
helios_aws_cloud_spin_params_from_dict = HeliosAwsCloudSpinParams.from_dict(helios_aws_cloud_spin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


