# ActiveDirectoryTopology

Response of Active directory topology.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**member_domains** | [**{str: (MemberDomain,)}, none_type**](MemberDomain.md) | Specifies map of domains where the key represents FQDN (fully qualified domain name) of each domain. The map contains both primary and trusted domains. | [optional] 
**primary_domains** | [**{str: (PrimaryDomain,)}, none_type**](PrimaryDomain.md) | Specifies map of primary domains where the key represents FQDN (fully qualified domain name) of each primary domain. | [optional] 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


