# AwsCloudSpinParams

Specifies various resources when converting and deploying a VM to AWS.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**custom_tag_list** | [**List[CustomTagParams]**](CustomTagParams.md) | Specifies tags of various resources when converting and deploying a VM to AWS. | [optional] 
**region** | **int** | Specifies id of the AWS region in which to deploy the VM. | 
**subnet_id** | **int** | Specifies id of the subnet within above VPC. | [optional] 
**vpc_id** | **int** | Specifies id of the Virtual Private Cloud to chose for the instance type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.aws_cloud_spin_params import AwsCloudSpinParams

# TODO update the JSON string below
json = "{}"
# create an instance of AwsCloudSpinParams from a JSON string
aws_cloud_spin_params_instance = AwsCloudSpinParams.from_json(json)
# print the JSON string representation of the object
print(AwsCloudSpinParams.to_json())

# convert the object into a dict
aws_cloud_spin_params_dict = aws_cloud_spin_params_instance.to_dict()
# create an instance of AwsCloudSpinParams from a dict
aws_cloud_spin_params_from_dict = AwsCloudSpinParams.from_dict(aws_cloud_spin_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


