# McmSourceRegistrationUpdateRequestParams

Specifies the request parameters to update a Protection Source.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**advanced_configs** | [**List[KeyValuePair]**](KeyValuePair.md) | Specifies the advanced configuration for a protection source. | [optional] 
**connection_id** | **int** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**connections** | [**List[ConnectionConfig]**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int** | Specifies the connector group id of connector groups. | [optional] 
**encryption_key** | **str** | Specifies the key that user has encrypted the credential with. | [optional] 
**environment** | **str** | Specifies the environment type of the Protection Source. | 
**is_internal_encrypted** | **bool** | Specifies if credentials are encrypted by internal key. | [optional] 
**name** | **str** | A user specified name for this source. | [optional] 
**aws_params** | [**AwsSourceRegistrationParams**](AwsSourceRegistrationParams.md) |  | [optional] 
**azure_params** | [**AzureSourceRegistrationParams**](AzureSourceRegistrationParams.md) |  | [optional] 
**cassandra_params** | [**CassandraSourceRegistrationParams**](CassandraSourceRegistrationParams.md) |  | [optional] 
**couchbase_params** | [**CouchbaseSourceRegistrationParams**](CouchbaseSourceRegistrationParams.md) |  | [optional] 
**elastifile_params** | [**ElastifileRegistrationParams**](ElastifileRegistrationParams.md) |  | [optional] 
**flashblade_params** | [**FlashbladeRegistrationParams**](FlashbladeRegistrationParams.md) |  | [optional] 
**generic_nas_params** | [**GenericNasRegistrationParams**](GenericNasRegistrationParams.md) |  | [optional] 
**gpfs_params** | [**GpfsRegistrationParams**](GpfsRegistrationParams.md) |  | [optional] 
**hbase_params** | [**HbaseSourceRegistrationParams**](HbaseSourceRegistrationParams.md) |  | [optional] 
**hdfs_params** | [**HdfsSourceRegistrationParams**](HdfsSourceRegistrationParams.md) |  | [optional] 
**hive_params** | [**HiveSourceRegistrationParams**](HiveSourceRegistrationParams.md) |  | [optional] 
**hyperv_params** | [**HyperVSourceRegistrationParams**](HyperVSourceRegistrationParams.md) |  | [optional] 
**isilon_params** | [**IsilonRegistrationParams**](IsilonRegistrationParams.md) |  | [optional] 
**mongodb_params** | [**MongoDBSourceRegistrationParams**](MongoDBSourceRegistrationParams.md) |  | [optional] 
**netapp_params** | [**NetappRegistrationParams**](NetappRegistrationParams.md) |  | [optional] 
**office365_params** | [**Office365SourceRegistrationParams**](Office365SourceRegistrationParams.md) |  | [optional] 
**physical_params** | [**PhysicalSourceRegistrationParams**](PhysicalSourceRegistrationParams.md) |  | [optional] 
**sfdc_params** | [**SfdcSourceRegistrationParams**](SfdcSourceRegistrationParams.md) |  | [optional] 
**uda_params** | [**UdaSourceRegistrationParams**](UdaSourceRegistrationParams.md) |  | [optional] 
**vmware_params** | [**VmwareSourceRegistrationParams**](VmwareSourceRegistrationParams.md) |  | [optional] 

## Example

```python
from cohesity_sdk.helios.models.mcm_source_registration_update_request_params import McmSourceRegistrationUpdateRequestParams

# TODO update the JSON string below
json = "{}"
# create an instance of McmSourceRegistrationUpdateRequestParams from a JSON string
mcm_source_registration_update_request_params_instance = McmSourceRegistrationUpdateRequestParams.from_json(json)
# print the JSON string representation of the object
print(McmSourceRegistrationUpdateRequestParams.to_json())

# convert the object into a dict
mcm_source_registration_update_request_params_dict = mcm_source_registration_update_request_params_instance.to_dict()
# create an instance of McmSourceRegistrationUpdateRequestParams from a dict
mcm_source_registration_update_request_params_from_dict = McmSourceRegistrationUpdateRequestParams.from_dict(mcm_source_registration_update_request_params_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


