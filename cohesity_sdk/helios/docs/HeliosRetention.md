# HeliosRetention

Specifies the retention of a backup.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data_lock_config** | [**DataLockConfig**](DataLockConfig.md) |  | [optional] 
**duration** | **int** | Specifies the duration for a backup retention. &lt;br&gt; Example. If duration is 7 and unit is Months, the retention of a backup is 7 * 30 &#x3D; 210 days. | [optional] 
**tiers** | [**List[HeliosTier]**](HeliosTier.md) | Specifies the list of tiers where backup will be moved. This will be populated only if poilcy type is DMaaS. | [optional] 
**unit** | **str** | Specificies the Retention Unit of a backup measured in days, months or years. &lt;br&gt; If unit is &#39;Months&#39;, then number specified in duration is multiplied to 30. &lt;br&gt; Example: If duration is 4 and unit is &#39;Months&#39; then number of retention days will be 30 * 4 &#x3D; 120 days. &lt;br&gt; If unit is &#39;Years&#39;, then number specified in duration is multiplied to 365. &lt;br&gt; If duration is 2 and unit is &#39;Months&#39; then number of retention days will be 365 * 2 &#x3D; 730 days. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_retention import HeliosRetention

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosRetention from a JSON string
helios_retention_instance = HeliosRetention.from_json(json)
# print the JSON string representation of the object
print(HeliosRetention.to_json())

# convert the object into a dict
helios_retention_dict = helios_retention_instance.to_dict()
# create an instance of HeliosRetention from a dict
helios_retention_from_dict = HeliosRetention.from_dict(helios_retention_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


