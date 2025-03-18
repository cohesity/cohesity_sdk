# DataLockConfig

Specifies WORM retention type for the snapshots. When a WORM retention type is specified, the snapshots of the Protection Groups using this policy will be kept for the last N days as specified in the duration of the datalock. During that time, the snapshots cannot be deleted.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**duration** | **int** | Specifies the duration for a dataLock. &lt;br&gt; Example. If duration is 7 and unit is Months, the dataLock is enabled for last 7 * 30 &#x3D; 210 days of the backup. | 
**enable_worm_on_external_target** | **bool** | Specifies whether objects in the external target associated with this policy need to be made immutable. | [optional] 
**mode** | **str** | Specifies the type of WORM retention type.  &#39;Compliance&#39; implies WORM retention is set for compliance reason.  &#39;Administrative&#39; implies WORM retention is set for administrative purposes. | 
**unit** | **str** | Specificies the Retention Unit of a dataLock measured in days, months or years. &lt;br&gt; If unit is &#39;Months&#39;, then number specified in duration is multiplied to 30. &lt;br&gt; Example: If duration is 4 and unit is &#39;Months&#39; then number of retention days will be 30 * 4 &#x3D; 120 days. &lt;br&gt; If unit is &#39;Years&#39;, then number specified in duration is multiplied to 365. &lt;br&gt; If duration is 2 and unit is &#39;Months&#39; then number of retention days will be 365 * 2 &#x3D; 730 days. | 

## Example

```python
from cohesity_sdk.cluster.models.data_lock_config import DataLockConfig

# TODO update the JSON string below
json = "{}"
# create an instance of DataLockConfig from a JSON string
data_lock_config_instance = DataLockConfig.from_json(json)
# print the JSON string representation of the object
print(DataLockConfig.to_json())

# convert the object into a dict
data_lock_config_dict = data_lock_config_instance.to_dict()
# create an instance of DataLockConfig from a dict
data_lock_config_from_dict = DataLockConfig.from_dict(data_lock_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


