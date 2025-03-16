# UpgradeNotification

Lists cluster upgrade notifications for an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**is_upgrade_available** | **bool** | Specifies whether an upgrade is available for any of the clusters. | [optional] 
**num_clusters_upgrade_available** | **int** | Specifies the number of clusters with upgrade available. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.upgrade_notification import UpgradeNotification

# TODO update the JSON string below
json = "{}"
# create an instance of UpgradeNotification from a JSON string
upgrade_notification_instance = UpgradeNotification.from_json(json)
# print the JSON string representation of the object
print(UpgradeNotification.to_json())

# convert the object into a dict
upgrade_notification_dict = upgrade_notification_instance.to_dict()
# create an instance of UpgradeNotification from a dict
upgrade_notification_from_dict = UpgradeNotification.from_dict(upgrade_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


