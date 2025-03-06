# CassandraSecurityInfo

Cassandra security related info.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**cassandra_auth_required** | **bool** | Is Cassandra authentication required ? | [optional] 
**cassandra_auth_type** | **str** | Cassandra Authentication type. | [optional] 
**cassandra_authorizer** | **str** | Cassandra Authenticator/Authorizer. | [optional] 
**client_encryption** | **bool** | Is Client Encryption enabled for this cluster ? | [optional] 
**dse_authorization** | **bool** | Is DSE Authorization enabled for this cluster ? | [optional] 
**server_encryption_req_client_auth** | **bool** | Is &#39;Server encryption request client authentication&#39; enabled for this cluster ? | [optional] 
**server_internode_encryption_type** | **str** | &#39;Server internal node Encryption&#39; type. | [optional] 

## Example

```python
from cohesity_sdk.cluster.models.cassandra_security_info import CassandraSecurityInfo

# TODO update the JSON string below
json = "{}"
# create an instance of CassandraSecurityInfo from a JSON string
cassandra_security_info_instance = CassandraSecurityInfo.from_json(json)
# print the JSON string representation of the object
print(CassandraSecurityInfo.to_json())

# convert the object into a dict
cassandra_security_info_dict = cassandra_security_info_instance.to_dict()
# create an instance of CassandraSecurityInfo from a dict
cassandra_security_info_from_dict = CassandraSecurityInfo.from_dict(cassandra_security_info_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


