# Retention

Specifies the retention of a backup.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**unit** | **str, none_type** | Specificies the Retention Unit of a backup measured in days, months or years. &lt;br&gt; If unit is &#39;Months&#39;, then number specified in duration is multiplied to 30. &lt;br&gt; Example: If duration is 4 and unit is &#39;Months&#39; then number of retention days will be 30 * 4 &#x3D; 120 days. &lt;br&gt; If unit is &#39;Years&#39;, then number specified in duration is multiplied to 365. &lt;br&gt; If duration is 2 and unit is &#39;Months&#39; then number of retention days will be 365 * 2 &#x3D; 730 days. | 
**duration** | **int, none_type** | Specifies the duration for a backup retention. &lt;br&gt; Example. If duration is 7 and unit is Months, the retention of a backup is 7 * 30 &#x3D; 210 days. | 
**data_lock_config** | [**DataLockConfig**](DataLockConfig.md) |  | [optional] 

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


