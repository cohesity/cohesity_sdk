# HeliosReplicationConfig

Specifies settings for copying Snapshots to Remote Clusters. This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**config_id** | **str, none_type** | Specifies the unique identifier for the target getting added. This field need to be passed only when helios policies are updated. | [optional] 
**copy_on_run_success** | **bool, none_type** | Specifies if Snapshots are copied from the first completely successful Protection Group Run or the first partially successful Protection Group Run occurring at the start of the replication schedule. &lt;br&gt; If true, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule that was completely successful i.e. Snapshots for all the Objects in the Protection Group were successfully captured. &lt;br&gt; If false, Snapshots are copied from the first Protection Group Run occurring at the start of the replication schedule, even if first Protection Group Run was not completely successful i.e. Snapshots were not captured for all Objects in the Protection Group. | [optional] 
**retention** | [**HeliosRetention**](HeliosRetention.md) |  | [optional] 
**schedule** | [**HeliosTargetSchedule**](HeliosTargetSchedule.md) |  | [optional] 
**aws_target_config** | [**HeliosAWSTargetConfig**](HeliosAWSTargetConfig.md) |  | [optional] 
**azure_target_config** | [**HeliosAzureTargetConfig**](HeliosAzureTargetConfig.md) |  | [optional] 
**remote_target_config** | [**HeliosRemoteTargetConfig**](HeliosRemoteTargetConfig.md) |  | [optional] 
**target_type** | **str, none_type** | Specifies the type of target to which replication need to be performed. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


