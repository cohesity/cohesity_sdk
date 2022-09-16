# RemoteAdapterProtectionGroupParams

Specifies the parameters which are specific to Remote Adapter related Protection Groups.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**hosts** | [**[RemoteAdapterHost], none_type**](RemoteAdapterHost.md) | Specifies a list of hosts to protected in this protection group. | 
**view_id** | **int, none_type** | Specifies the id of the view where we put the script result data. | 
**remote_view_params** | [**RemoteAdapterProtectionGroupReplicationParams**](RemoteAdapterProtectionGroupReplicationParams.md) |  | [optional] 
**indexing_policy** | [**IndexingPolicy**](IndexingPolicy.md) |  | [optional] 
**app_consistent_snapshot** | **bool, none_type** | Specifies whether or not to quiesce apps and the file system in order to take app consistent snapshots. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


