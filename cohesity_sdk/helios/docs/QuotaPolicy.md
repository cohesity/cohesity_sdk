# QuotaPolicy

Specifies a quota limit that can be optionally applied to Views and   Storage Domains.   At the View level, this quota defines a logical limit for usage on the View.   At the Storage Domain level, this quota defines a physical limit or   a default logical View limit.   If a physical quota is specified for Storage Domain, this quota defines a physical   limit for the usage on the Storage Domain.   If a default logical View quota is specified for Storage Domain, this limit   is inherited by all the Views in that Storage Domain.   However, this inherited quota can be overwritten at the View level.   A new write is not allowed if the resource will exceed the specified quota.   However, it takes time for the Cohesity Cluster to calculate   the usage across Nodes, so the limit may be exceeded by a small amount.   In addition, if the limit is increased or data is removed,   there may be a delay before the Cohesity Cluster allows more data   to be written to the resource, as the Cluster calculates the usage   across Nodes.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**alert_limit_bytes** | **int, none_type** | Specifies if an alert should be triggered when the usage of this   resource exceeds this quota limit.   This limit is optional and is specified in bytes.   If no value is specified, there is no limit. | [optional] 
**alert_threshold_percentage** | **int, none_type** | Supported only for user quota policy.   Specifies when the usage goes above an alert threshold percentage   which is:   HardLimitBytes * AlertThresholdPercentage, eg: 80% of HardLimitBytes   Can only be set if HardLimitBytes is set.   Cannot be set if AlertLimitBytes is already set. | [optional] 
**hard_limit_bytes** | **int, none_type** | Specifies an optional quota limit on the usage allowed for this   resource. This limit is specified in bytes. If no value is specified,   there is no limit. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


