# AwsCloudSpinParams

Specifies various resources when converting and deploying a VM to AWS.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**region** | **int, none_type** | Specifies id of the AWS region in which to deploy the VM. | 
**custom_tag_list** | [**[CustomTagParams], none_type**](CustomTagParams.md) | Specifies tags of various resources when converting and deploying a VM to AWS. | [optional] 
**subnet_id** | **int, none_type** | Specifies id of the subnet within above VPC. | [optional] 
**vpc_id** | **int, none_type** | Specifies id of the Virtual Private Cloud to chose for the instance type. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


