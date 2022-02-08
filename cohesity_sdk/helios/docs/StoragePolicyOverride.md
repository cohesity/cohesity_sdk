# StoragePolicyOverride

Specifies if inline deduplication and compression settings inherited from   Storage Domain (View Box) should be disabled for this View.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**disable_inline_dedup_and_compression** | **bool, none_type** | If false, the inline deduplication and compression settings inherited   from the Storage Domain (View Box) apply to this View.   If true, both inline deduplication and compression are disabled for this   View. This can only be set to true if inline deduplication is set for   the Storage Domain (View Box). | [optional] 
**disable_dedup** | **bool, none_type** | If it is set to true, we would disable dedup for writes made in this   view irrespective of the view box&#39;s storage policy. | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


