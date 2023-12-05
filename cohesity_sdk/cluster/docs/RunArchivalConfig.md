# RunArchivalConfig

Specifies settings for copying Snapshots External Targets (such as AWS or Tape). This also specifies the retention policy that should be applied to Snapshots after they have been copied to the specified target.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**archival_target_type** | **str, none_type** | Specifies the snapshot&#39;s archival target type from which recovery has been performed. | 
**id** | **int, none_type** | Specifies the Archival target to copy the Snapshots to. | 
**copy_only_fully_successful** | **bool, none_type** | Specifies if Snapshots are copied from a fully successful Protection Group Run or a partially successful Protection Group Run. If false, Snapshots are copied the Protection Group Run, even if the Run was not fully successful i.e. Snapshots were not captured for all Objects in the Protection Group. If true, Snapshots are copied only when the run is fully successful. | [optional] 
**retention** | [**Retention**](Retention.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


