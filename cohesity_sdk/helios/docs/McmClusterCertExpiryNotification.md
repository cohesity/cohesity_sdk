# McmClusterCertExpiryNotification

Lists clusters certificate expiry notification for an account.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | Specifies the cluster identifier for the cert. Format is of clusterId:clusterIncarnationId.  | [optional] 
**expiry_time_msecs** | **int** | Specifies a unix time in micro seconds when cluster certificate will expire. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_cluster_cert_expiry_notification import McmClusterCertExpiryNotification

# TODO update the JSON string below
json = "{}"
# create an instance of McmClusterCertExpiryNotification from a JSON string
mcm_cluster_cert_expiry_notification_instance = McmClusterCertExpiryNotification.from_json(json)
# print the JSON string representation of the object
print(McmClusterCertExpiryNotification.to_json())

# convert the object into a dict
mcm_cluster_cert_expiry_notification_dict = mcm_cluster_cert_expiry_notification_instance.to_dict()
# create an instance of McmClusterCertExpiryNotification from a dict
mcm_cluster_cert_expiry_notification_from_dict = McmClusterCertExpiryNotification.from_dict(mcm_cluster_cert_expiry_notification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


