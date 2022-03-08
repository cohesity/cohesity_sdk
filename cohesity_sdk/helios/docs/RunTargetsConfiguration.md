# RunTargetsConfiguration

Specifies the replication and archival targets.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_policy_defaults** | **bool, none_type** | Specifies whether to use default policy settings or not. If specified as true then &#39;replications&#39; and &#39;arcihvals&#39; should not be specified. In case of true value, replicatioan targets congfigured in the policy will be added internally. | [optional]  if omitted the server will use the default value of False
**replications** | [**[RunReplicationConfig], none_type**](RunReplicationConfig.md) | Specifies a list of replication targets configurations. | [optional] 
**archivals** | [**[RunArchivalConfig], none_type**](RunArchivalConfig.md) | Specifies a list of archival targets configurations. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


