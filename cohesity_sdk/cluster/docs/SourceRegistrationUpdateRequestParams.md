# SourceRegistrationUpdateRequestParams

Specifies the Source registration Update request parameters.

## Properties
Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**environment** | **str, none_type** | Specifies the environment type of the Protection Source. | 
**connection_id** | **int, none_type** | Specifies the id of the connection from where this source is reachable. This should only be set for a source being registered by a tenant user. | [optional] 
**connections** | [**[ConnectionConfig], none_type**](ConnectionConfig.md) | Specfies the list of connections for the source. | [optional] 
**connector_group_id** | **int, none_type** | Specifies the connector group id of connector groups. | [optional] 
**encryption_key** | **str, none_type** | Specifies the key that user has encrypted the credential with. | [optional] 
**is_internal_encrypted** | **bool, none_type** | Specifies if credentials are encrypted by internal key. | [optional] 
**name** | **str, none_type** | A user specified name for this source. | [optional] 
**aws_params** | [**AwsSourceRegistrationParams**](AwsSourceRegistrationParams.md) |  | [optional] 
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

[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


