# RunCloudReplicationConfig

Specifies settings for copying Snapshots to cloud targets. This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**target_type** | **str** | Specifies the type of target to which replication need to be performed. | 
**aws_target** | [**AWSTargetConfig**](AWSTargetConfig.md) |  | [optional] 
**azure_target** | [**AzureTargetConfig**](AzureTargetConfig.md) |  | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


