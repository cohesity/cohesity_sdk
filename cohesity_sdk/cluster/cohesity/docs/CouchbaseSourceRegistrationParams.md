# CouchbaseSourceRegistrationParams

Specifies parameters to register Couchbase source.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**password** | **str** | Specifies the password to access target entity. | 
**username** | **str** | Specifies the username to access target entity. | 
**carrier_port** | **int, none_type** | Carrier direct or Carrier SSL port. | 
**http_port** | **int, none_type** | HTTP direct or HTTP SSL port. | 
**is_ssl_required** | **bool, none_type** | Set to true if connection to couchbase has to be using SSL. | 
**seeds** | **[str]** | Specifies the IP Addresses or hostnames of the Couchbase cluster seed nodes. | 
**any string name** | **bool, date, datetime, dict, float, int, list, str, none_type** | any string name can be used but the value must be the correct type | [optional]

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


