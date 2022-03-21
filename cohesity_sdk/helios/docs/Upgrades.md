# Upgrades

Specifies clusters upgrade request like clusterId, release upgrade URL, time stamp to upgrade at, intervals for rolling upgrade in hours.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**clusters** | [**[Upgrade], none_type**](Upgrade.md) | Array for clusters to be upgraded. | [optional] 
**target_version** | **str** | Specifies target version to which clusters are to be upgraded. | [optional] 
**time_stamp_to_upgrade_at_msecs** | **int** | Specifies the time in msecs at which the cluster has to be upgraded. | [optional] 
**interval_for_rolling_upgrade_in_hours** | **int, none_type** | Specifies the difference of time between two cluster&#39;s upgrade. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


