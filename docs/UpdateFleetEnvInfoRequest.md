# UpdateFleetEnvInfoRequest

Specifies the params to add fleet env info.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**iam_role** | **str, none_type** | Specifies the IAM role used to create instances.This field is now deprecated, use awsFleetInfo instead. | [optional] 
**region** | **str, none_type** | Specifies the Region of the CE cluster. This field is now deprecated, use awsFleetInfo instead. | [optional] 
**vpc_id** | **str, none_type** | Specifies the VPC of the CE cluster.This field is now deprecated, use awsFleetInfo instead. | [optional] 
**subnet_id** | **str, none_type** | Specifies the Subnet of the CE cluster.This field is now deprecated, use awsFleetInfo instead. | [optional] 
**security_group_id** | **str, none_type** | Specifies the security group Id.This field is now deprecated, use awsFleetInfo instead. | [optional] 
**aws_fleet_info** | [**AwsFleetInfo**](AwsFleetInfo.md) |  | [optional] 
**azure_fleet_info** | [**AzureFleetInfo**](AzureFleetInfo.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


