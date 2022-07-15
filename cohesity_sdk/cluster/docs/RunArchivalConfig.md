# RunArchivalConfig

Specifies settings for copying Snapshots External Targets (such as AWS or Tape). This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **int, none_type** | Specifies the Archival target to copy the Snapshots to. | 
**archival_target_type** | **str, none_type** | Specifies the snapshot&#39;s archival target type from which recovery has been performed. | 
**retention** | [**Retention**](Retention.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


