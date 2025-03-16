# HeliosAuditLogClusterUser

Specifies cluster user for helios audit log message.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cluster_identifier** | **str** | Specifies cluster identifier. The format is clusterId:clusterIncarnationId. | [optional] 
**cluster_name** | **str** | Specifies cluster name. | [optional] 
**users** | [**List[HeliosAuditLogUser]**](HeliosAuditLogUser.md) | Specifies cluster users. | [optional] 

## Example

```python
from cohesity_sdk.helios.models.helios_audit_log_cluster_user import HeliosAuditLogClusterUser

# TODO update the JSON string below
json = "{}"
# create an instance of HeliosAuditLogClusterUser from a JSON string
helios_audit_log_cluster_user_instance = HeliosAuditLogClusterUser.from_json(json)
# print the JSON string representation of the object
print(HeliosAuditLogClusterUser.to_json())

# convert the object into a dict
helios_audit_log_cluster_user_dict = helios_audit_log_cluster_user_instance.to_dict()
# create an instance of HeliosAuditLogClusterUser from a dict
helios_audit_log_cluster_user_from_dict = HeliosAuditLogClusterUser.from_dict(helios_audit_log_cluster_user_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


