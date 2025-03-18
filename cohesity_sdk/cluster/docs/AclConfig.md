# AclConfig

Specifies the ACL config of an S3 bucket.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**grants** | [**List[AclGrant]**](AclGrant.md) | Specifies a list of ACL grants. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.acl_config import AclConfig

# TODO update the JSON string below
json = "{}"
# create an instance of AclConfig from a JSON string
acl_config_instance = AclConfig.from_json(json)
# print the JSON string representation of the object
print(AclConfig.to_json())

# convert the object into a dict
acl_config_dict = acl_config_instance.to_dict()
# create an instance of AclConfig from a dict
acl_config_from_dict = AclConfig.from_dict(acl_config_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


